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

from sigma.core.utilities.generic_responses import ok
from sigma.modules.moderation.server_settings.roles.autorole.bound_role_cacher import update_invites


async def syncinvites(cmd, pld):
    """
    :param cmd: The command object referenced in the command.
    :type cmd: sigma.core.mechanics.command.SigmaCommand
    :param pld: The payload with execution data and details.
    :type pld: sigma.core.mechanics.payload.CommandPayload
    """
    try:
        invites = await pld.msg.guild.invites()
    except discord.Forbidden:
        invites = []
    await update_invites(cmd.db, pld.msg.guild, invites)
    bound_invites = pld.settings.get('bound_invites') or {}
    keys_to_remove = []
    for invite_code in bound_invites.keys():
        find_code = discord.utils.find(lambda x: x.id == invite_code, invites)
        if not find_code:
            keys_to_remove.append(invite_code)
    if keys_to_remove:
        for key_to_remove in keys_to_remove:
            bound_invites.pop(key_to_remove)
    await cmd.db.set_guild_settings(pld.msg.guild.id, 'bound_invites', bound_invites)
    noresp = False
    if pld.args:
        if pld.args[0] == 'noresp':
            noresp = True
    if not noresp:
        inv_count = len(invites)
        response = ok(f'Synced {inv_count} invites.')
        await pld.msg.channel.send(embed=response)
