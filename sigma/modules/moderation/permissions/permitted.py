# Apex Sigma: The Database Giant Discord Bot.
# Copyright (C) 2019  Lucia's Cipher
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

from sigma.core.mechanics.command import SigmaCommand
from sigma.core.mechanics.paginator import PaginatorCore
from sigma.core.mechanics.payload import CommandPayload
from sigma.core.utilities.data_processing import get_image_colors
from sigma.core.utilities.generic_responses import error, not_found
from sigma.modules.moderation.permissions.nodes.permission_data import get_all_perms
from sigma.modules.moderation.permissions.permit import get_target_type


def get_exceptions(message: discord.Message, exceptions: list, target_type: str):
    overridden_items = []
    guild_dict = {'channels': message.guild.channels, 'users': message.guild.members, 'roles': message.guild.roles}
    guild_items = guild_dict.get(target_type)
    for exc_chn_id in exceptions:
        pnd = '#' if target_type == 'channels' else ''
        exc_item = discord.utils.find(lambda c: c.id == exc_chn_id, guild_items)
        exc_item_name = f'{pnd}{exc_item.name}' if exc_item else str(exc_chn_id)
        overridden_items.append(exc_item_name)
    return overridden_items


async def permitted(cmd: SigmaCommand, pld: CommandPayload):
    if pld.args:
        if len(pld.args) >= 2:
            if ':' in pld.args[1]:
                target_type = get_target_type(pld.args[0].lower())
                if target_type:
                    perm_mode = pld.args[1].split(':')[0]
                    node_name = pld.args[1].split(':')[1]
                    modes = {
                        'c': ('Command', 'command_exceptions', cmd.bot.modules.commands, True),
                        'm': ('Module', 'module_exceptions', cmd.bot.modules.categories, False)
                    }
                    perms = await get_all_perms(cmd.db, pld.msg)
                    mode_vars = modes.get(perm_mode)
                    if mode_vars:
                        mode_name, exception_group, check_group, check_alts = mode_vars
                        if check_alts:
                            if node_name in cmd.bot.modules.alts:
                                node_name = cmd.bot.modules.alts[node_name]
                        if node_name in check_group:
                            exceptions = perms.get(exception_group, {}).get(node_name, {}).get(target_type, [])
                            overridden_items = get_exceptions(pld.msg, exceptions, target_type)
                            if overridden_items:
                                total_overrides = len(overridden_items)
                                page = pld.args[2] if len(pld.args) > 2 else 1
                                overrides, page = PaginatorCore.paginate(overridden_items, page, 50)
                                title = f'{pld.msg.guild.name} {node_name.upper()} {target_type[:-1].title()} Overrides'
                                info = f'[Page {page}] Showing {len(overrides)} '
                                info += f'out of {total_overrides} channel overrides.'
                                response = discord.Embed(color=await get_image_colors(pld.msg.guild.icon_url))
                                response.set_author(name=title, icon_url=pld.msg.guild.icon_url)
                                response.description = ', '.join(overrides)
                                response.set_footer(text=info)
                            else:
                                title = f'🔍 No {target_type[:-1]} overrides found for {node_name}.'
                                response = discord.Embed(color=0x696969, title=title)
                        else:
                            mmn = mode_name.lower()
                            response = not_found(f'No {node_name} {mmn} found.')
                    else:
                        response = error('Unrecognized lookup mode, see usage example.')
                else:
                    response = error('Invalid target type.')
            else:
                response = error('Separate permission type and name with a colon.')
        else:
            response = error('Not enough arguments.')
    else:
        response = error('Nothing inputted.')
    await pld.msg.channel.send(embed=response)
