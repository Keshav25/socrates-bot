﻿# Apex Sigma: The Database Giant Discord Bot.
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

import json

import aiohttp
import discord

from sigma.core.mechanics.command import SigmaCommand

osu_logo = 'http://w.ppy.sh/c/c9/Logo.png'

user_data_cache = {}


async def find_user_data(profile_url: str):
    data_cache = user_data_cache.get(profile_url)
    if not data_cache:
        async with aiohttp.ClientSession() as session:
            async with session.get(profile_url) as data:
                page = await data.text()
        lines = [x.strip() for x in page.split('\n')]
        lines.reverse()
        user_data = {}
        for line in lines:
            if line.startswith('{"id":'):
                try:
                    user_data = json.loads(line)
                    break
                except json.JSONDecodeError:
                    pass
        user_data_cache.update({profile_url: user_data})
    else:
        user_data = data_cache
    return user_data


async def osu(_cmd: SigmaCommand, pld: CommandPayload):
    if args:
        osu_input = '%20'.join(args)
        profile_url = f'https://osu.ppy.sh/users/{osu_input.lower()}'
        user_data = await find_user_data(profile_url)
        username = user_data.get('username')
        if username:
            user_color = str(message.author.color)[1:]
            sig_url = f'https://lemmmy.pw/osusig/sig.php?colour=hex{user_color}&uname={osu_input}'
            response = discord.Embed(color=message.author.color)
            response.set_image(url=sig_url)
            response.set_author(name=f'{username}\'s osu! Profile', url=profile_url, icon_url=osu_logo)
        else:
            response = discord.Embed(color=0xBE1931, title='❗ Unable to retrieve profile.')
    else:
        response = discord.Embed(color=0xBE1931, title='❗ Nothing inputted.')
    await message.channel.send(embed=response)
