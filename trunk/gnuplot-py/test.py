#! /usr/bin/env python
# $Id$

"""Gnuplot_test.py -- Exercise the Gnuplot.py module.

Copyright (C) 1999 Michael Haggerty

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or (at
your option) any later version.  This program is distributed in the
hope that it will be useful, but WITHOUT ANY WARRANTY; without even
the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE.  See the GNU General Public License for more details; it is
available at <http://www.fsf.org/copyleft/gpl.html>, or by writing to
the Free Software Foundation, Inc., 59 Temple Place - Suite 330,
Boston, MA 02111-1307, USA.

"""

__version__ = '1.2'
__cvs_version__ = '$Revision$'

import math, time
import Numeric
from Numeric import *
import Gnuplot
gp = Gnuplot # abbreviation

def wait(str=None, prompt='Press return to show results...\n'):
    if str is not None:
        print str
    raw_input(prompt)


def main():
    """Exercise the Gnuplot module."""

    wait('Popping up a blank gnuplot window on your screen.')
    g = gp.Gnuplot()
    g.clear()

    # Make a temporary file:
    file1 = gp.TempFile() # will be deleted upon exit
    f = open(file1.filename, 'w')
    for x in arange(100)/5. - 10.:
        f.write('%s %s %s\n' % (x, math.cos(x), math.sin(x)))
    f.close()

    print '############### test Func ########################################'
    wait('Plot a gnuplot-generated function')
    g.plot(gp.Func('sin(x)'))

    wait('Set title and axis labels and try replot()')
    g.title('Title')
    g.xlabel('x')
    g.ylabel('y')
    g.replot()

    wait('Style linespoints')
    g.plot(gp.Func('sin(x)', with='linespoints'))
    wait('title=None')
    g.plot(gp.Func('sin(x)', title=None))
    wait('title="Sine of x"')
    g.plot(gp.Func('sin(x)', title='Sine of x'))

    print 'Change Func attributes after construction:'
    f = gp.Func('sin(x)')
    wait('Original')
    g.plot(f)
    wait('Style linespoints')
    f.set_option(with='linespoints')
    g.plot(f)
    wait('title=None')
    f.set_option(title=None)
    g.plot(f)
    wait('title="Sine of x"')
    f.set_option(title='Sine of x')
    g.plot(f)

    print '############### test File ########################################'
    wait('Generate a File from a filename')
    g.plot(gp.File(file1.filename))
    wait('Generate a File given a TempFile object')
    g.plot(gp.File(file1))

    wait('Style lines')
    g.plot(gp.File(file1.filename, with='lines'))
    wait('using=1, using=(1,)')
    g.plot(gp.File(file1.filename, using=1, with='lines'),
           gp.File(file1.filename, using=(1,), with='points'))
    wait('using=(1,2), using="1:3"')
    g.plot(gp.File(file1.filename, using=(1,2)),
           gp.File(file1.filename, using='1:3'))
    wait('title=None')
    g.plot(gp.File(file1.filename, title=None))
    wait('title="title"')
    g.plot(gp.File(file1.filename, title='title'))

    print 'Change File attributes after construction:'
    f = gp.File(file1.filename)
    wait('Original')
    g.plot(f)
    wait('Style linespoints')
    f.set_option(with='linespoints')
    g.plot(f)
    wait('using=(1,3)')
    f.set_option(using=(1,3))
    g.plot(f)
    wait('title=None')
    f.set_option(title=None)
    g.plot(f)

    print '############### test Data ########################################'
    x = arange(100)/5. - 10.
    y1 = Numeric.cos(x)
    y2 = Numeric.sin(x)
    d = Numeric.transpose((x,y1,y2))

    wait('Plot Data, specified column-by-column')
    g.plot(gp.Data(x,y2, inline=0))
    wait('Same thing, inline data')
    g.plot(gp.Data(x,y2, inline=1))

    wait('Plot Data, specified by an array')
    g.plot(gp.Data(d, inline=0))
    wait('Same thing, inline data')
    g.plot(gp.Data(d, inline=1))
    wait('with="lp 4 4"')
    g.plot(gp.Data(d, with='lp 4 4'))
    wait('cols=0')
    g.plot(gp.Data(d, cols=0))
    wait('cols=(0,1), cols=(0,2)')
    g.plot(gp.Data(d, cols=(0,1), inline=0),
           gp.Data(d, cols=(0,2), inline=0))
    wait('Same thing, inline data')
    g.plot(gp.Data(d, cols=(0,1), inline=1),
           gp.Data(d, cols=(0,2), inline=1))
    wait('Change title and replot()')
    g.title('New title')
    g.replot()
    wait('title=None')
    g.plot(gp.Data(d, title=None))
    wait('title="Cosine of x"')
    g.plot(gp.Data(d, title='Cosine of x'))

    print '############### test hardcopy ####################################'
    print '******** Generating postscript file "gp_test.ps" ********'
    g.hardcopy('gp_test.ps', enhanced=1, color=1)

    print '############### test shortcuts ###################################'
    wait('plot Func and Data using shortcuts')
    g.plot('sin(x)', d)

    print '############### test splot #######################################'
    g.splot(gp.Data(d, with='linesp', inline=0))
    wait('Same thing, inline data')
    g.splot(gp.Data(d, with='linesp', inline=1))

    print '############### test GridData and GridFunc #######################'
    # set up x and y values at which the function will be tabulated:
    x = arange(35)/2.0
    y = arange(30)/10.0 - 1.5
    # Make a 2-d array containing a function of x and y.  First create
    # xm and ym which contain the x and y values in a matrix form that
    # can be `broadcast' into a matrix of the appropriate shape:
    xm = x[:,NewAxis]
    ym = y[NewAxis,:]
    m = (sin(xm) + 0.1*xm) - ym**2
    wait('a function of two variables from a GridData file')
    g('set parametric')
    g('set data style lines')
    g('set hidden')
    g('set contour base')
    g.xlabel('x')
    g.ylabel('y')
    g.splot(gp.GridData(m,x,y, binary=0, inline=0))
    wait('Same thing, inline data')
    g.splot(gp.GridData(m,x,y, binary=0, inline=1))

    wait('The same thing using binary mode')
    g.splot(gp.GridData(m,x,y, binary=1))

    wait('The same thing using GridFunc to tabulate function')
    g.splot(gp.GridFunc(lambda x,y: sin(x) + 0.1*x - y**2, x,y))

    wait('Use GridFunc in ufunc mode')
    g.splot(gp.GridFunc(lambda x,y: sin(x) + 0.1*x - y**2, x,y,
                        ufunc=1, binary=1))

    wait('And now rotate it a bit')
    for view in range(35,70,5):
        g('set view 60, %d' % view)
        g.replot()
        time.sleep(1.0)

    wait(prompt='Press return to end the test.\n')


# when executed or imported, just run main():
main()
