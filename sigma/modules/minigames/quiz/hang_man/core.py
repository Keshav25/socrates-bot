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

import secrets

alive, dead = '🔵', '🔴'
body_parts = {
    'head': ' Head',
    'torso': ' Torso',
    'larm': ' Left Arm',
    'rarm': ' Right Arm',
    'lleg': ' Left Leg',
    'rleg': ' Right Leg'
}


class Gallows(object):
    def __init__(self, word):
        """
        :param word:
        :type word: str
        """
        self.unused = list(body_parts.copy().keys())
        self.used = []
        self.word = word.lower()
        self.right_letters = []
        self.wrong_letters = []
        self.count = len(self.word)

    @property
    def victory(self):
        """
        :return:
        :rtype: bool
        """
        return not set(self.word) - set(self.right_letters)

    @property
    def dead(self):
        """
        :return:
        :rtype: bool
        """
        return not self.unused

    def use_part(self):
        """
        :return:
        """
        self.used.append(self.unused.pop(secrets.randbelow((len(self.unused)))))

    def make_gallows_man(self):
        """
        :return:
        :rtype: str
        """
        parts = []
        for name, part in body_parts.items():
            state = alive if name in self.unused else dead
            parts.append(state + part)
        return '\n'.join(parts)

    def make_word_space(self):
        """
        :return:
        :rtype: str
        """
        word_space = []
        for letter in self.word:
            if letter in self.right_letters:
                char = letter if word_space else letter.upper()
                word_space.append(char)
            else:
                word_space.append(r'\_\_')
        return ' '.join(word_space)
