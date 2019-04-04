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

import aiohttp
import discord

from sigma.core.utilities.generic_responses import error


async def numberfact(_cmd, pld):
    """
    :param _cmd: The command object referenced in the command.
    :type _cmd: sigma.core.mechanics.command.SigmaCommand
    :param pld: The payload with execution data and details.
    :type pld: sigma.core.mechanics.payload.CommandPayload
    """
    if pld.args:
        lookup = ''.join(pld.args)
        if ':' in lookup:
            num_type = lookup.split(':')[0].lower()
            num_argument = lookup.split(':')[1].lower()
        else:
            num_type = 'trivia'
            num_argument = lookup.lower()
        if '/' in num_argument:
            num_type = 'date'
            mon = num_argument.split('/')[1]
            day = num_argument.split('/')[0]
            num_argument = f'{mon}/{day}'
    else:
        num_type = 'trivia'
        num_argument = 'random'
    num_fact_url = f'http://numbersapi.com/{num_argument}/{num_type}'
    async with aiohttp.ClientSession() as session:
        async with session.get(num_fact_url) as number_get:
            number_response = await number_get.text()
    if not number_response.lower().startswith('cannot'):
        response = discord.Embed(color=0x3B88C3, title='#⃣  Number Fact')
        response.description = number_response
    else:
        response = error('The API couldn\'t process that.')
    await pld.msg.channel.send(embed=response)
