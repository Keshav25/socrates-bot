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


class Cacher(object):
    def __init__(self):
        self.data = {}

    def get_cache(self, key: str or int):
        value = self.data.get(key)
        return value

    def set_cache(self, key: str or int, value):
        self.data.update({key: value})

    def del_cache(self, key: str or int):
        if key in self.data:
            self.data.pop(key)
