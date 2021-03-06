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

import json

import aiohttp
import discord


async def dogfact(_cmd, pld):
    """
    :param _cmd: The command object referenced in the command.
    :type _cmd: sigma.core.mechanics.command.SigmaCommand
    :param pld: The payload with execution data and details.
    :type pld: sigma.core.mechanics.payload.CommandPayload
    """
    api_url = 'https://dog-api.kinduff.com/api/facts'
    async with aiohttp.ClientSession() as session:
        async with session.get(api_url) as data:
            data = await data.read()
            data = json.loads(data)
    fact = data.get('facts')[0]
    response = discord.Embed(color=0xccd6dd)
    response.add_field(name='🐶 Did you know...', value=fact)
    await pld.msg.channel.send(embed=response)
