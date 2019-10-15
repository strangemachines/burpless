#   Copyright (C) 2019  Strangemachines
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
# -*- coding: utf-8 -*-
import io

from burpless.Grammar import Grammar


def test_grammar_open(patch):
    patch.object(io, 'open')
    result = Grammar.grammar('file')
    io.open.assert_called_with('file')
    assert result == io.open().__enter__().read()
