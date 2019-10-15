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
from burpless.App import App
from burpless.Cli import Cli
from burpless.Version import version

import click
from click.testing import CliRunner

from pytest import fixture


@fixture
def runner():
    return CliRunner()


def test_cli_parse(patch, runner):
    patch.object(click, 'echo')
    patch.object(App, 'parse')
    runner.invoke(Cli.parse, ['path'])
    App.parse.assert_called_with('path')
    click.echo.assert_called_with(App.parse().pretty())


def test_cli_version(patch, runner):
    patch.object(click, 'echo')
    runner.invoke(Cli.version, [])
    click.echo.assert_called_with(f'Burpless {version}')
