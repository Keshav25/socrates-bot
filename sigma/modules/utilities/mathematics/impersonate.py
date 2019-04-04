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

import functools
from concurrent.futures import ThreadPoolExecutor

import discord
import markovify

from sigma.core.mechanics.command import SigmaCommand
from sigma.core.mechanics.payload import CommandPayload
from sigma.core.utilities.data_processing import user_avatar
from sigma.core.utilities.generic_responses import error


async def impersonate(cmd, pld):
    """
    :param cmd: The command object referenced in the command.
    :type cmd: sigma.core.mechanics.command.SigmaCommand
    :param pld: The payload with execution data and details.
    :type pld: sigma.core.mechanics.payload.CommandPayload
    """
    if pld.args:
        if pld.msg.mentions:
            target = pld.msg.mentions[0]
        else:
            target = discord.utils.find(lambda x: x.name.lower() == ' '.join(pld.args).lower(), pld.msg.guild.members)
    else:
        target = pld.msg.author
    if target:
        chain_data = await cmd.db[cmd.db.db_nam].MarkovChains.find_one({'user_id': target.id})
        if chain_data:
            if chain_data['chain']:
                total_string = ' '.join(chain_data['chain'])
                chain_function = functools.partial(markovify.Text, total_string)
                with ThreadPoolExecutor() as threads:
                    try:
                        cache_key = f'chain_{target.id}'
                        chain = await cmd.db.cache.get_cache(cache_key)
                        if not chain:
                            chain = await cmd.bot.loop.run_in_executor(threads, chain_function)
                            await cmd.db.cache.set_cache(cache_key, chain)
                        sentence_function = functools.partial(chain.make_short_sentence, 500)
                        sentence = await cmd.bot.loop.run_in_executor(threads, sentence_function)
                    except KeyError:
                        sentence = None
                if not sentence:
                    not_enough_data = '😖 I could not think of anything... I need more chain items!'
                    response = discord.Embed(color=0xBE1931, title=not_enough_data)
                else:
                    response = discord.Embed(color=0xbdddf4)
                    response.set_author(name=target.name, icon_url=user_avatar(target))
                    response.add_field(name='💭 Hmm... something like...', value=sentence)
            else:
                response = error(f'{target.name}\'s chain has no data.')
        else:
            response = discord.Embed(color=0x696969)
            prefix = cmd.db.get_prefix(pld.settings)
            title = f'🔍 Chain Data Not Found For {target.name}'
            value = f'You can make one with `{prefix}collectchain @{target.name} #channel`!'
            response.add_field(name=title, value=value)
    else:
        response = error('No user targeted.')
    await pld.msg.channel.send(embed=response)
