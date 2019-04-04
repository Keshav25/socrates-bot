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

from sigma.core.mechanics.command import SigmaCommand
from sigma.core.mechanics.payload import CommandPayload


async def dog(_cmd: SigmaCommand, pld: CommandPayload):
    doggie_url = 'https://dog.ceo/api/breeds/image/random'
    async with aiohttp.ClientSession() as session:
        async with session.get(doggie_url) as data:
            doggie_data = await data.read()
            doggie_data = json.loads(doggie_data)
    response = discord.Embed(color=0xf9f9f9, title='🐶 Woof!')
    response.set_image(url=doggie_data.get('message'))
    await pld.msg.channel.send(embed=response)
