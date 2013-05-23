#
# update-header - Updates the header comment in source files
# Copyright (C) 2013  Lorenzo Villani
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


import updateheader
import unittest

try:
    # Python 2.x
    from StringIO import StringIO
except ImportError:
    # Python 3.x
    from io import StringIO


#
# Test case
#

class TestUpdateHeader(unittest.TestCase):

    def test_empty_input(self):
        self.t(EMPTY_OUTPUT, EMPTY)

    def test_shebang_input(self):
        self.t(SHEBANG_OUTPUT, SHEBANG)

    def test_existing_header(self):
        self.t(EXISTING_HEADER_OUTPUT, EXISTING_HEADER)

    def t(self, expected, input_string):
        input_stream = StringIO(input_string)
        header_stream = StringIO(HEADER)
        output_stream = StringIO()

        updateheader.update_header(input_stream, header_stream, output_stream)

        self.assertEqual(expected, output_stream.getvalue())


#
# Test inputs/outputs
#

HEADER = """
test - A test program

Copyright (c) 2013 Lorenzo Villani"""

# ---------------------------------------------

EMPTY = ""
EMPTY_OUTPUT = """#
# test - A test program
#
# Copyright (c) 2013 Lorenzo Villani"""

# ---------------------------------------------

SHEBANG = """#!/usr/bin/python
"""
SHEBANG_OUTPUT = """#!/usr/bin/python
#
# test - A test program
#
# Copyright (c) 2013 Lorenzo Villani"""

# ---------------------------------------------

EXISTING_HEADER = """#!/usr/bin/python
#
# old_test - An old test header
#
# Copyright (c) 2013 Lorenzo Villani"""
EXISTING_HEADER_OUTPUT = """#!/usr/bin/python
#
# test - A test program
#
# Copyright (c) 2013 Lorenzo Villani"""
