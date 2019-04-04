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
import secrets

import discord

from sigma.core.mechanics.command import SigmaCommand
from sigma.core.mechanics.payload import CommandPayload
from sigma.core.utilities.generic_responses import error
from sigma.modules.minigames.quiz.mech.utils import scramble

ongoing_list = []
word_cache = {}


async def unscramblegame(cmd: SigmaCommand, pld: CommandPayload):
    if not word_cache:
        dict_docs = await cmd.db[cmd.db.db_nam].DictionaryData.find({}).to_list(None)
        for ddoc in dict_docs:
            word = ddoc.get('word')
            if len(word) > 3 and len(word.split(' ')) == 1:
                word_cache.update({word: ddoc.get('description')})
    if pld.msg.channel.id not in ongoing_list:
        ongoing_list.append(pld.msg.channel.id)
        words = list(word_cache.keys())
        word_choice = secrets.choice(words)
        word_description = word_cache.get(word_choice)
        kud_reward = len(word_choice)
        scrambled = scramble(word_choice.title())
        question_embed = discord.Embed(color=0x3B88C3, title=f'🔣 {scrambled}')
        await pld.msg.channel.send(embed=question_embed)

        def check_answer(msg):
            if pld.msg.channel.id == msg.channel.id:
                if msg.content.lower() == word_choice.lower():
                    correct = True
                else:
                    correct = False
            else:
                correct = False
            return correct

        try:
            answer_message = await cmd.bot.wait_for('message', check=check_answer, timeout=30)
            await cmd.db.add_resource(answer_message.author.id, 'currency', kud_reward, cmd.name, pld.msg)
            author = answer_message.author.display_name
            currency = cmd.bot.cfg.pref.currency
            win_title = f'🎉 Correct, {author}, it was {word_choice}. You won {kud_reward} {currency}!'
            win_embed = discord.Embed(color=0x77B255, title=win_title)
            await pld.msg.channel.send(embed=win_embed)
        except asyncio.TimeoutError:
            timeout_title = '🕙 Time\'s up!'
            timeout_embed = discord.Embed(color=0x696969, title=timeout_title)
            timeout_embed.add_field(name=f'It was {word_choice.lower()}.', value=word_description)
            await pld.msg.channel.send(embed=timeout_embed)
        if pld.msg.channel.id in ongoing_list:
            ongoing_list.remove(pld.msg.channel.id)
    else:
        ongoing_error = error('There is one already ongoing.')
        await pld.msg.channel.send(embed=ongoing_error)
