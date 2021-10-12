#! /usr/bin/env python

# Copyright (C) 2021 Joaquin Abian <gatoygata2@gmail.com>
# Copyright (C) 1999-2003 Michael Haggerty <mhagger@alum.mit.edu>
#
# This file is licensed under the GNU Lesser General Public License
# (LGPL).  See LICENSE.txt for details.

"""test.py -- Exercise the Gnuplot.py module.

This module is not meant to be a flashy demonstration; rather it is a
thorough test of many combinations of Gnuplot.py features.

"""

import os, time
import math, tempfile
import numpy as np

try:
    import gnuplot, gnuplot.plotitems, gnuplot.funcutils
except ImportError:
    # kludge in case Gnuplot hasn't been installed as a module yet:
    import __init__
    gnuplot = __init__
    import plotitems
    gnuplot.plotitems = plotitems
    import funcutils
    gnuplot.funcutils = funcutils


def wait(msg=None, prompt='Press return to show results...\n'):
    if msg:
        print(msg)
    input(prompt)


def main():
    """Exercise the Gnuplot module."""

    print (
        'This program exercises many of the features of gnuplot_py3.  The\n'
        'commands that are actually sent to gnuplot are printed for your\n'
        'enjoyment.'
        )

    wait('Popping up a blank gnuplot window on your screen.')
    g = gnuplot.Gnuplot(debug=1)
    g.clear()

    # Make two temporary files:
    if hasattr(tempfile, 'mkstemp'):
        (fd, filename1,) = tempfile.mkstemp(text=1)
        f = os.fdopen(fd, 'w')
        (fd, filename2,) = tempfile.mkstemp(text=1)
    else:
        filename1 = tempfile.mktemp()
        f = open(filename1, 'w')
        filename2 = tempfile.mktemp()
    try:
        for x in np.arange(100) / 5 - 10:
            f.write('%s %s %s\n' % (x, math.cos(x), math.sin(x)))
        f.close()

        print('############### test Func ###################################')
        wait('Plot a gnuplot-generated function')
        g.plot(gnuplot.Func('sin(x)'))

        wait('Set title and axis labels and try replot()')
        g.title('Title')
        g.xlabel('x')
        g.ylabel('y')
        g.replot()

        wait('Style linespoints')
        g.plot(gnuplot.Func('sin(x)', with_='linespoints'))

        wait('title=None')
        g.plot(gnuplot.Func('sin(x)', title=None))

        wait('title="Sine of x"')
        g.plot(gnuplot.Func('sin(x)', title='Sine of x'))

        wait('axes=x2y2')
        g.plot(gnuplot.Func('sin(x)', axes='x2y2', title='Sine of x'))
        print('Change Func attributes after construction:')

        wait('Original')
        f = gnuplot.Func('sin(x)')
        g.plot(f)

        wait('Style linespoints')
        f.set_option(with_='linespoints')
        g.plot(f)

        wait('title=None')
        f.set_option(title=None)
        g.plot(f)

        wait('title="Sine of x"')
        f.set_option(title='Sine of x')
        g.plot(f)

        wait('axes=x2y2')
        f.set_option(axes='x2y2')
        g.plot(f)

        print('############### test File ###################################')
        wait('Generate a File from a filename')
        g.plot(gnuplot.File(filename1))

        wait('Style lines')
        g.plot(gnuplot.File(filename1, with_='lines'))

        wait('using=1, using=(1,)')
        g.plot(gnuplot.File(filename1, using=1, with_='lines'),
               gnuplot.File(filename1, using=(1,), with_='points'))
        
        wait('using=(1,2), using="1:3"')
        g.plot(gnuplot.File(filename1, using=(1,2)),
               gnuplot.File(filename1, using='1:3'))

        wait('every=5, every=(5,)')
        g.plot(gnuplot.File(filename1, every=5, with_='lines'),
               gnuplot.File(filename1, every=(5,), with_='points'))

        wait('every=(10,None,0), every="10::5"')
        g.plot(gnuplot.File(filename1, with_='lines'),
               gnuplot.File(filename1, every=(10, None, 0)),
               gnuplot.File(filename1, every='10::5'))

        wait('title=None')
        g.plot(gnuplot.File(filename1, title=None))

        wait('title="title"')
        g.plot(gnuplot.File(filename1, title='title'))

        print('Change File attributes after construction:')
        f = gnuplot.File(filename1)
        wait('Original')
        g.plot(f)
        wait('Style linespoints')
        f.set_option(with_='linespoints')
        g.plot(f)
        wait('using=(1,3)')
        f.set_option(using=(1,3))
        g.plot(f)
        wait('title=None')
        f.set_option(title=None)
        g.plot(f)

        print('############### test Data ###################################')
        x = np.arange(100) / 5 - 10
        y1 = np.cos(x)
        y2 = np.sin(x)
        d = np.transpose((x, y1, y2))

        wait('Plot Data against its index')
        g.plot(gnuplot.Data(y2, inline=0))

        wait('Plot Data, specified column-by-column')
        g.plot(gnuplot.Data(x,y2, inline=0))

        wait('Same thing, saved to a file')
        gnuplot.Data(x,y2, inline=0, filename=filename1)
        g.plot(gnuplot.File(filename1))

        wait('Same thing, inline data')
        g.plot(gnuplot.Data(x,y2, inline=1))

        wait('Plot Data, specified by an array')
        g.plot(gnuplot.Data(d, inline=0))
        wait('Same thing, saved to a file')
        gnuplot.Data(d, inline=0, filename=filename1)
        g.plot(gnuplot.File(filename1))

        wait('Same thing, inline data')
        g.plot(gnuplot.Data(d, inline=1))

        wait('with_="lp lt 4 lw 4"')
        g.plot(gnuplot.Data(d, with_='lp lt 4 lw 4'))

        wait('cols=0')
        g.plot(gnuplot.Data(d, cols=0))

        wait('cols=(0,1), cols=(0,2)')
        g.plot(gnuplot.Data(d, cols=(0,1), inline=0),
               gnuplot.Data(d, cols=(0,2), inline=0))

        wait('Same thing, saved to files')
        gnuplot.Data(d, cols=(0,1), inline=0, filename=filename1)
        gnuplot.Data(d, cols=(0,2), inline=0, filename=filename2)
        g.plot(gnuplot.File(filename1), gnuplot.File(filename2))

        wait('Same thing, inline data')
        g.plot(gnuplot.Data(d, cols=(0,1), inline=1),
               gnuplot.Data(d, cols=(0,2), inline=1))

        wait('Change title and replot()')
        g.title('New title')
        g.replot()

        wait('title=None')
        g.plot(gnuplot.Data(d, title=None))

        wait('title="Cosine of x"')
        g.plot(gnuplot.Data(d, title='Cosine of x'))

        print('############### test compute_Data ###########################')
        x = np.arange(100) / 5 - 10

        wait('Plot Data, computed by Gnuplot.py')
        g.plot(
            gnuplot.funcutils.compute_Data(x, lambda x: math.cos(x), inline=0)
            )

        wait('Same thing, saved to a file')
        gnuplot.funcutils.compute_Data(
            x, lambda x: math.cos(x), inline=0, filename=filename1
            )
        g.plot(gnuplot.File(filename1))

        wait('Same thing, inline data')
        g.plot(gnuplot.funcutils.compute_Data(x, math.cos, inline=1))

        wait('with_="lp lt 4 lw 4"')
        g.plot(gnuplot.funcutils.compute_Data(x, math.cos, with_='lp lt 4 lw 4'))

        print('############### test hardcopy ###############################')
        print('******** Generating postscript file "gp_test.ps" ********')
        g.plot(gnuplot.Func('cos(0.5*x*x)', with_='linespoints lt 2 lw 2',
                       title='cos(0.5*x^2)'))
        g.hardcopy('gp_test.ps')

        wait('Testing hardcopy options: mode="eps"')
        g.hardcopy('gp_test.ps', mode='eps')

        wait('Testing hardcopy options: mode="landscape"')
        g.hardcopy('gp_test.ps', mode='landscape')

        wait('Testing hardcopy options: mode="portrait"')
        g.hardcopy('gp_test.ps', mode='portrait')

        wait('Testing hardcopy options: eps=1')
        g.hardcopy('gp_test.ps', eps=1)

        wait('Testing hardcopy options: mode="default"')
        g.hardcopy('gp_test.ps', mode='default')

        wait('Testing hardcopy options: enhanced=1')
        g.hardcopy('gp_test.ps', enhanced=1)

        wait('Testing hardcopy options: enhanced=0')
        g.hardcopy('gp_test.ps', enhanced=0)

        wait('Testing hardcopy options: color=1')
        g.hardcopy('gp_test.ps', color=1)
        # For some reason,
        #    g.hardcopy('gp_test.ps', color=0, solid=1)
        # doesn't work here (it doesn't activate the solid option), even
        # though the command sent to gnuplot looks correct.  I'll
        # tentatively conclude that it is a gnuplot bug. ###
        wait('Testing hardcopy options: color=0')
        g.hardcopy('gp_test.ps', color=0)

        wait('Testing hardcopy options: solid=1')
        g.hardcopy('gp_test.ps', solid=1)

        wait('Testing hardcopy options: duplexing="duplex"')
        g.hardcopy('gp_test.ps', solid=0, duplexing='duplex')

        wait('Testing hardcopy options: duplexing="defaultplex"')
        g.hardcopy('gp_test.ps', duplexing='defaultplex')

        wait('Testing hardcopy options: fontname="Times-Italic"')
        g.hardcopy('gp_test.ps', fontname='Times-Italic')

        wait('Testing hardcopy options: fontsize=20')
        g.hardcopy('gp_test.ps', fontsize=20)

        print('******** Generating svg file "gp_test.svg" ********')
        wait()
        g.plot(gnuplot.Func('cos(0.5*x*x)', with_='linespoints lt 2 lw 2',
                       title='cos(0.5*x^2)'))
        g.hardcopy('gp_test.svg', terminal='svg')

        wait('Testing hardcopy svg options: enhanced')
        g.hardcopy('gp_test.ps', terminal='svg', enhanced='1')


        print('############### test shortcuts ##############################')
        wait('plot Func and Data using shortcuts')
        g.plot('sin(x)', d)

        print('############### test splot ##################################')
        wait('a 3-d curve')
        g.splot(gnuplot.Data(d, with_='linesp', inline=0))

        wait('Same thing, saved to a file')
        gnuplot.Data(d, inline=0, filename=filename1)
        g.splot(gnuplot.File(filename1, with_='linesp'))

        wait('Same thing, inline data')
        g.splot(gnuplot.Data(d, with_='linesp', inline=1))

        print('############### test GridData and compute_GridData ##########')
        # set up x and y values at which the function will be tabulated:
        x = np.arange(35) / 2
        y = np.arange(30) / 10 - 1.5
        # Make a 2-d array containing a function of x and y.  First create
        # xm and ym which contain the x and y values in a matrix form that
        # can be `broadcast' into a matrix of the appropriate shape:
        xm = x[:, np.newaxis]
        ym = y[np.newaxis, :]
        m = (np.sin(xm) + 0.1 * xm) - ym**2

        wait('a function of two variables from a GridData file')
        g('set parametric')
        g('set style data lines')
        g('set hidden')
        g('set contour base')
        g.xlabel('x')
        g.ylabel('y')
        data = gnuplot.GridData(m, x, y, binary=0, inline=0)
        g.splot(data)

        wait('Same thing, saved to a file')
        gnuplot.GridData(m,x,y, binary=0, inline=0, filename=filename1)
        g.splot(gnuplot.File(filename1, binary=0))

        wait('Same thing, inline data')
        g.splot(gnuplot.GridData(m,x,y, binary=0, inline=1))

        wait('The same thing using binary mode')
        g.splot(gnuplot.GridData(m,x,y, binary=1))

        wait('Same thing, using binary mode and an intermediate file')
        gnuplot.GridData(m,x,y, binary=1, filename=filename1)
        g.splot(gnuplot.File(filename1, binary=1))

        wait('The same thing using compute_GridData to tabulate function')
        g.splot(gnuplot.funcutils.compute_GridData(
            x,y, lambda x,y: math.sin(x) + 0.1*x - y**2,
            ))

        wait('Same thing, with an intermediate file')
        gnuplot.funcutils.compute_GridData(
            x,y, lambda x,y: math.sin(x) + 0.1*x - y**2,
            filename=filename1)
        g.splot(gnuplot.File(filename1, binary=1))

        wait('Use compute_GridData in ufunc and binary mode')
        g.splot(gnuplot.funcutils.compute_GridData(
            x,y, lambda x,y: np.sin(x) + 0.1*x - y**2,
            ufunc=1, binary=1,
            ))
        wait('Same thing, with an intermediate file')
        gnuplot.funcutils.compute_GridData(
            x,y, lambda x,y: np.sin(x) + 0.1*x - y**2,
            ufunc=1, binary=1,
            filename=filename1)
        g.splot(gnuplot.File(filename1, binary=1))

        wait('And now rotate it a bit')
        for view in range(35, 70, 5):
            g('set view 60, %d' % view)
            g.replot()
            time.sleep(1.0)

        wait(prompt='Press return to end the test.\n')
    finally:
        os.unlink(filename1)
        os.unlink(filename2)


# when executed, just run main():
if __name__ == '__main__':
    main()
