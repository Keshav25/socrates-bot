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

from sigma.core.utilities.generic_responses import GenericResponse
from sigma.modules.fun.mbti.mech.storage import MBTICore

mbti_img = 'https://i.imgur.com/XzJPkmu.png'
types_src = 'https://www.typeinmind.com/'
funcs_src = 'https://www.cognitiveprocesses.com/Cognitive-Functions'


def make_paragraph(items):
    """
    Creates a paragraph from a dict.
    :type items: dict
    :rtype: str
    """
    pieces = []
    for key, value in items.items():
        if key == 'stack':
            stack_text = '**Stack:** '
            stack_text += '-'.join([f.title() for f in value.split('-')])
            value = stack_text
        elif key == 'name':
            value = f'**{value}**'
        pieces.append(value)
    return '\n\n'.join(pieces)


async def mbti(_cmd, pld):
    """
    :param _cmd: The command object referenced in the command.
    :type _cmd: sigma.core.mechanics.command.SigmaCommand
    :param pld: The payload with execution data and details.
    :type pld: sigma.core.mechanics.payload.CommandPayload
    """
    if pld.args:
        lookup = pld.args[0].lower()
        if len(pld.args) == 2:
            target = pld.args[1].lower()
            if lookup in MBTICore.mbti_types and target in MBTICore.mbti_types:
                type_comp_list = MBTICore.mbti_chart[lookup]
                type_comp = type_comp_list[MBTICore.mbti_list.index(target)]
                type_comp_desc = MBTICore.mbti_compatibility.get(f'{lookup.upper()} x {target.upper()}')
                if not type_comp_desc:
                    type_comp_desc = MBTICore.mbti_compatibility.get(f'{target.upper()} x {lookup.upper()}')
                    lookup, target = target, lookup
                title = f'👥 Compatibility of {lookup.upper()} and {target.upper()}'
                response = discord.Embed(color=0x734d5f, title=title)
                if type_comp_desc:
                    response.description = make_paragraph(type_comp_desc)
                    response.set_footer(text=f'{type_comp} out of 5 compatibility.')
                else:
                    response.description = f'{type_comp} out of 5 compatibility.'
                    response.set_footer(text='A more detailed response is being worked on.')
            else:
                if lookup not in MBTICore.mbti_types and target not in MBTICore.mbti_types:
                    item = 'Types'
                elif lookup not in MBTICore.mbti_types:
                    item = 'First type'
                else:
                    item = 'Second type'
                response = GenericResponse(f'{item} not found.').not_found()
        elif lookup in MBTICore.mbti_types:
            mbti_type = MBTICore.mbti_types[lookup]
            title, description = f'👥 {lookup.upper()}', make_paragraph(mbti_type)
            response = discord.Embed(color=0x734d5f, title=title, description=description)
            type_src = types_src + ''.join(mbti_type['stack'].split('-')[:2])
            response.set_footer(text=f'Sourced from: {type_src}')
        elif lookup in MBTICore.mbti_functions:
            mbti_function = MBTICore.mbti_functions[lookup]
            title, description = f'👥 {lookup.title()}', make_paragraph(mbti_function)
            response = discord.Embed(color=0x734d5f, title=title, description=description)
            response.set_footer(text=f'Sourced from: {funcs_src}')
        else:
            if len(lookup) == 4:
                item = 'Type'
            elif len(lookup) == 2:
                item = 'Function'
            else:
                item = 'Query'
            response = GenericResponse(f'{item} not found.').not_found()
    else:
        title, description = '👥 Myers-Briggs Type Indicator', make_paragraph(MBTICore.mbti_overview)
        response = discord.Embed(color=0x734d5f, title=title, description=description)
    await pld.msg.channel.send(embed=response)
