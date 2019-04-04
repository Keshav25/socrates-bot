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

import secrets

import discord

from sigma.modules.searches.safebooru.mech.safe_core import generate_embed, grab_post_list

links = []
embed_titles = ['Fluffy tails are supreme!', 'Touch fluffy tail~', '>:3',
                '乀^｀・´^／', '(ミ`ω´ミ)', '◝(´◝ω◜｀)◜']


async def kitsunemimi(cmd, pld):
    """
    :param cmd: The command object referenced in the command.
    :type cmd: sigma.core.mechanics.command.SigmaCommand
    :param pld: The payload with execution data and details.
    :type pld: sigma.core.mechanics.payload.CommandPayload
    """
    global links
    if not links:
        name = cmd.bot.user.name
        filler_message = discord.Embed(color=0xff3300, title=f'🦊 One moment, filling {name} with foxes...')
        fill_notify = await pld.msg.channel.send(embed=filler_message)
        links = await grab_post_list('fox_tail')
        filler_done = discord.Embed(color=0xff3300, title=f'🦊 We added {len(links)} foxes!')
        await fill_notify.edit(embed=filler_done)
    rand_pop = secrets.randbelow(len(links))
    post_choice = links.pop(rand_pop)
    icon = 'https://i.imgur.com/g0wv2Pf.jpg'
    response = generate_embed(post_choice, embed_titles, 0xff3300, icon=icon)
    await pld.msg.channel.send(embed=response)
