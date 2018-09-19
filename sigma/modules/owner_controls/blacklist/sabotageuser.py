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

from sigma.core.mechanics.command import SigmaCommand


async def sabotageuser(cmd: SigmaCommand, message: discord.Message, args: list):
    if args:
        target_id = None
        if args[0].isdigit():
            target_id = int(args[0])
        if target_id:
            if target_id not in cmd.bot.cfg.dsc.owners:
                all_members = cmd.bot.get_all_members()
                target = discord.utils.find(lambda x: x.id == target_id, all_members)
                if target:
                    sabotage_collection = cmd.db[cmd.bot.cfg.db.database].SabotagedUsers
                    sabotage_file = await sabotage_collection.find_one({'user_id': target.id})
                    if sabotage_file:
                        await cmd.db[cmd.bot.cfg.db.database].SabotagedUsers.delete_one({'user_id': target.id})
                        icon, result = '🔓', 'unsabotaged'
                    else:
                        await cmd.db[cmd.bot.cfg.db.database].SabotagedUsers.insert_one({'user_id': target.id})
                        icon, result = '🔒', 'sabotaged'
                    response = discord.Embed(color=0xFFCC4D, title=f'{icon} {target.name} has been {result}.')
                else:
                    response = discord.Embed(color=0x696969, title='🔍 No user with that ID was found.')
            else:
                response = discord.Embed(color=0xBE1931, title='❗ That target is immune.')
        else:
            response = discord.Embed(color=0xBE1931, title='❗ Invalid user ID.')
    else:
        response = discord.Embed(color=0xBE1931, title='❗ Missing user ID.')
    await message.channel.send(embed=response)
