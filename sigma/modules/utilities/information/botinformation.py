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

import sys

import arrow
import discord

from sigma.core.mechanics.command import SigmaCommand
from sigma.core.mechanics.payload import CommandPayload

sigma_image = 'https://i.imgur.com/mGyqMe1.png'
support_url = 'https://discordapp.com/invite/aEUCHwX'


async def botinformation(cmd, pld):
    """
    :param cmd: The command object referenced in the command.
    :type cmd: sigma.core.mechanics.command.SigmaCommand
    :param pld: The payload with execution data and details.
    :type pld: sigma.core.mechanics.payload.CommandPayload
    """
    version = cmd.bot.info.get_version()
    authors = cmd.bot.info.get_authors().authors
    full_version = f'{version.major}.{version.minor}.{version.patch}'
    if version.beta:
        full_version += ' Beta'
    sigma_title = f'Apex Sigma: v{full_version} {version.codename}'
    env_text = f'Language: **Python** {sys.version.split()[0]}'
    env_text += f'\nLibrary: **discord.py** {discord.__version__}'
    env_text += f'\nPlatform: **{sys.platform.upper()}**'
    auth_text = ''
    for author in authors:
        auth = await cmd.bot.get_user(author.id)
        if auth:
            auth_text += f'\n**{auth.name}**#{auth.discriminator}'
        else:
            auth_text += f'\n**{author.name}**#{author.discriminator}'
    response = discord.Embed(color=0x1B6F5F, timestamp=arrow.get(version.timestamp).datetime)
    response.set_author(name=sigma_title, icon_url=sigma_image, url=support_url)
    response.add_field(name='Authors', value=auth_text)
    response.add_field(name='Environment', value=env_text)
    response.set_footer(text=f'Last updated {arrow.get(version.timestamp).humanize()}')
    await pld.msg.channel.send(embed=response)
