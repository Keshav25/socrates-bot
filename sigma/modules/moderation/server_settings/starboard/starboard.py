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

from sigma.core.utilities.generic_responses import denied, ok


async def starboard(cmd, pld):
    """
    :param cmd: The command object referenced in the command.
    :type cmd: sigma.core.mechanics.command.SigmaCommand
    :param pld: The payload with execution data and details.
    :type pld: sigma.core.mechanics.payload.CommandPayload
    """
    if pld.msg.author.permissions_in(pld.msg.channel).manage_guild:
        starboard_doc = pld.settings.get('starboard') or {}
        active = starboard_doc.get('state')
        state, ender = (False, 'disabled') if active else (True, 'enabled')
        starboard_doc.update({'state': state})
        await cmd.db.set_guild_settings(pld.msg.guild.id, 'starboard', starboard_doc)
        response = ok(f'Starboard {ender}.')
    else:
        response = denied('Access Denied. Manage Server needed.')
    await pld.msg.channel.send(embed=response)
