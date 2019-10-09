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
import io

import aiohttp
import discord
from PIL import Image

from sigma.core.utilities.data_processing import user_avatar
from sigma.modules.utilities.misc.other.event.spooktober.mech.image.compositor import ImageCompositor


async def pumpkin(cmd, pld):
    """
    :param cmd: The command object referenced in the command.
    :type cmd: sigma.core.mechanics.command.SigmaCommand
    :param pld: The payload with execution data and details.
    :type pld: sigma.core.mechanics.payload.CommandPayload
    """
    target = pld.msg.mentions[0] if pld.msg.mentions else pld.msg.author
    weight_res = await cmd.db.get_resource(target.id, 'weight')
    weight_val = round(weight_res.current / 1000, 2)
    canv = ImageCompositor(cmd.resource('font/exo2-regular.ttf'), 666, 420)
    bg = ImageCompositor.resize(cmd.resource('img/bg/bg_pumpkin.png'), width=666, height=420).convert('L')
    canv.stick(bg, (0, 0), cmd.resource('img/bg/bg_mask.png'))
    canv.stick(cmd.resource('img/bg/bg_rim.png'), (0, 0))

    canv.stick(cmd.resource('img/pmk/pmk_body_v2.png'), (40, 65))

    name_img = canv.text_image(target.name, 34, (179, 36, 25))
    disc_img = canv.text_image(f'#{target.discriminator}', 34)
    full_nam = Image.new(
        'RGBA',
        (
            name_img.width + disc_img.width,
            max([name_img.height, disc_img.height])
        ),
        (0, 0, 0, 0)
    )
    full_nam.paste(name_img, (0, 0))
    full_nam.paste(disc_img, (name_img.width, 0))
    full_nam = ImageCompositor.resize(full_nam, width=152)
    canv.stick(cmd.resource('img/user/name.png'), (378, 247))
    canv.stick(full_nam, (402, 246 + int((42 - full_nam.height) / 2.125)))

    value_img = canv.text_image(str(weight_val), 34, (179, 36, 25))
    kilog_img = canv.text_image('kg', 34)

    weight = Image.new(
        'RGBA',
        (
            value_img.width + disc_img.width,
            max([value_img.height, kilog_img.height])
        ),
        (0, 0, 0, 0)
    )
    weight.paste(value_img, (0, 0))
    weight.paste(kilog_img, (value_img.width, 0))
    weight = ImageCompositor.resize(weight, width=120)

    canv.stick(weight, (128, 70 + (30 - weight.height)))

    async with aiohttp.ClientSession() as session:
        async with session.get(str(target.avatar_url_as(format='png', size=128))) as data:
            avatar_raw = await data.read()

    avatar_img = Image.open(io.BytesIO(avatar_raw))
    avatar_img = ImageCompositor.resize(avatar_img, 95, 95)
    canv.stick(avatar_img, (431, 137), cmd.resource('img/user/av_mask.png'))
    canv.stick(cmd.resource('img/user/av_rim.png'), (431, 137))

    response = discord.Embed(color=0xbf181d)
    response.set_author(name=f'{target.display_name}\'s Pumpkin', icon_url=user_avatar(target))
    file_name = f'pumpkin_{pld.msg.id}.png'
    file = discord.File(canv.to_bytes(), file_name)
    response.set_image(url=f'attachment://{file_name}')
    await pld.msg.channel.send(embed=response, file=file)
