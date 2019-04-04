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

from urllib.parse import quote as escape

import aiohttp
import discord
import lxml.html as lx

from sigma.core.mechanics.command import SigmaCommand
from sigma.core.mechanics.payload import CommandPayload
from sigma.core.utilities.generic_responses import error, not_found
from sigma.modules.minigames.quiz.mathgame import ongoing_list as math_chs

wolfram_icon = 'https://i.imgur.com/sGKq1A6.png'
wolfram_url = 'http://www.wolframalpha.com/input/?i='
api_url = 'http://api.wolframalpha.com/v2/query?format=plaintext&podindex=2&input='


async def get_url_body(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as data:
            data = await data.read()
    return data


async def get_results(query_url: str):
    results = ''
    if query_url:
        query_page_xml = await get_url_body(query_url)
        if query_page_xml:
            query_page = lx.fromstring(query_page_xml)
            pods = query_page.getchildren()
            for pod in pods:
                if 'title' in pod.keys():
                    pod_data = []
                    subpods = pod.getchildren()
                    for subpod in subpods:
                        for element in subpod.getiterator():
                            if element.tag == 'plaintext':
                                if element.text:
                                    pod_data.append(element.text)
                    results += '\n\n'.join(pod_data)
    return results


def make_safe_query(query: list):
    safe = r'`~!@$^*()[]{}\|:;"\'<>,.'
    query_list = list(' '.join(query))
    safe_query = ''
    while query_list:
        char = query_list.pop(0).lower()
        safe_query += escape(char, safe=safe)
    return safe_query


async def send_response(message: discord.Message, init: discord.Message or None, response: discord.Embed):
    await init.edit(embed=response) if init else await message.channel.send(embed=response)


async def wolframalpha(cmd: SigmaCommand, pld: CommandPayload):
    init_message = None
    if cmd.cfg.app_id:
        if pld.msg.channel.id not in math_chs:
            if pld.args:
                query = make_safe_query(pld.args)
                url = f'{api_url}{query}&appid={cmd.cfg.app_id}'
                init_response = discord.Embed(color=0xff7e00)
                init_response.set_author(name='Processing request...', icon_url=wolfram_icon)
                init_message = await pld.msg.channel.send(embed=init_response)
                results = await get_results(url)
                if results:
                    if len(results) <= 2000:
                        response = discord.Embed(color=0xff7e00, description=f'```\n{results}\n```')
                        response.set_author(name='Wolfram Alpha', icon_url=wolfram_icon, url=wolfram_url + query)
                        response.set_footer(text='View the full results by clicking the embed title.')
                    else:
                        response = error('Results too long to display.')
                        response.description = f'You can view them directly [here]({wolfram_url + query}).'
                else:
                    response = not_found('No results.')
            else:
                response = error('Nothing inputted.')
        else:
            response = error('Wolfram can\'t be used during an ongoing math game.')
    else:
        response = error('The API Key is missing.')
    await send_response(pld.msg, init_message, response)
