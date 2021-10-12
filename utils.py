#! /usr/bin/env python

# Copyright (C) 2021 Joaquin Abian <gatoygata2@gmail.com>
# Copyright (C) 1998-2003 Michael Haggerty <mhagger@alum.mit.edu>
#
# This file is licensed under the GNU Lesser General Public License
# (LGPL).  See LICENSE.txt for details.

"""utils.py -- Utility functions used by gnuplot_py3.

This module contains utility functions used by gnuplot_py3 which aren't
particularly gnuplot-related.

"""

import numpy

def float_array(m):
    """Return the argument as a numpy array of type at least 'Float32'.

    Leave 'Float64' unchanged, but upcast all other types to
    'Float32'.  Allow also for the possibility that the argument is a
    python native type that can be converted to a numpy array using
    'numpy.asarray()', but in that case don't worry about
    downcasting to single-precision float.

    """

    try:
        # Try Float32 (this will refuse to downcast)
        return numpy.asarray(m, numpy.float32)
    except TypeError:
        # That failure might have been because the input array was
        # of a wider data type than float32; try to convert to the
        # largest floating-point type available:
        # NOTE TBD: I'm not sure float_ is the best data-type for this...
        try:
            return numpy.asarray(m, numpy.float_)
        except TypeError:
            # TBD: Need better handling of this error!
            print("Fatal: array dimensions not equal!")
            return None

def write_array(f, lols,
                item_sep=' ',
                nest_prefix='', nest_suffix='\n', nest_sep=''):
    """Write an array of arbitrary dimension to a file.

    A general recursive array writer from a list of lists (lols).
    The last four parameters allow a great deal of freedom in choosing the
    output format of the array.
    The defaults for those parameters give output that is gnuplot-readable.
    But using '(",", "{", "}", ",\n")' would output an array in a format
    that Mathematica could read.
    'item_sep' should not contain '%' (or if it does, it should be escaped to
    '%%') since it is put into a format string.

    The default 2-d file organization::

        lols[0,0] lols[0,1] ...
        lols[1,0] lols[1,1] ...

    The 3-d format::

        lols[0,0,0] lols[0,0,1] ...
        lols[0,1,0] lols[0,1,1] ...

        lols[1,0,0] lols[1,0,1] ...
        lols[1,1,0] lols[1,1,1] ...

    """

    if len(lols.shape) == 1:
        (columns,) = lols.shape
        assert columns > 0
        fmt = item_sep.join(['%s'] * columns)
        f.write(nest_prefix)
        f.write(fmt % tuple(lols.tolist()))
        f.write(nest_suffix)
    elif len(lols.shape) == 2:
        # This case could be done with recursion, but `unroll' for
        # efficiency.
        (points, columns) = lols.shape
        assert points > 0 and columns > 0
        fmt = item_sep.join(['%s'] * columns)
        f.write(nest_prefix + nest_prefix)
        f.write(fmt % tuple(lols[0].tolist()))
        f.write(nest_suffix)
        for point in lols[1:]:
            f.write(nest_sep + nest_prefix)
            f.write(fmt % tuple(point.tolist()))
            f.write(nest_suffix)
        f.write(nest_suffix)
    else:
        # Use recursion for three or more dimensions:
        assert lols.shape[0] > 0
        f.write(nest_prefix)
        write_array(f, lols[0],
                    item_sep, nest_prefix, nest_suffix, nest_sep)
        for subset in lols[1:]:
            f.write(nest_sep)
            write_array(f, subset,
                        item_sep, nest_prefix, nest_suffix, nest_sep)
