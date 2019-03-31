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

import copy

import discord

from sigma.core.mechanics.command import SigmaCommand
from sigma.core.mechanics.payload import CommandPayload
from sigma.core.utilities.dialogue_controls import bool_dialogue
from sigma.core.utilities.generic_responses import error, ok
from sigma.modules.fun.family.models.human import AdoptableHuman


async def adopt(cmd: SigmaCommand, pld: CommandPayload):
    target = pld.msg.mentions[0] if pld.msg.mentions else None
    if target is not None:
        if not target.bot:
            fake_msg = copy.copy(pld.msg)
            fake_msg.author = target
            parent = AdoptableHuman(cmd.db, pld.msg.author.id)
            await parent.load()
            if not parent.exists:
                await parent.new(pld.msg.author)
            else:
                parent.update_name(pld.msg.author.name)
            child = AdoptableHuman(cmd.db, target.id)
            await child.load()
            if not child.exists:
                await child.new(target)
            else:
                child.update_name(target.name)
            direct, sibling, ancestor, descendant = await child.is_related(parent)
            if len(child.parents) >= 2:
                response = error(f'{target.name} already has two parents.')
            elif sibling:
                if direct:
                    response = error(f'{target.name} is one of your siblings.')
                else:
                    response = error(f'{target.name} is one of your cousins.')
            elif child.is_child(pld.msg.author.id):
                response = error(f'{target.name} is one of your ancestors.')
            elif child.is_parent(pld.msg.author.id):
                response = error(f'{target.name} is one of your descendants.')
            else:
                adop_q = discord.Embed(color=0xf9f9f9, title=f'📋 {target.name}, do you accept to be adopted?')
                accepted, timeout = await bool_dialogue(cmd.bot, fake_msg, adop_q)
                if accepted:
                    parent.children.append(child)
                    await parent.save()
                    child.parents.append(parent)
                    await child.save()
                    response = ok(f'Congrats on adopting {target.name}!')
                else:
                    if timeout:
                        response = discord.Embed(color=0x696969, title=f'🕙 {target.name} didn\'t respond.')
                    else:
                        response = error(f'{target.name} rejected the adoption.')
        else:
            response = error('You can\'t adopt bots.')
    else:
        response = error('No user targeted.')
    await pld.msg.channel.send(embed=response)
