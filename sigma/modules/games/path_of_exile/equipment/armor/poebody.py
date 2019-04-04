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

import aiohttp
import discord
import lxml.html as lx

from sigma.core.utilities.generic_responses import error, not_found

body_armor_list_cache = {}
body_armor_data_cache = {}
body_armor_icon = 'https://i.imgur.com/wcY4eDb.png'
item_urls = [
    'https://pathofexile.gamepedia.com/Body_Armour',
    'https://pathofexile.gamepedia.com/List_of_unique_body_armours'
]


async def fill_body_armor_cache():
    if not body_armor_list_cache:
        for active_sg_url in item_urls:
            async with aiohttp.ClientSession() as session:
                async with session.get(active_sg_url) as data:
                    page_html_raw = await data.text()
            page_html = lx.fromstring(page_html_raw)
            armor_items = page_html.cssselect('.c-item-hoverbox')
            for armor_item in armor_items:
                armor_name = armor_item[0][0].text
                if armor_name:
                    armor_dkey = armor_name.replace(' ', '_').lower()
                    url_pointer = armor_item[0][0].attrib.get("href")
                    armor_link = f'https://pathofexile.gamepedia.com{url_pointer}'
                    body_armor_list_cache.update({armor_dkey: {'name': armor_name, 'url': armor_link}})


async def get_armor_data(armor_name: str, armor_url: str):
    """

    :param armor_name:
    :type armor_name:
    :param armor_url:
    :type armor_url:
    :return:
    :rtype:
    """
    armor_key = armor_name.replace(' ', '_').lower()
    armor_data = body_armor_data_cache.get(armor_key)
    if not armor_data:
        async with aiohttp.ClientSession() as session:
            async with session.get(armor_url) as data:
                page_html_raw = await data.text()
        page_html = lx.fromstring(page_html_raw)
        isb = page_html.cssselect('.item-stats')[0]
        armor_info = "\n".join([row.text_content().strip() for row in isb[0]])
        try:
            armor_level = int(isb[1][0][0][0].text or 0)
        except IndexError:
            armor_level = 0
        try:
            requitements = isb[1][0].text_content()
        except IndexError:
            requitements = None
        try:
            armor_desc = isb[2].text_content()
        except IndexError:
            armor_desc = None
        armor_image = page_html.cssselect(".image")[0][0].attrib.get("src")
        armor_data = {
            'name': armor_name,
            'url': armor_url,
            'info': parse_armor_info(armor_info),
            'level': armor_level,
            'desc': armor_desc,
            'image': armor_image,
            'requirements': requitements
        }
        body_armor_data_cache.update({armor_key: armor_data})
    return armor_data


def find_broad(lookup: str):
    """

    :param lookup:
    :type lookup:
    :return:
    :rtype:
    """
    out = None
    for key in body_armor_list_cache:
        if lookup in key:
            out = body_armor_list_cache.get(key)
            break
    return out


def parse_armor_info(armor_info: str):
    """

    :param armor_info:
    :type armor_info:
    :return:
    :rtype:
    """
    sects = armor_info.split('\n\n')
    types = sects[0].split('\n')[0]
    types = types.split(': ')
    det_sects = sects[1:]
    info_lines = [[types[0], types[1]]]
    for det_sect in det_sects:
        if ': ' in det_sect:
            info_name = det_sect.split(': ')[0].strip()
            info_value = det_sect.split(': ')[1].strip()
            info_lines.append([info_name, info_value])
    return {'types': types, 'details': info_lines}


async def poebody(_cmd, pld):
    """
    :param _cmd: The command object referenced in the command.
    :type _cmd: sigma.core.mechanics.command.SigmaCommand
    :param pld: The payload with execution data and details.
    :type pld: sigma.core.mechanics.payload.CommandPayload
    """
    if pld.args:
        lookup_key = '_'.join(pld.args).lower()
        await fill_body_armor_cache()
        armor_entry = body_armor_list_cache.get(lookup_key) or find_broad(lookup_key)
        if armor_entry:
            armor_entry = await get_armor_data(armor_entry.get('name'), armor_entry.get('url'))
            if armor_entry:
                if armor_entry.get('level'):
                    armor_info_block = f'**Level**: {armor_entry.get("level")}'
                else:
                    armor_info_block = ''
                for detail in armor_entry.get('info').get('details'):
                    armor_info_block += f'\n**{detail[0]}**: {detail[1]}'
                img_data = armor_entry.get('image')
                title = f'Body Armor: {armor_entry.get("name")}'
                response = discord.Embed(color=0xf2c462)
                response.description = armor_entry.get('desc')
                response.set_thumbnail(url=img_data)
                response.set_author(name=title, icon_url=body_armor_icon, url=armor_entry.get('url'))
                response.add_field(name='Information', value=armor_info_block, inline=False)
                response.set_footer(text=armor_entry.get("requirements"))
            else:
                response = error('Invalid armor data received.')
        else:
            response = not_found('Armor not found.')
    else:
        response = error('Nothing inputted.')
    await pld.msg.channel.send(embed=response)
