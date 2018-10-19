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

import asyncio

from sigma.core.mechanics.event import SigmaEvent


async def autorole_control(ev: SigmaEvent, member):
    curr_role_id = await ev.db.get_guild_settings(member.guild.id, 'auto_role')
    if curr_role_id:
        curr_role = member.guild.get_role(curr_role_id)
        if curr_role:
            timeout = await ev.db.get_guild_settings(member.guild.id, 'auto_role_timeout')
            if timeout:
                await asyncio.sleep(timeout)
            try:
                await member.add_roles(curr_role, reason='Appointed guild autorole.')
            except (discord.NotFound, discord.Forbidden):
                pass
