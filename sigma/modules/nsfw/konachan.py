﻿"""
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
import secrets

import aiohttp
import discord

from sigma.core.utilities.generic_responses import not_found, error


async def konachan(_cmd, pld):
    """
    :param _cmd: The command object referenced in the command.
    :type _cmd: sigma.core.mechanics.command.SigmaCommand
    :param pld: The payload with execution data and details.
    :type pld: sigma.core.mechanics.payload.CommandPayload
    """
    url = 'https://konachan.com/post.json?limit=100&tags='
    url += '+'.join(pld.args) if pld.args else 'nude'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as data:
            data = await data.read()
            try:
                data = json.loads(data)
                failed = False
            except json.JSONDecodeError:
                data = []
                failed = True
    if data and not failed:
        post = secrets.choice(data)
        post_url = f'http://konachan.com/post/show/{post["id"]}'
        icon_url = 'https://i.imgur.com/qc4awFL.png'
        response = discord.Embed(color=0x473a47)
        response.set_author(name='Konachan', url=post_url, icon_url=icon_url)
        response.set_image(url=post["file_url"])
        response.set_footer(
            text=f'Score: {post["score"]} | Size: {post["width"]}x{post["height"]} | Uploaded By: {post["author"]}')
    else:
        if failed:
            response = error('Failed to parse Konachan\'s data...')
        else:
            response = not_found('No results.')
    await pld.msg.channel.send(embed=response)
