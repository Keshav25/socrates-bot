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

import secrets

import discord

from sigma.core.mechanics.command import SigmaCommand


def settings(lookup: str):
    mode = None
    if lookup in ['private', 'locked']:
        mode = lookup
    return mode


async def makelist(cmd: SigmaCommand, message: discord.Message, args: list):
    mode = None
    if args:
        mode = settings(args[0].lower())
    list_data = {
        'server_id': message.guild.id,
        'user_id': message.author.id,
        'list_id': secrets.token_hex(2),
        'mode': mode,
        'name': f'{message.author.name}\'s List',
        'contents': []
    }
    await cmd.db[cmd.db.db_nam].CustomLists.insert_one(list_data)
    response = discord.Embed(color=0x77B255)
    response.title = f'✅ List `{list_data.get("list_id")}` has been created.'
    response.set_footer(text=f'You can rename it with {cmd.bot.cfg.pref.prefix}renamelist.')
    await message.channel.send(embed=response)
