#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-or-later
u"""
    headers
    ~~~~~~~

    Implementation of the ``headers`` reST-directive.

    :copyright:  Copyright (C) 2024 Nicolas Bourdaud
    :license:    AGPL-3.0-or-later; see LICENSE for details.

    For user documentation see :ref:`header-directive`.
"""

# ==============================================================================
# imports
# ==============================================================================

from docutils.parsers.rst import Directive, directives
from docutils.nodes import PreBibliographic, Element

__version__  = '1.0'

# ==============================================================================
def setup(app): # pylint: disable=missing-docstring
# ==============================================================================

    app.add_node(
        HeadersHint,
        html = (visit_header_hints, depart_header_hints),
    )
    app.add_directive("headers", Headers)
    return dict(
        version = __version__,
        parallel_read_safe = True,
        parallel_write_safe = True,
    )


# ==============================================================================
class HeadersHint(PreBibliographic, Element):
# ==============================================================================
    """Node indicating which headers must be used"""


# ==============================================================================
class Headers(Directive):
# ==============================================================================
    u"""Headers (``headers``) directive"""

    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True

    def run(self):
        return [HeadersHint(headers=self.arguments[0].split())]


# ==============================================================================
# common globals
# ==============================================================================
def visit_header_hints(self, node):
    pass

def depart_header_hints(self, node):
    pass
