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

import functools
import secrets
from concurrent.futures import ThreadPoolExecutor

import discord
import markovify

from sigma.core.utilities.data_processing import user_avatar
from sigma.core.utilities.generic_responses import error
from sigma.modules.utilities.mathematics.collector_clockwork import deserialize


def shuffle(items):
    new = []
    copy = [i for i in items]
    while len(copy) > 0:
        new.append(copy.pop(secrets.randbelow(len(copy))))
    return new


def combine_names(users):
    """

    :param users:
    :type users: list
    :return:
    :rtype:
    """
    pieces = []
    users = shuffle(users)
    total_length = sum([len(u.name) for u in users])
    usable_length = total_length // len(users)
    needed_length = usable_length // len(users)
    for user in users:
        piece = user.name[needed_length * len(pieces):needed_length * (len(pieces) + 1)]
        pieces.append(piece)
    return ''.join(pieces)


async def combinechains(cmd, pld):
    """
    :param cmd: The command object referenced in the command.
    :type cmd: sigma.core.mechanics.command.SigmaCommand
    :param pld: The payload with execution data and details.
    :type pld: sigma.core.mechanics.payload.CommandPayload
    """
    if len(pld.msg.mentions) >= 2:
        empty_chain = None
        chains = []
        chain_dicts = []
        with ThreadPoolExecutor() as threads:
            for target in pld.msg.mentions:
                target_chain = await cmd.db[cmd.db.db_nam].MarkovChains.find_one({'user_id': target.id})
                if not target_chain:
                    empty_chain = target
                    break
                chain_dicts.append(deserialize(target_chain.get("chain")))
            failed = False
            for chain_dict in chain_dicts:
                try:
                    chain_task = functools.partial(markovify.Text.from_dict, chain_dict)
                    chain = await cmd.bot.loop.run_in_executor(threads, chain_task)
                    chains.append(chain)
                except (ValueError, KeyError, AttributeError):
                    failed = True
            if not empty_chain:
                if not failed:
                    await cmd.bot.cool_down.set_cooldown(cmd.name, pld.msg.author, 20)
                    try:
                        combine_task = functools.partial(markovify.combine, chains)
                        combination = await cmd.bot.loop.run_in_executor(threads, combine_task)
                        sentence_function = functools.partial(combination.make_short_sentence, 500)
                        sentence = await cmd.bot.loop.run_in_executor(threads, sentence_function)
                    except (ValueError, KeyError, AttributeError):
                        sentence = None
                    if not sentence:
                        not_enough_data = '😖 I could not think of anything... I need more chain items!'
                        response = discord.Embed(color=0xBE1931, title=not_enough_data)
                    else:
                        combined_name = combine_names(pld.msg.mentions)
                        response = discord.Embed(color=0xbdddf4)
                        response.set_author(name=combined_name, icon_url=user_avatar(secrets.choice(pld.msg.mentions)))
                        response.add_field(name='💭 Hmm... something like...', value=sentence)
                else:
                    response = error('Failed to combine the markov chains.')
            else:
                response = error(f'{empty_chain.name} does not have a chain.')
    else:
        response = error('Invalid number of targets.')
    await pld.msg.channel.send(embed=response)
