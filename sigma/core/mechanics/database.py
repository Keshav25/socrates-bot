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

import arrow
import discord
from motor import motor_asyncio as motor

from sigma.core.mechanics.caching import Cacher
from sigma.core.mechanics.config import DatabaseConfig


class Database(motor.AsyncIOMotorClient):
    def __init__(self, bot, db_cfg: DatabaseConfig):
        self.bot = bot
        self.db_cfg = db_cfg
        self.db_nam = self.db_cfg.database
        self.cache = Cacher()
        if self.db_cfg.auth:
            self.db_address = f'mongodb://{self.db_cfg.username}:{self.db_cfg.password}'
            self.db_address += f'@{self.db_cfg.host}:{self.db_cfg.port}/'
        else:
            self.db_address = f'mongodb://{self.db_cfg.host}:{self.db_cfg.port}/'
        super().__init__(self.db_address)

    async def get_prefix(self, message: discord.Message):
        prefix = self.bot.cfg.pref.prefix
        if message.guild:
            pfx_search = await self.get_guild_settings(message.guild.id, 'prefix')
            if pfx_search:
                prefix = pfx_search
        return prefix

    async def precache_settings(self):
        self.bot.log.info('Pre-Caching all guild settings...')
        all_settings = await self[self.db_cfg.database].ServerSettings.find({}).to_list(None)
        for setting_file in all_settings:
            guild_id = setting_file.get('server_id')
            if guild_id:
                self.cache.set_cache(guild_id, setting_file)
        self.bot.log.info(f'Finished pre-caching {len(all_settings)} guild settings.')

    async def get_guild_settings(self, guild_id, setting_name):
        guild_settings = self.cache.get_cache(guild_id)
        if guild_settings is None:
            guild_settings = await self[self.bot.cfg.db.database].ServerSettings.find_one({'server_id': guild_id}) or {}
            self.cache.set_cache(guild_id, guild_settings)
        if not guild_settings:
            setting_value = None
        else:
            setting_value = guild_settings.get(setting_name)
        return setting_value

    async def set_guild_settings(self, guild_id, setting_name, value):
        guild_settings = await self[self.bot.cfg.db.database].ServerSettings.find_one({'server_id': guild_id})
        if guild_settings:
            update_target = {"server_id": guild_id}
            update_data = {"$set": {setting_name: value}}
            await self[self.bot.cfg.db.database].ServerSettings.update_one(update_target, update_data)
        else:
            update_data = {'server_id': guild_id, setting_name: value}
            await self[self.bot.cfg.db.database].ServerSettings.insert_one(update_data)
        self.cache.del_cache(guild_id)

    async def get_experience(self, user, guild):
        collection = self[self.bot.cfg.db.database].ExperienceSystem
        entry = await collection.find_one({'user_id': user.id}) or {}
        global_xp = entry.get('global', 0)
        guild_id = str(guild.id)
        guilds = entry.get('guilds', {})
        guild_xp = guilds.get(guild_id, 0)
        total_xp = entry.get('total', 0)
        output = {'global': global_xp, 'guild': guild_xp, 'total': total_xp}
        return output

    async def add_experience(self, user, guild, points, additive=True):
        sabotage_file = await self[self.db_cfg.database].SabotagedUsers.find_one({'user_id': user.id})
        if not sabotage_file:
            collection = self[self.bot.cfg.db.database].ExperienceSystem
            entry = await collection.find_one({'user_id': user.id}) or {}
            if not entry:
                await collection.insert_one({'user_id': user.id})
            total_xp = entry.get('total', 0)
            global_xp = entry.get('global', 0)
            guilds = entry.get('guilds', {})
            guild_id = str(guild.id)
            guild_points = guilds.get(guild_id, 0)
            if additive:
                global_xp += points
                guild_points += points
                total_xp += points
            guild_data = {guild_id: guild_points}
            guilds.update(guild_data)
            xp_data = {'global': global_xp, 'guilds': guilds, 'total': total_xp}
            update_target = {'user_id': user.id}
            update_data = {'$set': xp_data}
            await collection.update_one(update_target, update_data)

    async def get_currency(self, user, guild):
        collection = self[self.bot.cfg.db.database].CurrencySystem
        entry = await collection.find_one({'user_id': user.id}) or {}
        global_amount = entry.get('global', 0)
        current_amount = entry.get('current', 0)
        guild_id = str(guild.id)
        guilds = entry.get('guilds', {})
        guild_amount = guilds.get(guild_id, 0)
        total_amount = entry.get('total', 0)
        output = {'current': current_amount, 'global': global_amount, 'guild': guild_amount, 'total': total_amount}
        return output

    async def add_currency(self, user, guild, points, additive=True):
        sabotage_file = await self[self.db_cfg.database].SabotagedUsers.find_one({'user_id': user.id})
        if not sabotage_file:
            collection = self[self.bot.cfg.db.database].CurrencySystem
            points = abs(points)
            entry = await collection.find_one({'user_id': user.id}) or {}
            if not entry:
                await collection.insert_one({'user_id': user.id})
            current_amount = entry.get('current', 0)
            global_amount = entry.get('global', 0)
            total_amount = entry.get('total', 0)
            guilds = entry.get('guilds', {})
            guild_id = str(guild.id)
            guild_points = guilds.get(guild_id, 0)
            if additive:
                global_amount += points
                guild_points += points
                total_amount += points
            current_amount += points
            guild_data = {guild_id: guild_points}
            guilds.update(guild_data)
            xp_data = {'current': current_amount, 'global': int(global_amount), 'guilds': guilds, 'total': total_amount}
            update_target = {'user_id': user.id}
            update_data = {'$set': xp_data}
            await collection.update_one(update_target, update_data)

    async def rmv_currency(self, user, points):
        collection = self[self.bot.cfg.db.database].CurrencySystem
        points = abs(points)
        entry = await collection.find_one({'user_id': user.id}) or {}
        if not entry:
            await collection.insert_one({'user_id': user.id})
        current_amount = entry.get('current', 0)
        current_amount -= points
        xp_data = {'current': current_amount}
        update_target = {'user_id': user.id}
        update_data = {'$set': xp_data}
        await collection.update_one(update_target, update_data)

    async def get_inventory(self, user):
        inventory = await self[self.db_cfg.database].Inventory.find_one({'user_id': user.id}) or {}
        if not inventory:
            await self[self.db_cfg.database].Inventory.insert_one({'user_id': user.id, 'items': []})
        inventory = inventory.get('items', [])
        return inventory

    async def update_inv(self, user, inv):
        await self[self.db_cfg.database].Inventory.update_one({'user_id': user.id}, {'$set': {'items': inv}})

    async def add_to_inventory(self, user, item_data):
        sabotage_file = await self[self.db_cfg.database].SabotagedUsers.find_one({'user_id': user.id})
        if not sabotage_file:
            stamp = arrow.utcnow().timestamp
            item_data.update({'timestamp': stamp})
            inv = await self.get_inventory(user)
            inv.append(item_data)
            await self.update_inv(user, inv)

    async def del_from_inventory(self, user, item_id):
        inv = await self.get_inventory(user)
        for item in inv:
            if item.get('item_id') == item_id:
                inv.remove(item)
        await self.update_inv(user, inv)

    async def get_inventory_item(self, user, item_file_id):
        inv = await self.get_inventory(user)
        output = None
        for item in inv:
            if item.get('item_file_id').lower() == item_file_id.lower():
                output = item
                break
        return output
