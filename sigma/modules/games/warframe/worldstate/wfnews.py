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

import arrow
import discord

from sigma.core.mechanics.command import SigmaCommand
from sigma.core.mechanics.payload import CommandPayload
from sigma.core.utilities.generic_responses import error
from sigma.modules.games.warframe.commons.worldstate import WorldState


async def wfnews(_cmd: SigmaCommand, pld: CommandPayload):
    news_list = await WorldState().news
    if news_list:
        news_lines = []
        for news in reversed(news_list):
            en_trans = news.get('translations', {}).get('en')
            if en_trans:
                human_time = arrow.get(news['date']).humanize()
                news_line = f'[{en_trans}]({news["link"]}) - {human_time}'
                news_lines.append(news_line)
        output_text = '\n'.join(news_lines)
        response = discord.Embed(color=0x336699, title='Warframe News', description=output_text)
    else:
        response = error('Could not retrieve News data.')
    await pld.msg.channel.send(embed=response)
