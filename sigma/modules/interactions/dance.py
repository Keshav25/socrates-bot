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
from sigma.core.mechanics.payload import CommandPayload
from sigma.modules.interactions.mech.interaction_mechanics import grab_interaction, get_target, make_footer


async def dance(cmd: SigmaCommand, pld: CommandPayload):
    interaction = await grab_interaction(cmd.db, 'dance')
    target = get_target(pld.msg)
    auth = pld.msg.author
    icons = ['💃', '🕺']
    icon = secrets.choice(icons)
    if not target or target.id == pld.msg.author.id:
        response = discord.Embed(color=0xdd2e44, title=f'{icon} {auth.display_name} dances.')
    else:
        response = discord.Embed(color=0xdd2e44, title=f'{icon} {auth.display_name} dances with {target.display_name}.')
    response.set_image(url=interaction['url'])
    response.set_footer(text=await make_footer(cmd, interaction))
    await pld.msg.channel.send(embed=response)
