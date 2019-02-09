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
import yaml

from sigma.core.mechanics.database import Database
from sigma.modules.moderation.server_settings.filters.edit_name_check import clean_name


class AdoptableHuman(object):
    def __init__(self, parents_only=False, children_only=False):
        self.id = None
        self.name = None
        self.parents = []
        self.children = []
        self.exists = False
        self.parents_only = parents_only
        self.children_only = children_only

    async def new(self, db: Database, user: discord.Member):
        self.id = user.id
        self.name = clean_name(user.name, str(self.id))
        await self.save(db, True)

    async def load(self, db: Database, user_id: int):
        family = await db[db.db_nam].Families.find_one({'user_id': user_id})
        if family:
            self.exists = True
            self.id = user_id
            self.name = clean_name(family.get('user_name'), str(self.id))
            if not self.children_only:
                await self.load_iterable(db, family.get('parents', []), self.parents, True, False)
            if not self.parents_only:
                await self.load_iterable(db, family.get('children', []), self.children, False, True)

    def update_name(self, name: str):
        self.name = clean_name(name, str(self.id))

    @staticmethod
    async def load_iterable(db: Database, iterable: list, appendable: list, p_only: bool, c_only: bool):
        for iter_item in iterable:
            human_object = AdoptableHuman(p_only, c_only)
            await human_object.load(db, iter_item)
            appendable.append(human_object)

    async def save(self, db: Database, new=False):
        data = self.to_dict()
        if new:
            await db[db.db_nam].Families.insert_one(data)
        else:
            await db[db.db_nam].Families.update_one({'user_id': self.id}, {'$set': data})

    def is_parent(self, user_id: int):
        confirmed = False
        if self.id == user_id:
            confirmed = True
        else:
            for parent in self.parents:
                if parent.is_parent(user_id):
                    confirmed = True
                    break
        return confirmed

    def is_child(self, user_id: int):
        confirmed = False
        if self.id == user_id:
            confirmed = True
        else:
            for child in self.children:
                if child.is_child(user_id):
                    confirmed = True
                    break
        return confirmed

    def top_parent(self):
        top = None
        if len(self.parents) == 0:
            top = self
        else:
            for parent in self.parents:
                top = parent.top_parent()
                if top:
                    break
        return top

    def bot_child(self):
        bot = None
        if len(self.children) == 0:
            bot = self
        else:
            for child in self.children:
                bot = child.bot_child()
                if bot:
                    break
        return bot

    def to_tree(self, origin: int):
        name = self.name if self.id != origin else f'> {self.name} <'
        children = [c.to_tree(origin) for c in self.children]
        return {name: children}

    def draw_tree(self, origin: int):
        tree_data = self.to_tree(origin)
        tree_out = yaml.safe_dump(tree_data, default_flow_style=False)
        return tree_out

    def to_dict(self):
        return {
            'user_id': self.id,
            'user_name': self.name,
            'parents': [par.id for par in self.parents],
            'children': [cld.id for cld in self.children]
        }
