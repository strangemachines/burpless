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
import os

from lark import Lark

from .Grammar import Grammar
from .Indenter import CustomIndenter
from .Transformer import Transformer


class Parser:
    def __init__(self, algo='lalr', ebnf_file=None):
        self.algo = algo
        self.ebnf_file = ebnf_file

    @staticmethod
    def indenter():
        """
        Initialize the indenter
        """
        return CustomIndenter()

    @staticmethod
    def transformer():
        """
        Initialize the transformer
        """
        return Transformer()

    @staticmethod
    def default_ebnf():
        folder = os.path.dirname(__file__)
        path = os.path.join(folder, '..', 'grammar', 'grammar.ebnf')
        return os.path.realpath(path)

    def lark(self):
        if self.ebnf_file is None:
            self.ebnf_file = self.default_ebnf()
        grammar = Grammar.grammar(self.ebnf_file)
        return Lark(grammar, parser=self.algo, postlex=self.indenter())

    def parse(self, source):
        source = '{}\n'.format(source)
        lark = self.lark()
        tree = lark.parse(source)
        return self.transformer().transform(tree)
