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
from sigma.core.mechanics.payload import CommandPayload
from sigma.core.utilities.generic_responses import permission_denied


async def unflip(cmd: SigmaCommand, pld: CommandPayload):
    message = pld.msg
    if message.author.permissions_in(message.channel).manage_guild:
        flip_settings = await cmd.db.get_guild_settings(message.guild.id, 'unflip')
        if flip_settings is None:
            unflip_set = False
        else:
            unflip_set = flip_settings
        if unflip_set:
            await cmd.db.set_guild_settings(message.guild.id, 'unflip', False)
            ending = 'disabled'
        else:
            await cmd.db.set_guild_settings(message.guild.id, 'unflip', True)
            ending = 'enabled'
        response = discord.Embed(color=0x77B255, title=f'✅ Table unflipping has been {ending}')
    else:
        response = permission_denied('Manage Server')
    await message.channel.send(embed=response)
