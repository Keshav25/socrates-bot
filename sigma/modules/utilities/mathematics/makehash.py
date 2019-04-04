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

import hashlib

import discord

from sigma.core.mechanics.command import SigmaCommand
from sigma.core.mechanics.payload import CommandPayload
from sigma.core.utilities.generic_responses import error


async def makehash(_cmd: SigmaCommand, pld: CommandPayload):
    if pld.args:
        if len(pld.args) >= 2:
            hash_name = pld.args[0]
            hashes = hashlib.algorithms_available
            if hash_name in hashes:
                qry = ' '.join(pld.args[1:])
                crypt = hashlib.new(hash_name)
                crypt.update(qry.encode('utf-8'))
                final = crypt.hexdigest()
                response = discord.Embed(color=0x66cc66)
                response.add_field(name=f'✅ Hashing With {hash_name.upper()} Done', value=f'```\n{final}\n```')
            else:
                response = discord.Embed(color=0xBE1931)
                response.add_field(name='❗ Unknown Hashing Method', value=f'Available:\n```\n{", ".join(hashes)}\n```')
        else:
            response = error('Not enough arguments.')
    else:
        response = error('Nothing inputted.')
    await pld.msg.channel.send(embed=response)
