"""
Apex Sigma: The Database Giant Discord Bot.
Copyright (C) 2019  Lucia's Cipher

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import errno
import os
import shutil

import arrow
import discord
from pymongo.errors import OperationFailure, ServerSelectionTimeoutError

from sigma.core.mechanics.caching import get_cache
from sigma.core.mechanics.config import Configuration
from sigma.core.mechanics.cooldown import CooldownControl
from sigma.core.mechanics.database import Database
from sigma.core.mechanics.executor import ExecutionClockwork
from sigma.core.mechanics.fetch import get_fetch_helper
from sigma.core.mechanics.information import Information
from sigma.core.mechanics.logger import create_logger
from sigma.core.mechanics.modman import ModuleManager
from sigma.core.mechanics.music import MusicCore
from sigma.core.mechanics.payload import BanPayload, GuildPayload, GuildUpdatePayload, MemberPayload
from sigma.core.mechanics.payload import MemberUpdatePayload, MessageEditPayload, MessagePayload, RawReactionPayload
from sigma.core.mechanics.payload import ReactionPayload, ShardReadyPayload, UnbanPayload, VoiceStateUpdatePayload
from sigma.core.utilities.data_processing import set_color_cache_coll

# I love spaghetti!
# Valebu pls, no take my spaghetti... :'(
#
# 🍝

ci_token = os.getenv('CI')
if not ci_token:
    init_cfg = Configuration()
    if init_cfg.dsc.bot:
        client_class = discord.AutoShardedClient
    else:
        client_class = discord.Client
else:
    client_class = discord.AutoShardedClient


class ApexSigma(client_class):
    """
    The core client class of the Apex Framework.
    """

    __slots__ = (
        "ready", "db", "log", "cache", "music", "modules",
        "cool_down", "cfg", "queue", "shard_count", "shard_ids",
        "loop", "start_time", "message_count", "command_count",
        "gateway_start", "gateway_finish"
    )

    def __init__(self):
        super().__init__(status=discord.Status.dnd, activity=discord.Game('booting...'))
        self.ready = False
        # State attributes before initialization.
        self.db = None
        self.log = None
        self.cache = None
        self.music = None
        self.modules = None
        self.cool_down = None
        self.cfg = init_cfg
        self._connection.max_messages = self.cfg.dsc.max_messages
        self.queue = ExecutionClockwork(self)
        self.shard_count = self.cfg.dsc.shard_count
        self.shard_ids = [self.cfg.dsc.shard] if self.cfg.dsc.shard is not None else None
        # Initialize startup methods and attributes.
        self.create_cache()
        self.init_logger()
        self.log.info('---------------------------------')
        self.init_config()
        self.log.info('---------------------------------')
        self.loop.run_until_complete(self.init_cacher())
        self.loop.run_until_complete(self.init_database())
        self.log.info('---------------------------------')
        self.init_cool_down()
        self.log.info('---------------------------------')
        self.init_music()
        self.log.info('---------------------------------')
        self.info = Information()
        self.init_modules(init=True)
        self.start_time = arrow.utcnow()
        self.message_count = 0
        self.command_count = 0
        self.gateway_start = 0
        self.gateway_finish = 0
        self.loop.run_until_complete(self.on_boot())
        self.log.info('---------------------------------')

    @staticmethod
    def create_cache():
        """
        Initializes the static cache folder.
        Mostly, if not only, used for music file caching.
        :return:
        """
        if os.path.exists('cache'):
            shutil.rmtree('cache')
        os.makedirs('cache')

    async def init_cacher(self):
        """
        Initializes the core client Cacher.
        :return:
        """
        try:
            self.cache = await get_cache(self.cfg.cache)
        except OSError:
            self.log.error('Cacher failed to initialize, if you are using Redis, make sure the server is running!')
            exit(errno.ETIMEDOUT)

    def init_logger(self):
        """
        Initializes the core client Logger.
        :return:
        """
        self.log = create_logger('Sigma', shard=init_cfg.dsc.shard)
        self.log.info('Logger Created')

    def init_config(self):
        """
        Reads the configuration files and adds them to the core client.
        :return:
        """
        self.log.info('Loading Configuration...')
        self.log.info(f'Running as a Bot: {self.cfg.dsc.bot}')
        self.log.info(f'Default Bot Prefix: {self.cfg.pref.prefix}')
        self.log.info('Core Configuration Data Loaded')

    async def init_database(self):
        """
        Initializes the database connection to MongoDB.
        Also pre-caches potentially heavy resources from the DB.
        :return:
        """
        self.log.info('Connecting to Database...')
        self.db = Database(self, self.cfg.db)
        try:
            await self.db[self.db.db_nam].collection.find_one({})
            if self.cfg.cache.type not in ['redis', 'mixed']:
                await self.db.precache_settings()
                await self.db.precache_profiles()
                await self.db.precache_resources()
            set_color_cache_coll(self.db[self.db.db_nam].ColorCache)
        except ServerSelectionTimeoutError:
            self.log.error('A Connection To The Database Host Failed!')
            exit(errno.ETIMEDOUT)
        except OperationFailure:
            self.log.error('Database Access Operation Failed!')
            exit(errno.EACCES)
        self.log.info('Successfully Connected to Database')

    def init_cool_down(self):
        """
        Initializes the core client cooldown handler.
        :return:
        """
        self.log.info('Loading Cool-down Controls...')
        self.cool_down = CooldownControl(self)
        self.loop.run_until_complete(self.cool_down.clean_cooldowns())
        self.log.info('Cool-down Controls Successfully Enabled')

    def init_music(self):
        """
        Initializes the music handling core.
        :return:
        """
        self.log.info('Loading Music Controller...')
        self.music = MusicCore(self)
        self.log.info('Music Controller Initialized and Ready')

    def init_modules(self, init=False):
        """
        Loads all modules and within them, commands and events.
        :type init: bool
        :param init: Should the initialized modules be logged.
        :return:
        """
        if init:
            self.log.info('Loading Sigma Modules')
        self.modules = ModuleManager(self, init)

    def is_ready(self):
        """
        Check if the bot is ready.
        If for whatever reason the check fails, it is treated as False.
        :return:
        """
        # noinspection PyBroadException
        try:
            ready = super().is_ready()
        except Exception:
            ready = False
        return ready

    async def get_user(self, uid, cached=False):
        """
        Gets a user from the core client
        or from the cache if one exists in the Cacher class.
        :type uid: int
        :type cached: bool
        :param uid: The User ID of the requested user.
        :param cached: Should the user be cached/obtained from the cache.
        :return:
        """
        cacheable = False
        cache_key = f'get_usr_{uid}'
        if cached and self.cfg.cache.type not in ['mixed', 'redis']:
            cacheable = True
            out = await self.cache.get_cache(cache_key)
            if not out:
                out = super().get_user(uid)
        else:
            out = super().get_user(uid)
        if not out:
            fh = get_fetch_helper(self)
            try:
                out = await fh.fetch_user(uid)
            except Exception:
                out = None
        if out and cacheable:
            await self.cache.set_cache(cache_key, out)
        return out

    async def get_channel(self, cid, cached=False):
        """
        Gets a channel from the core client
        or from the cache if one exists in the Cacher class.
        :type cid: int
        :type cached: bool
        :param cid: The Channel ID of the requested channel.
        :param cached: Should the channel be cached/obtained from the cache.
        :return:
        """
        cacheable = False
        cache_key = f'get_chn_{cid}'
        if cached and self.cfg.cache.type not in ['mixed', 'redis']:
            cacheable = True
            out = await self.cache.get_cache(cache_key)
            if not out:
                out = super().get_channel(cid)
        else:
            out = super().get_channel(cid)
        if not out:
            fh = get_fetch_helper(self)
            try:
                out = await fh.fetch_channel(cid)
            except Exception:
                out = None
        if out and cacheable:
            await self.cache.set_cache(cache_key, out)
        return out

    async def get_guild(self, gid, cached=False):
        """
        Gets a guild from the core client
        or form teh cache if one exists in the Cacher class.
        :param gid: The Guild ID of the requested guild.
        :type gid: int
        :param cached: Should the channel be cached/obtained from the cache.
        :type cached: bool
        :return:
        :rtype:
        """
        cacheable = False
        cache_key = f'get_gld_{gid}'
        if cached and self.cfg.cache.type not in ['mixed', 'redis']:
            cacheable = True
            out = await self.cache.get_cache(cache_key)
            if not out:
                out = super().get_guild(gid)
        else:
            out = super().get_guild(gid)
        if not out:
            fh = get_fetch_helper(self)
            try:
                out = await fh.fetch_guild(gid)
            except Exception:
                out = None
        if out and cacheable:
            await self.cache.set_cache(cache_key, out)
        return out

    def run(self):
        """
        Starts the gateway connection processes.
        :return:
        """
        try:
            self.log.info('Connecting to Discord Gateway...')
            self.gateway_start = arrow.utcnow().float_timestamp
            if self.cfg.dsc.token is not None:
                super().run(self.cfg.dsc.token, bot=self.cfg.dsc.bot)
            else:
                self.log.error('You need to configure the Discord bot token before starting.')
                exit(errno.EPERM)
        except discord.LoginFailure:
            self.log.error('Invalid Token!')
            exit(errno.EPERM)

    async def on_connect(self):
        """
        Starts events when the client connects to the Discord gateway.
        :return:
        """
        self.loop.create_task(self.queue.event_runner('connect'))

    async def on_shard_ready(self, shard_id):
        """
        Starts events when the client connects to a shard, if the client is sharded.
        :type shard_id: int
        :param shard_id: The ID of the shard that the connection was established to.
        :return:
        """
        self.log.info(f'Connection to Discord Shard #{shard_id} Established')
        self.loop.create_task(self.queue.event_runner('shard_ready', ShardReadyPayload(self, shard_id)))

    async def on_ready(self):
        """
        Starts events when the full client connection process is finished.
        :return:
        """
        self.gateway_finish = arrow.utcnow().float_timestamp
        self.log.info(f'Gateway connection established in {round(self.gateway_finish - self.gateway_start, 3)}s')
        self.ready = True
        self.log.info('---------------------------------')
        self.log.info('Apex Sigma Fully Loaded and Ready')
        self.log.info('---------------------------------')
        self.log.info(f'User Account: {self.user.name}#{self.user.discriminator}')
        self.log.info(f'User Snowflake: {self.user.id}')
        self.log.info('---------------------------------')
        self.log.info('Launching On-Ready Modules...')
        self.loop.create_task(self.queue.event_runner('ready'))
        self.log.info('All On-Ready Module Loops Created')
        self.log.info('---------------------------------')

    async def on_boot(self):
        """
        Starts initialization modules that don't require
        an active discord connection to be ran. Such as
        static database initialization data and pre-processing.
        :return:
        :rtype:
        """
        boot_events = self.modules.events.get('boot', [])
        dbinit_events = self.modules.events.get('dbinit', [])
        if boot_events:
            self.log.info('Launching boot events...')
            for boot_event in boot_events:
                await boot_event.execute()
            self.log.info('Boot events executed.')
        if 0 in (self.shard_ids or [0]) and dbinit_events:
            self.log.info('Launching DB-Init events...')
            for dbinit_event in dbinit_events:
                await dbinit_event.execute()
            self.log.info('DB-Init events executed.')

    async def on_message(self, message):
        """
        Starts events whenver a user sends a message.
        :type message: discord.Message
        :param message: The message class of the sent message.
        :return:
        """
        self.message_count += 1
        if not message.author.bot:
            payload = MessagePayload(self, message)
            self.loop.create_task(self.queue.event_runner('message', payload))
            if self.user.mentioned_in(payload.msg):
                self.loop.create_task(self.queue.event_runner('mention', payload))
            await self.queue.command_runner(payload)

    async def on_message_edit(self, before, after):
        """
        Starts events when a message is edited.
        This event triggers only if the message is in the core message cache.
        As the gateway only reports edits by their IDs and not content.
        To catch all edits use the raw event trigger function.
        :type before: discord.Message
        :type after: discord.Message
        :param before: The message as it was before the edit.
        :param after: The message as it is after the edit.
        :return:
        """
        if not after.author.bot:
            self.loop.create_task(self.queue.event_runner('message_edit', MessageEditPayload(self, before, after)))

    async def on_message_delete(self, message):
        """
        Starts events when a message is deleted.
        This event triggers only if the message is in the core message cache.
        As the gateway only reports deletions by their IDs and not content.
        To catch all deletions use the raw event trigger function.
        :type message: discord.Message
        :param message: The message class of the deleted message.
        :return:
        """
        if not message.author.bot:
            self.loop.create_task(self.queue.event_runner('message_delete', MessagePayload(self, message)))

    async def on_member_join(self, member):
        """
        Starts events when a user joins a guild.
        :type member: discord.Member
        :param member: The member that joined.
        :return:
        """
        if not member.bot:
            self.loop.create_task(self.queue.event_runner('member_join', MemberPayload(self, member)))

    async def on_member_remove(self, member):
        """
        Starts events when a user leaves, or is removed from, a guild.
        :type member: discord.Member
        :param member: The member that left.
        :return:
        """
        if not member.bot:
            self.loop.create_task(self.queue.event_runner('member_remove', MemberPayload(self, member)))

    async def on_member_update(self, before, after):
        """
        Starts events when a member is updated.
        This can be various things such as avatar changes,
        playing status message changes, online status changes, etc.
        :type before: discord.Member
        :type after: discord.Member
        :param before: The member before the change.
        :param after: The member after the change.
        :return:
        """
        if not before.bot:
            self.loop.create_task(self.queue.event_runner('member_update', MemberUpdatePayload(self, before, after)))

    async def on_member_ban(self, guild, user):
        """
        Starts events when a member is banned from a guild.
        :type guild: discord.Guild
        :type user: discord.Member or discord.User
        :param guild: The guild on which the member was banned.
        :param user: The user that was banned.
        :return:
        """
        if not user.bot:
            self.loop.create_task(self.queue.event_runner('member_ban', BanPayload(self, guild, user)))

    async def on_member_unban(self, guild, user):
        """
        Starts events when a user is removed from a guild's ban list.
        :type guild: discord.Guild
        :type user: discord.User
        :param guild: The guild from which the user was unbanned.
        :param user: The user that was unbanned.
        :return:
        """
        if not user.bot:
            self.loop.create_task(self.queue.event_runner('member_unban', UnbanPayload(self, guild, user)))

    async def on_guild_join(self, guild):
        """
        Starts events when this client joins a guild.
        :type guild: discord.Guild
        :param guild: The guild that the client joined.
        :return:
        """
        self.loop.create_task(self.queue.event_runner('guild_join', GuildPayload(self, guild)))

    async def on_guild_remove(self, guild):
        """
        Starts events when this client leaves, or is removed from, a guild.
        :type guild: discord.Guild
        :param guild: The guild that the client left.
        :return:
        """
        self.loop.create_task(self.queue.event_runner('guild_remove', GuildPayload(self, guild)))

    async def on_guild_update(self, before, after):
        """
        Starts events when a guild, or a guild settings entry, is updated/changed.
        :type before: discord.Guild
        :type after: discord.Guild
        :param before: The guild as it was before the change.
        :param after: The guild as it is after the change.
        :return:
        """
        self.loop.create_task(self.queue.event_runner('guild_update', GuildUpdatePayload(self, before, after)))

    async def on_voice_state_update(self, member, before, after):
        """
        Starts events when a user changes their voice state.
        Such as connecting, disconnecting and moving between channels.
        :type member: discord.Member
        :type before: discord.VoiceState
        :type after: discord.VoiceState
        :param member: The member that changed their voice state.
        :param before: The member as they were before the change.
        :param after: The member as they are after the change.
        :return:
        """
        if not member.bot:
            payload = VoiceStateUpdatePayload(self, member, before, after)
            self.loop.create_task(self.queue.event_runner('voice_state_update', payload))

    async def on_reaction_add(self, reaction, user):
        """
        Starts events when a user adds an emote reaction to a message.
        This event is triggered only if the message that had a reaction removed is cached.
        :type reaction: discord.Reaction
        :type user: discord.User
        :param reaction: The reaction that was added to the message.
        :param user: The user that added the reaction.
        :return:
        """
        if not user.bot:
            payload = ReactionPayload(self, reaction, user)
            self.loop.create_task(self.queue.event_runner('reaction_add', payload))
            if str(reaction.emoji) in ['⬅', '➡']:
                self.loop.create_task(self.queue.event_runner('paginate', payload))

    async def on_reaction_remove(self, reaction, user):
        """
        Starts events when a user removes an emote reaction from a message.
        This event is triggered only if the message that had a reaction removed is cached.
        :type reaction: discord.Reaction
        :type user: discord.User
        :param reaction: The reaction that was removed from the message.
        :param user: The user that removed the reaction.
        :return:
        """
        if not user.bot:
            payload = ReactionPayload(self, reaction, user)
            self.loop.create_task(self.queue.event_runner('reaction_remove', payload))

    async def on_raw_reaction_add(self, payload):
        """
        Starts events when a user adds an emote reaction to a message regardless of it being cached.
        :type payload: discord.RawReactionActionEvent
        :param payload: The raw reaction addition event payload.
        :return:
        """
        if payload.user_id != payload.channel_id:
            payload = RawReactionPayload(self, payload)
            self.loop.create_task(self.queue.event_runner('raw_reaction_add', payload))
            if str(payload.raw.emoji) in ['⬅', '➡']:
                self.loop.create_task(self.queue.event_runner('raw_paginate', payload))

    async def on_raw_reaction_remove(self, payload):
        """
        Starts events when a user removes an emote reaction from a message regardless of it being cached.
        :type payload: discord.RawReactionActionEvent
        :param payload: The raw reaction removal event payload.
        :return:
        """
        if payload.user_id != payload.channel_id:
            self.loop.create_task(self.queue.event_runner('raw_reaction_remove', RawReactionPayload(self, payload)))
