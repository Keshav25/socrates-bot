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

import discord

from sigma.core.utilities.data_processing import user_avatar
from sigma.core.utilities.dialogue_controls import bool_dialogue
from sigma.core.utilities.generic_responses import error, not_found
from sigma.modules.minigames.professions.nodes.item_core import get_item_core
from sigma.modules.minigames.utils.ongoing.ongoing import del_ongoing, is_ongoing, set_ongoing


async def sell(cmd, pld):
    """
    :param cmd: The command object referenced in the command.
    :type cmd: sigma.core.mechanics.command.SigmaCommand
    :param pld: The payload with execution data and details.
    :type pld: sigma.core.mechanics.payload.CommandPayload
    """
    if is_ongoing(cmd.name, pld.msg.author.id):
        return
    set_ongoing(cmd.name, pld.msg.author.id)
    item_core = await get_item_core(cmd.db)
    currency = cmd.bot.cfg.pref.currency
    if pld.args:
        inv = await cmd.db.get_inventory(pld.msg.author.id)
        if inv:
            lookup = ' '.join(pld.args)
            if lookup.lower() == 'all':
                ender = 's' if len(inv) != 1 else ''
                worth = sum([item_core.get_item_by_file_id(ient['item_file_id']).value for ient in inv])
                question = f'❔ Are you sure you want to sell {len(inv)} item{ender} worth {worth} {currency}?'
                quesbed = discord.Embed(color=0xF9F9F9, title=question)
                sell_confirm, timeout = await bool_dialogue(cmd.bot, pld.msg, quesbed, True)
                if sell_confirm:
                    value = 0
                    count = 0
                    for invitem in inv.copy():
                        item_ob_id = item_core.get_item_by_file_id(invitem['item_file_id'])
                        value += item_ob_id.value
                        count += 1
                        await cmd.db.del_from_inventory(pld.msg.author.id, invitem['item_id'])
                    await cmd.db.add_resource(pld.msg.author.id, 'currency', value, cmd.name, pld.msg)
                    response = discord.Embed(color=0xc6e4b5)
                    response.title = f'💶 You sold {count} item{ender} for {value} {currency}.'
                else:
                    response = discord.Embed(color=0xBE1931, title='❌ Item sale canceled.')
            elif lookup.lower() == 'duplicates':
                value = 0
                count = 0
                existing_ids = []
                for invitem in inv.copy():
                    file_id = invitem['item_file_id']
                    if file_id in existing_ids:
                        item_ob_id = item_core.get_item_by_file_id(file_id)
                        value += item_ob_id.value
                        count += 1
                        await cmd.db.del_from_inventory(pld.msg.author.id, invitem['item_id'])
                    else:
                        existing_ids.append(file_id)
                await cmd.db.add_resource(pld.msg.author.id, 'currency', value, cmd.name, pld.msg)
                ender = 's' if count != 1 else ''
                response = discord.Embed(color=0xc6e4b5)
                response.title = f'💶 You sold {count} duplicate{ender} for {value} {currency}.'
            else:
                request_count = 1
                if lookup.split()[0].isdigit:
                    parts = lookup.split(None, 1)
                    request_count = int(parts[0])
                    lookup = parts[1]
                item_o = item_core.get_item_by_name(lookup)                    
                count = 0
                value = 0
                if item_o:
                    for x in range(request_count):
                        item = await cmd.db.get_inventory_item(pld.msg.author.id, item_o.file_id)
                        if item:
                            value += item_o.value
                            count += 1
                            await cmd.db.del_from_inventory(pld.msg.author.id, item['item_id'])
                        else
                            break
                if count > 0:
                    await cmd.db.add_resource(pld.msg.author.id, 'currency', value, cmd.name, pld.msg)
                    ender = 's' if count != 1 else ''
                    response = discord.Embed(color=0xc6e4b5)
                    response.title = f'💶 You sold {count} {item_o.name}{ender} for {value} {currency}.'
                else:
                    response = not_found(f'I didn\'t find any {lookup} in your inventory.')
        else:
            response = discord.Embed(color=0xc6e4b5, title='💸 Your inventory is empty...')
    else:
        response = error('Nothing inputted.')
    if is_ongoing(cmd.name, pld.msg.author.id):
        del_ongoing(cmd.name, pld.msg.author.id)
    response.set_author(name=pld.msg.author.display_name, icon_url=user_avatar(pld.msg.author))
    await pld.msg.channel.send(embed=response)
