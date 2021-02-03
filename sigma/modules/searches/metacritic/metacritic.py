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

import asyncio

import discord

from sigma.core.utilities.generic_responses import GenericResponse
from sigma.modules.searches.metacritic.mech.core import MetaCriticGame, MetaCriticMusic
from sigma.modules.searches.metacritic.mech.core import MetaCriticMovie, MetaCriticSearch


async def metacritic(cmd, pld):
    """
    :param cmd: The command object referenced in the command.
    :type cmd: sigma.core.mechanics.command.SigmaCommand
    :param pld: The payload with execution data and details.
    :type pld: sigma.core.mechanics.payload.CommandPayload
    """
    results_msg = None
    if pld.args:
        query_str = ' '.join(pld.args).lower()
        if '/' in query_str:
            category, _, title = query_str.partition('/')
            if category == 'search':
                mc = MetaCriticSearch(cmd)
                search_filter = 'all'
                if '/' in title:
                    search_filter, _, title = title.partition('/')
                if search_filter in ['game', 'movie', 'tv', 'music', 'all']:
                    if search_filter == 'music':
                        search_filter = 'album'
                    await mc.set_response_data(category, search_filter, title)
                    if mc.valid_response:
                        response = mc.generate_embed(search_filter)
                        results_msg = await pld.msg.channel.send(embed=response)

                        def check_answer(msg):
                            """
                            Checks if the answer message is valid.
                            :param msg: The message to check.
                            :type msg: discord.Message
                            :return:
                            :rtype: bool
                            """
                            same_channel = pld.msg.channel.id == msg.channel.id
                            same_author = pld.msg.author.id == msg.author.id
                            if same_channel and same_author:
                                if msg.content.isdigit():
                                    num = abs(int(msg.content))
                                    if num <= mc.results_len:
                                        valid = True
                                    else:
                                        valid = False
                                else:
                                    valid = False
                            else:
                                valid = False
                            return valid

                        try:
                            answer_message = await cmd.bot.wait_for('message', check=check_answer, timeout=30)
                            result = mc.result_map[answer_message.content]
                            category, _, title = result.partition('/')
                        except asyncio.TimeoutError:
                            return
                    else:
                        response = GenericResponse(f'No results for {title}.').not_found()
                        await pld.msg.channel.send(embed=response)
                        return
                else:
                    response = GenericResponse('Invalid search filter.').error()
                    await pld.msg.channel.send(embed=response)
                    return
            if category in ['game', 'movie', 'tv', 'music']:
                if category == 'game':
                    mc = MetaCriticGame(cmd)
                    platform, _, title = title.partition('/')
                    platform = mc.get_platform(platform)
                    if platform:
                        await mc.set_response_data(category, platform, title)
                        if mc.valid_response:
                            response = mc.generate_embed()
                        else:
                            response = GenericResponse('Game not found.').not_found()
                    else:
                        response = GenericResponse('Invalid game platform.').error()
                elif category == 'movie':
                    mc = MetaCriticMovie(cmd)
                    await mc.set_response_data(category, title)
                    if mc.valid_response:
                        response = mc.generate_embed()
                    else:
                        response = GenericResponse('Movie not found.').not_found()
                elif category == 'tv':
                    mc = MetaCriticMovie(cmd)
                    season = ''
                    if '/' in title:
                        title, _, season = title.partition('/')
                    await mc.set_response_data(category, title, season)
                    if mc.valid_response:
                        response = mc.generate_embed()
                    else:
                        response = GenericResponse('TV Show not found.').not_found()
                else:
                    mc = MetaCriticMusic(cmd)
                    album, _, artist = title.partition('/')
                    await mc.set_response_data(category, album, artist)
                    if mc.valid_response:
                        response = mc.generate_embed()
                    else:
                        response = GenericResponse('Album not found.').not_found()
            else:
                response = GenericResponse('Invalid category.').error()
        else:
            response = GenericResponse('Separate fields with forward slashes.').error()
    else:
        response = GenericResponse('Nothing inputted.').error()
    if results_msg:
        try:
            await results_msg.edit(embed=response)
        except discord.NotFound:
            await pld.msg.channel.send(embed=response)
    else:
        await pld.msg.channel.send(embed=response)
