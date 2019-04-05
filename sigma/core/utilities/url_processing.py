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

import json

import aiohttp


async def aioget(url, as_json=False):
    """
    Asynchronously fetches a URL.
    :param url: The URL to fetch.
    :type url: str
    :param as_json: Whether or not to parse the response into JSON.
    :type as_json: bool
    :return:
    :rtype: str or dict
    """
    async with aiohttp.ClientSession() as aio_client:
        async with aio_client.get(url) as aio_session:
            response = await aio_session.text()
            if as_json:
                response = json.loads(response)
    return response
