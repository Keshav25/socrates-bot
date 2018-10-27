# Apex Sigma: The Database Giant Discord Bot.
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

import arrow
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import discord

from sigma.core.mechanics.event import SigmaEvent
from sigma.core.mechanics.payload import MessageEditPayload
from sigma.core.utilities.data_processing import user_avatar
from sigma.core.utilities.event_logging import log_event


async def edit_logger(ev: SigmaEvent, pld: MessageEditPayload):
    before, after = pld.before, pld.after
    if after.guild:
        if before.content and after.content and (before.content != after.content):
            log_title = f'{after.author.name}#{after.author.discriminator} edited their message.'
            log_embed = discord.Embed(color=0x262626, timestamp=arrow.utcnow().datetime)
            log_embed.set_author(name=log_title, icon_url=user_avatar(after.author))
            log_embed.add_field(name='➖ Before', value=before.content, inline=False)
            log_embed.add_field(name='➕ After', value=after.content, inline=False)
            log_embed.set_footer(text=f'Message {after.id} in #{after.channel.name}')
            await log_event(ev.bot, after.guild, ev.db, log_embed, 'log_edits')
