'''
Copyright (C) cgtinker, cgtinker.com, hello@cgtinker.com

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
'''

import json


def to_json(data, path):
    with open(path, 'w', encoding='utf-8') as f:
        j = json.dumps(data, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ':'))
        f.write(j)
    return j


def from_json(path):
    with open(path) as f:
        j = json.load(f)
    return j
