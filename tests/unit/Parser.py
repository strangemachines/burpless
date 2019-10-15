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

from burpless.Grammar import Grammar
from burpless.Indenter import CustomIndenter
from burpless.Parser import Parser
from burpless.Transformer import Transformer

from lark import Lark

from pytest import fixture


@fixture
def parser():
    return Parser()


def test_parser_init(parser):
    assert parser.algo == 'lalr'
    assert parser.ebnf_file is None


def test_parser_init__keyargs():
    parser = Parser('algo', 'ebnf')
    assert parser.algo == 'algo'
    assert parser.ebnf_file == 'ebnf'


def test_parser_indenter(patch):
    patch.init(CustomIndenter)
    result = Parser.indenter()
    assert isinstance(result, CustomIndenter)


def test_parser_transformer(patch):
    patch.init(Transformer)
    result = Parser.transformer()
    assert isinstance(result, Transformer)


def test_parser_default_ebnf(patch):
    patch.many(os.path, ['dirname', 'join', 'realpath'])
    result = Parser.default_ebnf()
    os.path.join.assert_called_with(os.path.dirname(), '..', 'grammar',
                                    'grammar.ebnf')
    os.path.realpath.assert_called_with(os.path.join())
    assert result == os.path.realpath()


def test_parser_lark(patch, parser):
    patch.init(Lark)
    patch.object(Grammar, 'grammar')
    patch.many(Parser, ['default_ebnf', 'indenter'])
    result = parser.lark()
    Grammar.grammar.assert_called_with(Parser.default_ebnf())
    Lark.__init__.assert_called_with(Grammar.grammar(), parser='lalr',
                                     postlex=Parser.indenter())
    assert isinstance(result, Lark)


def test_parser_lark__ebnf(patch, parser):
    patch.init(Lark)
    patch.object(Grammar, 'grammar')
    patch.many(Parser, ['default_ebnf', 'indenter'])
    parser.ebnf_file = 'ebnf'
    parser.lark()
    Grammar.grammar.assert_called_with('ebnf')


def test_parser_parse(patch, parser):
    patch.many(Parser, ['lark', 'transformer'])
    result = parser.parse('source')
    Parser.lark().parse.assert_called_with('source\n')
    Parser.transformer().transform.assert_called_with(Parser.lark().parse())
    assert result == Parser.transformer().transform()
