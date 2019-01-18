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
from sigma.core.utilities.generic_responses import error


async def colorme(_cmd: SigmaCommand, pld: CommandPayload):
    if not pld.msg.guild.me.top_role.position <= pld.msg.author.top_role.position:
        enabled = pld.settings.get('color_roles')
        if enabled:
            if pld.args:
                bad_hex = False
                hex_req = pld.args[0].lower().strip('#')
                if len(hex_req) == 3:
                    hex_req = hex_req * 2
                if len(hex_req) != 6:
                    bad_hex = True
                if not bad_hex:
                    role_name = f'SCR-{hex_req.upper()}'
                    role_posi = pld.msg.author.top_role.position + 1
                    role_objc = discord.utils.find(lambda role: role.name == role_name, pld.msg.guild.roles)
                    if not role_objc:
                        color_int = int(f'0x{hex_req}', 16)
                        role_color = discord.Color(color_int)
                        role_objc = await pld.msg.guild.create_role(name=role_name, color=role_color)
                        await role_objc.edit(position=role_posi)
                    for member_role in pld.msg.author.roles:
                        if member_role.name.startswith('SCR-'):
                            await pld.msg.author.remove_roles(member_role, reason='Assigning new color role.')
                    await pld.msg.author.add_roles(role_objc, reason='Assigned color role.')
                    addition_title = f'✅ {role_objc.name} has been added to you, {pld.msg.author.name}.'
                    response = discord.Embed(color=0x77B255, title=addition_title)
                else:
                    response = error('Invalid HEX color code.')
            else:
                response = error('No color HEX provided.')
        else:
            response = discord.Embed(color=0xBE1931, title='⛔ Color roles are not enabled.')
    else:
        response = error('I can\'t make a color role with my current role position.')
    await pld.msg.channel.send(embed=response)
