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

import inspect

import discord

from sigma.core.mechanics.command import SigmaCommand


async def evaluate(_cmd: SigmaCommand, pld: CommandPayload):
    if args:
        try:
            execution = " ".join(args)
            output = eval(execution)
            if inspect.isawaitable(output):
                output = await output
            response = discord.Embed(color=0x77B255, title='✅ Executed')
            response.description = f'```py\n{output}\n```'
        except Exception as e:
            response = discord.Embed(color=0xBE1931, title='❗ Error')
            response.description = f'```py\n{e}\n```'
    else:
        response = discord.Embed(color=0xBE1931, title='❗ Nothing inputted.')
    await message.channel.send(embed=response)
