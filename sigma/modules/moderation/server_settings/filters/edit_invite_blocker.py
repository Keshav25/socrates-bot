# Apex Sigma: The Database Giant Discord Bot.
# Copyright (C) 2018  Lucia's Cipher
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import discord

from sigma.core.mechanics.event import SigmaEvent
from sigma.core.mechanics.permissions import FilterPermissions
from sigma.core.utilities.data_processing import user_avatar
from sigma.core.utilities.event_logging import log_event
from sigma.modules.moderation.warning.issuewarning import warning_data


async def edit_invite_blocker(ev: SigmaEvent, _before: discord.Message, after: discord.Message):
    if after.guild:
        if isinstance(after.author, discord.Member):
            filter_perms = FilterPermissions(ev, after)
            override = await filter_perms.check_perms('invites')
            is_owner = after.author.id in ev.bot.cfg.dsc.owners
            if not any([after.author.permissions_in(after.channel).administrator, is_owner, override]):
                active = await ev.db.get_guild_settings(after.guild.id, 'block_invites')
                if active:
                    arguments = after.content.split(' ')
                    invite_found = False
                    for arg in arguments:
                        triggers = ['discord.gg', 'discordapp.com/invite']
                        for trigger in triggers:
                            if trigger in arg:
                                try:
                                    code = arg.split('/')[-1]
                                    invite_found = await ev.bot.get_invite(code)
                                    break
                                except (discord.NotFound, IndexError):
                                    pass
                    if invite_found:
                        try:
                            invite_warn = await ev.db.get_guild_settings(after.guild.id, 'invite_auto_warn')
                            if invite_warn:
                                reason = f'Sent an invite to {invite_found.guild.name}.'
                                warn_data = warning_data(after.guild.me, after.author, reason)
                                await ev.db[ev.db.db_nam].Warnings.insert_one(warn_data)
                            await after.delete()
                            title = f'⛓ Invite links are not allowed on {after.guild.name}.'
                            response = discord.Embed(color=0xF9F9F9, title=title)
                            try:
                                await after.author.send(embed=response)
                            except discord.Forbidden:
                                pass
                            log_embed = discord.Embed(color=0xF9F9F9)
                            author = f'{after.author.name}#{after.author.discriminator}'
                            log_embed.set_author(name=f'I removed {author}\'s invite link.',
                                                 icon_url=user_avatar(after.author))
                            log_embed.set_footer(
                                text=f'Posted In: #{after.channel.name} | Leads To: {invite_found.guild.name}')
                            await log_event(ev.bot, after.guild, ev.db, log_embed, 'log_filters')
                        except (discord.ClientException, discord.NotFound, discord.Forbidden):
                            pass
