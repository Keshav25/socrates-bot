"""
Apex Sigma: The Database Giant Discord Bot.
Copyright (C) 2019  Lucia's Cipher

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import discord

from sigma.core.utilities.generic_responses import GenericResponse


async def lmgtfy(_cmd, pld):
    """
    :param _cmd: The command object referenced in the command.
    :type _cmd: sigma.core.mechanics.command.SigmaCommand
    :param pld: The payload with execution data and details.
    :type pld: sigma.core.mechanics.payload.CommandPayload
    """
    if pld.args:
        lookup = '%20'.join(pld.args)
        google_icon = 'https://maxcdn.icons8.com/Share/icon/Logos/google_logo1600.png'
        query_url = f'http://lmgtfy.com/?q={lookup}'
        response = discord.Embed(color=0xF9F9F9)
        response.set_author(name='Click here to go to the results.', icon_url=google_icon, url=query_url)
    else:
        response = GenericResponse('No search inputted.').error()
    await pld.msg.channel.send(embed=response)
