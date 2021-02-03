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

import discord

from sigma.core.utilities.data_processing import user_avatar
from sigma.core.utilities.generic_responses import GenericResponse


async def message_search(lookup, message):
    """

    :param lookup:
    :type lookup: int
    :param message:
    :type message: discord.Message
    :return:
    :rtype: discord.Message
    """
    try:
        msg = await message.channel.fetch_message(lookup)
    except discord.NotFound:
        msg = None
    if not msg:
        for channel in message.guild.channels:
            if isinstance(channel, discord.TextChannel):
                try:
                    msg = await channel.fetch_message(lookup)
                    break
                except (discord.Forbidden, discord.NotFound):
                    msg = None
    return msg


async def quote(_cmd, pld):
    """
    :param _cmd: The command object referenced in the command.
    :type _cmd: sigma.core.mechanics.command.SigmaCommand
    :param pld: The payload with execution data and details.
    :type pld: sigma.core.mechanics.payload.CommandPayload
    """
    if pld.args:
        lookup = pld.args[0]
        if lookup.isdigit():
            msg = await message_search(int(lookup), pld.msg)
            if msg:
                valid = False
                pref_arg = pld.args[-1].lower()
                prefix = 'canary' if pref_arg == '--canary' else 'ptb' if pref_arg == '--ptb' else None
                domain = 'discordapp.com' if not prefix else f'{prefix}.discordapp.com'
                msg_url = f'https://{domain}/channels/{msg.guild.id}/{msg.channel.id}/{msg.id}'
                location = f'{msg.guild.name} | #{msg.channel.name}'
                response = discord.Embed(color=msg.author.color, timestamp=msg.created_at)
                response.set_author(name=msg.author.display_name, icon_url=user_avatar(msg.author), url=msg_url)
                response.set_footer(text=location)
                if msg.content:
                    valid = True
                    response.description = msg.content
                if msg.attachments:
                    valid = True
                    attachments = []
                    for attachment in msg.attachments:
                        size, ender = attachment.size, 'B'
                        if size >= 1000000:
                            size, ender = round(size / 1000000, 2), 'Mb'
                        elif size >= 1000:
                            size, ender = round(size / 1000, 2), 'Kb'
                        details = f'[{attachment.filename}]({attachment.url}): {size} {ender}'
                        attachments.append(details)
                    response.add_field(name='Attachments', value='\n'.join(attachments), inline=False)
                if not valid:
                    response = GenericResponse('That message has no text content.').error()
            else:
                response = GenericResponse('Message not found.').not_found()
        else:
            response = GenericResponse('Invalid message ID.').error()
    else:
        response = GenericResponse('Nothing inputted.').error()
    await pld.msg.channel.send(embed=response)
