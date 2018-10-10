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

from sigma.core.mechanics.command import SigmaCommand
from sigma.core.utilities.data_processing import paginate


async def viewlists(cmd: SigmaCommand, message: discord.Message, args: list):
    lookup_data = {'server_id': message.guild.id}
    list_coll = cmd.db[cmd.db.db_nam].CustomLists
    list_files = await list_coll.find(lookup_data).to_list(None)
    if list_files:
        list_lines = []
        for list_file in list_files:
            author_id = list_file.get('user_id')
            author = cmd.bot.get_user(author_id)
            creator = f'{author.name}#{author.discriminator}' if author else author_id
            pv = '⛔' if list_file.get('private') else ''
            lk = '🔏' if list_file.get('locked') else ''
            attributes = f'`{pv}{lk}`' if pv or lk else ''
            list_line = f'`{list_file.get("list_id")}` - {creator} {attributes}'
            list_lines.append(list_line)
        page = args[0] if args else 1
        list_lines, page = paginate(list_lines, page)
        response = discord.Embed(color=0xF9F9F9, title=f':books: Custom Lists | Page {page}')
        list_list = '\n'.join(list_lines)
        response.description = list_list
    else:
        response = discord.Embed(color=0x696969, title='🔍 There are no lists on this server.')
    await message.channel.send(embed=response)
