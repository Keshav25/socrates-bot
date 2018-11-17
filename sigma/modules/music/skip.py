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

import discord

from sigma.core.mechanics.command import SigmaCommand
from sigma.core.mechanics.payload import CommandPayload
from sigma.core.utilities.data_processing import user_avatar


async def skip(cmd: SigmaCommand, pld: CommandPayload):
    if pld.msg.author.voice:
        same_bound = True
        if pld.msg.guild.voice_client:
            if pld.msg.guild.voice_client.channel.id != pld.msg.author.voice.channel.id:
                same_bound = False
        if same_bound:
            if pld.msg.guild.voice_client:
                queue = cmd.bot.music.get_queue(pld.msg.guild.id)
                if queue:
                    curr = cmd.bot.music.currents.get(pld.msg.guild.id)
                    if curr:
                        pld.msg.guild.voice_client.stop()
                        response = discord.Embed(color=0x66CC66, title=f'✅ Skipping {curr.title}.')
                        requester = f'{pld.msg.author.name}#{pld.msg.author.discriminator}'
                        response.set_author(name=requester, icon_url=user_avatar(pld.msg.author))
                    else:
                        response = discord.Embed(color=0xBE1931, title='❗ Nothing currently playing.')
                else:
                    response = discord.Embed(color=0xBE1931, title='❗ The queue is empty or this is the last song.')
            else:
                response = discord.Embed(color=0xBE1931, title='❗ I am not connected to any channel.')
        else:
            response = discord.Embed(color=0xBE1931, title='❗ You are not in my voice channel.')
    else:
        response = discord.Embed(color=0xBE1931, title='❗ You are not in a voice channel.')
    await pld.msg.channel.send(embed=response)
