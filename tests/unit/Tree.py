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
from burpless.Tree import Tree

from lark.tree import Tree as LarkTree

from pytest import fixture


@fixture
def tree():
    return Tree('tree', [])


def test_tree():
    assert issubclass(Tree, LarkTree)


def test_tree_walk():
    node = Tree('node', [])
    assert Tree.walk(Tree('tree', [node]), 'node') == node


def test_tree__no_children():
    assert Tree.walk(Tree('tree', []), 'node') is None


def test_tree_walk__not_tree():
    assert Tree.walk(Tree('tree', ['node']), 'node') is None


def test_tree_child(tree):
    tree.children = ['child']
    assert tree.child(0) == 'child'


def test_tree_child__overflow(tree):
    assert tree.child(0) is None
