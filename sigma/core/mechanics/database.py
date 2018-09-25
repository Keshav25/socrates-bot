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
from sigma.core.mechanics.resources import SigmaResource


class Database(motor.AsyncIOMotorClient):
    def __init__(self, bot, db_cfg: DatabaseConfig):
        self.bot = bot
        self.db_cfg = db_cfg
        self.db_nam = self.db_cfg.database
        self.cache = Cacher(600)
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

    # Document Pre-Cachers

    async def precache_settings(self):
        self.bot.log.info('Pre-Caching all guild settings...')
        all_settings = await self[self.db_cfg.database].ServerSettings.find({}).to_list(None)
        for setting_file in all_settings:
            guild_id = setting_file.get('server_id')
            if guild_id:
                self.cache.set_cache(guild_id, setting_file)
        self.bot.log.info(f'Finished pre-caching {len(all_settings)} guild settings.')

    async def precache_profiles(self):
        self.bot.log.info('Pre-Caching all member profiles...')
        all_settings = await self[self.db_cfg.database].Profiles.find({}).to_list(None)
        for setting_file in all_settings:
            guild_id = setting_file.get('user_id')
            if guild_id:
                self.cache.set_cache(guild_id, setting_file)
        self.bot.log.info(f'Finished pre-caching {len(all_settings)} member profiles.')

    # Guild Setting Variable Calls

    async def get_guild_settings(self, guild_id: int, setting_name: str):
        guild_settings = self.cache.get_cache(guild_id)
        if guild_settings is None:
            guild_settings = await self[self.db_nam].ServerSettings.find_one({'server_id': guild_id}) or {}
            self.cache.set_cache(guild_id, guild_settings)
        setting_value = guild_settings.get(setting_name)
        return setting_value

    async def set_guild_settings(self, guild_id: int, setting_name: str, value):
        guild_settings = await self[self.db_nam].ServerSettings.find_one({'server_id': guild_id})
        if guild_settings:
            update_target = {"server_id": guild_id}
            update_data = {"$set": {setting_name: value}}
            await self[self.db_nam].ServerSettings.update_one(update_target, update_data)
        else:
            update_data = {'server_id': guild_id, setting_name: value}
            await self[self.db_nam].ServerSettings.insert_one(update_data)
        self.cache.del_cache(guild_id)

    # Profile Data Entry Variable Calls

    async def get_profile(self, user_id: int, entry_name: str):
        user_profile = self.cache.get_cache(user_id)
        if user_profile is None:
            user_profile = await self[self.db_nam].Profiles.find_one({'user_id': user_id}) or {}
            self.cache.set_cache(user_id, user_profile)
        entry_value = user_profile.get(entry_name)
        return entry_value

    async def set_profile(self, user_id: int, entry_name: str, value):
        user_profile = await self[self.db_nam].Profiles.find_one({'user_id': user_id}) or {}
        if user_profile:
            update_target = {"user_id": user_id}
            update_data = {"$set": {entry_name: value}}
            await self[self.db_nam].Profiles.update_one(update_target, update_data)
        else:
            update_data = {'user_id': user_id, entry_name: value}
            await self[self.db_nam].Profiles.insert_one(update_data)
        self.cache.del_cache(user_id)

    async def is_sabotaged(self, user_id: int):
        return bool(await self.get_profile(user_id, 'sabotaged'))

    # Resource Handling

    async def update_resource(self, resource: SigmaResource, user_id: int, resource_name: str):
        cache_key = f'res_{resource_name}_{user_id}'
        resources = await self[self.db_nam][f'{resource_name.title()}Resource'].find_one({'user_id': user_id})
        coll = self[self.db_nam][f'{resource_name.title()}Resource']
        data = resource.dictify()
        if resources:
            await coll.update_one({'user_id': user_id}, {'$set': data})
        else:
            data.update({'user_id': user_id})
            await coll.insert_one(data)
        self.cache.del_cache(cache_key)

    async def get_resource(self, user_id: int, resource_name: str):
        cache_key = f'res_{resource_name}_{user_id}'
        resource = self.cache.get_cache(cache_key)
        if not resource:
            data = await self[self.db_nam][f'{resource_name.title()}Resource'].find_one({'user_id': user_id}) or {}
            resource = SigmaResource(data)
            self.cache.set_cache(cache_key, resource)
        return resource

    async def add_resource(self, user_id: int, name: str, amount: int, trigger: str, origin=None, ranked: bool=True):
        if not await self.is_sabotaged(user_id):
            amount = abs(int(amount))
            resource = await self.get_resource(user_id, name)
            resource.add_value(amount, trigger, origin, ranked)
            await self.update_resource(resource, user_id, name)

    async def del_resource(self, user_id: int, name: str, amount: int, trigger: str, origin=None):
        amount = abs(int(amount))
        resource = await self.get_resource(user_id, name)
        resource.del_value(amount, trigger, origin)
        await self.update_resource(resource, user_id, name)

    # Inventory Handling

    async def update_inventory(self, user_id: int, inventory: list):
        cache_key = f'inv_{user_id}'
        inv = await self[self.db_nam].Inventory.find_one({'user_id': user_id})
        data = {'items': inventory}
        if inv:
            await self[self.db_nam].Inventory.update_one({'user_id': user_id}, {'$set': data})
        else:
            data.update({'user_id': user_id})
            await self[self.db_nam].Inventory.insert_one(data)
        self.cache.del_cache(cache_key)

    async def get_inventory(self, user_id: int):
        cache_key = f'inv_{user_id}'
        inventory = self.cache.get_cache(cache_key)
        if not inventory:
            inventory = await self[self.db_nam].Inventory.find_one({'user_id': user_id}) or {}
            self.cache.set_cache(cache_key, inventory)
        inventory = inventory.get('items', [])
        return inventory

    async def add_to_inventory(self, user_id: int, item_data: dict):
        stamp = arrow.utcnow().timestamp
        item_data.update({'timestamp': stamp})
        inv = await self.get_inventory(user_id)
        inv.append(item_data)
        await self.update_inventory(user_id, inv)

    async def del_from_inventory(self, user_id: int, item_id: str):
        inv = await self.get_inventory(user_id)
        for item in inv:
            if item.get('item_id') == item_id:
                inv.remove(item)
        await self.update_inventory(user_id, inv)

    async def get_inventory_item(self, user_id: int, item_file_id: str):
        inv = await self.get_inventory(user_id)
        output = None
        for item in inv:
            if item.get('item_file_id').lower() == item_file_id.lower():
                output = item
                break
        return output
