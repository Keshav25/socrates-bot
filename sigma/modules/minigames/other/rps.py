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

import secrets

import discord

from sigma.core.mechanics.command import SigmaCommand


async def rps(cmd: SigmaCommand, message: discord.Message, args: list):
    if not args:
        embed = discord.Embed(color=0xBE1931, title='❗ Nothing inputted.')
        await message.channel.send(None, embed=embed)
    else:
        sign_list = ['rock', 'paper', 'scissors']
        my_choice = secrets.choice(sign_list)
        if args[0].lower().startswith('r'):
            their_choice = 'rock'
            counter = 'paper'
        elif args[0].lower().startswith('p'):
            their_choice = 'paper'
            counter = 'scissors'
        elif args[0].lower().startswith('s'):
            their_choice = 'scissors'
            counter = 'rock'
        else:
            embed = discord.Embed(color=0xBE1931, title='❗ Unrecognized sign.')
            await message.channel.send(None, embed=embed)
            return
        if my_choice == their_choice:
            embed = discord.Embed(color=0xFFCC4D, title=':fire: It\'s a draw!')
        elif my_choice == counter:
            embed = discord.Embed(color=0xBE1931, title='❗ You lose!')
        else:
            embed = discord.Embed(color=0x3B88C3, title=':gem: You win!')
        embed.add_field(name='User\'s Choice', value='**' + their_choice.title() + '**')
        embed.add_field(name='Sigma\'s Choice', value='**' + my_choice.title() + '**')
        await message.channel.send(None, embed=embed)
