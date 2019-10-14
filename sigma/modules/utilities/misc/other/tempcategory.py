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

from sigma.core.utilities.generic_responses import denied, error, ok, not_found


async def tempcategory(cmd, pld):
    """
    :param cmd: The command object referenced in the command.
    :type cmd: sigma.core.mechanics.command.SigmaCommand
    :param pld: The payload with execution data and details.
    :type pld: sigma.core.mechanics.payload.CommandPayload
    """
    if pld.msg.author.permissions_in(pld.msg.channel).manage_channels:
        if pld.args:
            if pld.args[0].lower() == 'disable':
                await cmd.db.set_guild_settings(pld.msg.guild.id, 'temp_channel_category', None)
                response = ok('Temp Channel Category disabled.')
                await pld.msg.channel.send(embed=response)
                return
            target = None
            lookup = ' '.join(pld.args).lower()
            if lookup.isdigit():
                try:
                    search = pld.msg.guild.get_channel(int(lookup))
                    if isinstance(search, discord.CategoryChannel):
                        target = search
                except ValueError:
                    target = None
            else:
                target = discord.utils.find(lambda c: c.name.lower() == lookup, pld.msg.guild.categories)
            if target:
                if pld.msg.guild.me.permissions_in(target).manage_channels:
                    await cmd.db.set_guild_settings(pld.msg.guild.id, 'temp_channel_category', target.id)
                    response = ok(f'Temp Channel Category set to {target.name}')
                else:
                    response = error('I can\'t create channels in that category.')
            else:
                response = not_found('Category not found.')
        else:
            response = error('Nothing inputted.')
    else:
        response = denied('Access Denied. Manage Channels needed.')
    await pld.msg.channel.send(embed=response)
