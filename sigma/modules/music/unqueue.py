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

from asyncio.queues import Queue

import discord

from sigma.core.utilities.data_processing import user_avatar
from sigma.core.utilities.generic_responses import GenericResponse


async def unqueue(cmd, pld):
    """
    :param cmd: The command object referenced in the command.
    :type cmd: sigma.core.mechanics.command.SigmaCommand
    :param pld: The payload with execution data and details.
    :type pld: sigma.core.mechanics.payload.CommandPayload
    """
    if pld.args:
        if pld.msg.author.voice:
            same_bound = True
            if pld.msg.guild.voice_client:
                if pld.msg.guild.voice_client.channel.id != pld.msg.author.voice.channel.id:
                    same_bound = False
            if same_bound:
                if pld.msg.guild.voice_client:
                    queue = cmd.bot.music.get_queue(pld.msg.guild.id)
                    if not queue.empty():
                        try:
                            order_num = int(pld.args[0])
                            if order_num >= 1:
                                order_num -= 1
                            queue_list = await cmd.bot.music.listify_queue(queue)
                            queue_size = len(queue_list)
                            if order_num <= queue_size - 1:
                                item = queue_list[order_num]
                                is_mod = pld.msg.author.guild_permissions.manage_guild
                                is_req = item.requester.id == pld.msg.author.id
                                if is_mod or is_req:
                                    queue_list.remove(item)
                                    new_queue = Queue()
                                    for list_item in queue_list:
                                        await new_queue.put(list_item)
                                    cmd.bot.music.queues.update({pld.msg.guild.id: new_queue})
                                    response = GenericResponse(f'Removed {item.title}.').ok()
                                    requester = f'{pld.msg.author.name}#{pld.msg.author.discriminator}'
                                    response.set_author(name=requester, icon_url=user_avatar(pld.msg.author))
                                else:
                                    auth_deny_desc = f'Sorry, {pld.msg.author.name}. To remove a song you need to be'
                                    auth_deny_desc += ' the person who requested it, or have the Manage Server'
                                    auth_deny_desc += f' permission on {pld.msg.guild.name}.'
                                    response = discord.Embed(color=0xBE1931)
                                    response.add_field(name='⛔ Access Denied', value=auth_deny_desc)
                            else:
                                response = GenericResponse('Input out of range.').error()
                        except ValueError:
                            response = GenericResponse('Invalid input. Numbers only.').error()
                    else:
                        response = GenericResponse('The queue is empty.').error()
                else:
                    response = GenericResponse('I am not connected to any channel.').error()
            else:
                response = GenericResponse('You are not in my voice channel.').error()
        else:
            response = GenericResponse('You are not in a voice channel.').error()
    else:
        response = GenericResponse('Nothing inputted.').error()
    await pld.msg.channel.send(embed=response)
