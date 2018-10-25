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
from sigma.core.utilities.generic_responses import permission_denied


async def pruneroles(_cmd: SigmaCommand, pld: CommandPayload):
    if message.author.guild_permissions.manage_roles:
        top_role = message.guild.me.top_role.position
        empty_roles = list(filter(lambda r: len(r.members) == 0, message.guild.roles))
        deleted_roles = [await role.delete() for role in empty_roles if role.position < top_role]
        response = discord.Embed(color=0x77B255, title=f'✅ Removed {len(deleted_roles)} roles from this server.')
    else:
        response = permission_denied('Manage Roles')
    await message.channel.send(embed=response)
