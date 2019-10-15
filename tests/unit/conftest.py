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
from pytest import fixture


@fixture
def magic(mocker):
    """
    Shorthand for mocker.MagicMock. It's magic!
    """
    return mocker.MagicMock


@fixture
def patch_none(mocker):
    """
    Makes patching to none simpler.
    """
    def patch_none(item, attribute):
        if type(attribute) == list:
            for method in attribute:
                mocker.patch.object(item, method, return_value=None)
        else:
            mocker.patch.object(item, attribute, return_value=None)
    return patch_none


@fixture
def patch_init(mocker):
    """
    Makes patching a class' constructor slightly easier
    """
    def patch_init(item):
        mocker.patch.object(item, '__init__', return_value=None)
    return patch_init


@fixture
def patch_many(mocker):
    """
    Makes patching many attributes of the same object simpler
    """
    def patch_many(item, attributes):
        for attribute in attributes:
            mocker.patch.object(item, attribute)
    return patch_many


@fixture
def patch(mocker, patch_none, patch_init, patch_many):
    mocker.patch.none = patch_none
    mocker.patch.init = patch_init
    mocker.patch.many = patch_many
    return mocker.patch


@fixture
def call_count():
    """
    Makes asserting a call count on the same module less repetitive.
    """
    def call_count(module, methods, count=1):
        for method in methods:
            assert getattr(module, method).call_count == count
    return call_count
