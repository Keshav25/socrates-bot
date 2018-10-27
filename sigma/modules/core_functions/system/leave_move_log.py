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

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import discord

from sigma.core.mechanics.event import SigmaEvent
from sigma.core.mechanics.payload import GuildPayload
from sigma.core.utilities.data_processing import user_avatar
from sigma.modules.core_functions.system.move_log_embed import make_move_log_embed


async def leave_move_log(ev: SigmaEvent, pld: GuildPayload):
    bot_count = 0
    user_count = 0
    for user in pld.guild.members:
        if user.bot:
            bot_count += 1
        else:
            user_count += 1
    owner = pld.guild.owner
    log_lines = f'Guild: {pld.guild.name}[{pld.guild.id}] | '
    log_lines += f'Owner: {owner.name} [{owner.id}] | '
    log_lines += f'Members: {user_count} | Bots: {bot_count}'
    ev.log.info(log_lines)
    if ev.bot.cfg.pref.movelog_channel:
        mlc_id = ev.bot.cfg.pref.movelog_channel
        mlc = await ev.bot.get_channel(mlc_id, True)
        if mlc:
            if pld.guild.icon_url:
                icon = pld.guild.icon_url
            else:
                icon = user_avatar(pld.guild.owner)
            log_embed = discord.Embed(color=0xBE1931)
            log_embed.set_author(name='Left A Guild', icon_url=icon, url=icon)
            make_move_log_embed(log_embed, pld.guild)
            await mlc.send(embed=log_embed)
