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

import asyncio

from sigma.modules.games.warframe.commons.cycles.generic import send_to_channels
from sigma.modules.games.warframe.commons.parsers.acolyte_parser import generate_acolyte_embed, get_acolyte_data

wfaco_loop_running = False


async def acolyte_clockwork(ev):
    """
    :param ev: The event object referenced in the event.
    :type ev: sigma.core.mechanics.event.SigmaEvent
    """
    global wfaco_loop_running
    if not wfaco_loop_running:
        wfaco_loop_running = True
        ev.bot.loop.create_task(acolyte_cycler(ev))


async def acolyte_cycler(ev):
    """
    :param ev: The event object referenced in the event.
    :type ev: sigma.core.mechanics.event.SigmaEvent
    """
    while True:
        if ev.bot.is_ready():
            # noinspection PyBroadException
            try:
                acolytes, triggers = await get_acolyte_data(ev.db)
                if acolytes:
                    response = generate_acolyte_embed(acolytes)
                    await send_to_channels(ev, response, 'warframe_acolyte_channel', triggers)
            except Exception:
                pass
        await asyncio.sleep(5)
