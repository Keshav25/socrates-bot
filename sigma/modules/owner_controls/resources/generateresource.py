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

from sigma.core.mechanics.command import SigmaCommand
from sigma.core.mechanics.payload import CommandPayload
from sigma.core.utilities.generic_responses import error, ok


async def generateresource(cmd, pld):
    """
    :param cmd: The command object referenced in the command.
    :type cmd: sigma.core.mechanics.command.SigmaCommand
    :param pld: The payload with execution data and details.
    :type pld: sigma.core.mechanics.payload.CommandPayload
    """
    if pld.msg.mentions:
        if len(pld.args) >= 3:
            target = pld.msg.mentions[0]
            if not target.bot:
                try:
                    amount = abs(int(pld.args[-1]))
                    currency = cmd.bot.cfg.pref.currency.lower()
                    res_nam = 'currency' if pld.args[0].lower() == currency else pld.args[0].lower()
                    await cmd.db.add_resource(target.id, res_nam, amount, cmd.name, pld.msg, False)
                    response = ok(f'Ok, I\'ve given {amount} {res_nam} to {target.display_name}.')
                except ValueError:
                    response = error('Invalid amount.')
            else:
                response = error('You can\'t give resources to bots.')
        else:
            response = error('Resource name, amount and target needed.')
    else:
        response = error('No user targeted.')
    await pld.msg.channel.send(embed=response)
