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
import os

from burpless.Burpless import Burpless
from burpless.Parser import Parser


def test_app_parse(patch):
    patch.object(io, 'open')
    patch.init(Parser)
    patch.object(Parser, 'parse')
    result = Burpless.parse('path')
    io.open.assert_called_with(os.path.join(os.getcwd(), 'path'), 'r')
    Parser.parse.assert_called_with(io.open().__enter__().read())
    assert result == Parser.parse()
