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

import discord

from sigma.core.mechanics.payload import CommandPayload, MessagePayload


def log_dm(ev, pld: MessagePayload):
    """
    :param ev: The event object referenced in the event.
    :type ev: sigma.core.mechanics.event.SigmaEvent
    :param pld:
    :type pld:
    """
    author_text = f'{pld.msg.author.name}#{pld.msg.author.discriminator} [{pld.msg.author.id}]'
    ev.log.info(f'DM From {author_text}: {pld.msg.content}')


async def has_invite(ev, arguments):
    """
    :param ev: The event object referenced in the event.
    :type ev: sigma.core.mechanics.event.SigmaEvent
    :param arguments:
    :type arguments:
    :return:
    :rtype:
    """
    invite_found = False
    for arg in arguments:
        triggers = ['discord.gg', 'discordapp.com']
        for trigger in triggers:
            if trigger in arg:
                try:
                    await ev.bot.fetch_invite(arg)
                    invite_found = True
                    break
                except discord.NotFound:
                    pass
    return invite_found


async def dm_detection(ev, pld: MessagePayload):
    """
    :param ev: The event object referenced in the event.
    :type ev: sigma.core.mechanics.event.SigmaEvent
    :param pld:
    :type pld:
    """
    if not pld.msg.guild:
        if not pld.msg.author.bot:
            pfx = ev.db.get_prefix(pld.settings)
            if not pld.msg.content.startswith(pfx):
                if await has_invite(ev, pld.msg.content.split()):
                    command = 'invite'
                else:
                    log_dm(ev, pld)
                    command = 'help'
                if not await ev.bot.cool_down.on_cooldown(ev.name, pld.msg.author):
                    await ev.bot.modules.commands[command].execute(CommandPayload(ev.bot, pld.msg, []))
                await ev.bot.cool_down.set_cooldown(ev.name, pld.msg.author, 30)
