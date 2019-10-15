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
from burpless.Indenter import CustomIndenter

from lark.indenter import Indenter


def test_indenter_customindenter():
    assert issubclass(CustomIndenter, Indenter)
    assert CustomIndenter.NL_type == '_NL'
    assert CustomIndenter.OPEN_PAREN_types == []
    assert CustomIndenter.CLOSE_PAREN_types == []
    assert CustomIndenter.INDENT_type == '_INDENT'
    assert CustomIndenter.DEDENT_type == '_DEDENT'
    assert CustomIndenter.tab_len == 8
