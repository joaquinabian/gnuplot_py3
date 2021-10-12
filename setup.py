#! /usr/bin/env python

# Copyright (C) 2021 Joaquin Abian <gatoygata2@gmail.com>
# Copyright (C) 2001-2003 Michael Haggerty <mhagger@alum.mit.edu>
#
# This file is licensed under the GNU Lesser General Public License
# (LGPL).  See LICENSE.txt for details.

"""Setup script for the gnuplot module distribution.

"""

from distutils.core import setup

# Get the version number from the __init__ file:
from __init__ import __version__

long_description = """\
gnuplot_py3 is a Python package that allows you to create graphs from
within Python 3 using the gnuplot plotting program.
Forked from Michael Haggerty's Gnuplot.py at Sourceforge.
"""

setup(
    # Distribution meta-data
    name='gnuplot_py3',
    version=__version__,
    description='A Python 3 interface to the gnuplot plotting program.',
    long_description=long_description,
    author='Joaquin Abian',
    author_email='gatoygata2@gmail.com',
    url='https://github.com/joaquinabian/gnuplot_py3',
    license='LGPL',

    # Description of the package in the distribution
    package_dir={'Gnuplot': '.'},
    packages=['Gnuplot'],
    )
