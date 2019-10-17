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

from sigma.core.mechanics.fetch import get_fetch_helper, SaveResponse


async def channel_dumper(ev):
    """
    :param ev: The event object referenced in the event.
    :type ev: sigma.core.mechanics.event.SigmaEvent
    """
    variant = 'channel'
    responses = []
    fh = get_fetch_helper(ev.bot)
    for channel in ev.bot.get_all_channels():
        if isinstance(channel, discord.TextChannel):
            data = fh.make_channel_data(channel)
            responses.append(await fh.save_object_doc(variant, data))
    ev.log.info(SaveResponse.describe(responses, variant))
