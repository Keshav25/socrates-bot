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
from sigma.core.mechanics.paginator import PaginatorCore


async def blockedarguments(cmd: SigmaCommand, message: discord.Message, args: list):
    blocked_args = await cmd.db.get_guild_settings(message.guild.id, 'blocked_args')
    if not blocked_args:
        response = discord.Embed(color=0x3B88C3, title='ℹ There are no blocked arguments.')
    else:
        total_count = len(blocked_args)
        blocked_args, page = PaginatorCore.paginate(blocked_args, args[0] if args else 1, 20)
        showing_count = len(blocked_args)
        title = f'ℹ Arguments blocked on {message.guild.name}'
        response = discord.Embed(color=0x3B88C3, title=title)
        response.description = ', '.join(blocked_args)
        response.set_footer(text=f'[Page {page}] Total: {total_count} | Showing: {showing_count}')
    await message.channel.send(embed=response)
