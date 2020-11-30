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

import arrow
import discord

from sigma.core.mechanics.incident import get_incident_core
from sigma.core.utilities.data_processing import convert_to_seconds, get_broad_target, user_avatar
from sigma.core.utilities.event_logging import log_event
from sigma.core.utilities.generic_responses import denied, error, ok
from sigma.core.utilities.permission_processing import hierarchy_permit


def generate_log_embed(message, target, reason):
    """

    :param message:
    :type message: discord.Message
    :param target:
    :type target: discord.Member
    :param reason:
    :type reason: str
    :return:
    :rtype: discord.Embed
    """
    log_embed = discord.Embed(color=0x696969, timestamp=arrow.utcnow().datetime)
    log_embed.set_author(name='A Member Has Been Hard Muted', icon_url=user_avatar(target))
    log_embed.add_field(name='🔇 Muted User',
                        value=f'{target.mention}\n{target.name}#{target.discriminator}')
    author = message.author
    log_embed.add_field(name='🛡 Responsible',
                        value=f'{author.mention}\n{author.name}#{author.discriminator}')
    if reason:
        log_embed.add_field(name='📄 Reason', value=f"```\n{reason}\n```", inline=False)
    log_embed.set_footer(text=f'User ID {target.id}')
    return log_embed


async def make_incident(db, gld, ath, trg, reason):
    """

    :param db:
    :type db: sigma.core.mechanics.database.Database
    :param gld:
    :type gld: discord.Guild
    :param ath:
    :type ath: discord.Member
    :param trg:
    :type trg: discord.Member
    :param reason:
    :type reason: str
    """
    icore = get_incident_core(db)
    inc = icore.generate('hardmute')
    inc.set_location(gld)
    inc.set_moderator(ath)
    inc.set_target(trg)
    inc.set_reason(reason)
    await icore.save(inc)
    await icore.report(gld, inc.to_embed('🔇', 0x696969))


async def hardmute(cmd, pld):
    """
    :param cmd: The command object referenced in the command.
    :type cmd: sigma.core.mechanics.command.SigmaCommand
    :param pld: The payload with execution data and details.
    :type pld: sigma.core.mechanics.payload.CommandPayload
    """
    if pld.msg.author.permissions_in(pld.msg.channel).manage_channels:
        target = get_broad_target(pld)
        if target:
            hierarchy_me = hierarchy_permit(pld.msg.guild.me, target)
            if hierarchy_me:
                hierarchy_auth = hierarchy_permit(pld.msg.author, target)
                if hierarchy_auth:
                    ongoing = discord.Embed(color=0x696969, title='⛓ Editing permissions...')
                    ongoing_msg = await pld.msg.channel.send(embed=ongoing)
                    timed = pld.args[-1].startswith('--time=')
                    try:
                        now = arrow.utcnow().int_timestamp
                        endstamp = now + convert_to_seconds(pld.args[-1].split('=')[-1]) if timed else None
                    except (LookupError, ValueError):
                        err_response = error('Please use the format HH:MM:SS.')
                        await pld.msg.channel.send(embed=err_response)
                        return
                    for channel in pld.msg.guild.channels:
                        if isinstance(channel, discord.TextChannel) or isinstance(channel, discord.CategoryChannel):
                            try:
                                await channel.set_permissions(target, send_messages=False, add_reactions=False)
                            except (discord.Forbidden, discord.NotFound):
                                pass
                    try:
                        await ongoing_msg.delete()
                    except discord.NotFound:
                        pass
                    rarg = pld.args[1:-1] if timed else pld.args[1:] if pld.args[1:] else None
                    reason = ' '.join(rarg) if rarg else None
                    await make_incident(cmd.db, pld.msg.guild, pld.msg.author, target, reason)
                    log_embed = generate_log_embed(pld.msg, target, reason)
                    await log_event(cmd.bot, pld.settings, log_embed, 'log_mutes')
                    response = ok(f'{target.display_name} has been hard-muted.')
                    guild_icon = str(pld.msg.guild.icon_url) if pld.msg.guild.icon_url else discord.Embed.Empty
                    to_target_title = '🔇 You have been hard-muted.'
                    to_target = discord.Embed(color=0x696969)
                    to_target.add_field(name=to_target_title, value=f'Reason: {reason}')
                    to_target.set_footer(text=f'On: {pld.msg.guild.name}', icon_url=guild_icon)
                    try:
                        await target.send(embed=to_target)
                    except (discord.Forbidden, discord.HTTPException):
                        pass
                    if endstamp:
                        doc_data = {'server_id': pld.msg.guild.id, 'user_id': target.id, 'time': endstamp}
                        await cmd.db[cmd.db.db_nam].HardmuteClockworkDocs.insert_one(doc_data)
                else:
                    response = error('That user is equal or above you.')
            else:
                response = error('I can\'t mute a user equal or above me.')
        else:
            response = error('No user targeted.')
    else:
        response = denied('Access Denied. Manage Channels needed.')
    await pld.msg.channel.send(embed=response)
