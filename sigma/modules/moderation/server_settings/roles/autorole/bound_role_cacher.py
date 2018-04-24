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

cache = {}


def update_invites(guild, invites):
    cache.update({guild.id: invites})


def get_changed_invite(guild_id, bound_list, invites):
    invite = None
    cached = cache.get(guild_id)
    if cached is None:
        cached = []
    cache.update({guild_id: invites})
    if invites is None:
        invites = []
    if invites:
        for cached_inv in cached:
            for curr_inv in invites:
                if cached_inv.id == curr_inv.id:
                    if cached_inv.uses != curr_inv.uses:
                        if curr_inv.id in bound_list:
                            invite = curr_inv
                            break
    return invite


async def bound_role_cacher(ev: SigmaEvent):
    counter = 0
    ev.log.info('Starting invite caching...')
    for guild in ev.bot.guilds:
        if await ev.db.get_guild_settings(guild.id, 'BoundInvites'):
            if guild.me.guild_permissions.create_instant_invite:
                try:
                    invites = await guild.invites()
                    counter += 1
                except discord.Forbidden:
                    invites = []
                cache.update({guild.id: invites})
    ev.log.info(f'Finished caching invites for {counter} guilds.')
