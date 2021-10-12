gnuplot_py3 -- A pipe-based interface to the gnuplot plotting program.

This was forked from Michael Haggerty's Gnuplot.py at Sourceforge.
The original Gnuplot.py home page is  http://gnuplot-py.sourceforge.net

Gnuplot.py has not been in development for a while and required a few changes
to be ported to Python 3.


Documentation
-------------

The quickest way to learn how to use gnuplot_py3 is to install it and
run the simple demonstration by typing `python demo.py', then look at
the demo.py file to see the commands that created the demo.  One of
the examples is probably similar to what you want to do.

Don't forget to read the Gnuplot.html, README.txt, and FAQ.txt files
in the Gnuplot.py distribution.

HTML documentation for the Python classes is included in the doc/
directory of the distribution and is also available online (follow
links from the home page).  This documentation is extracted
automatically from the package's docstrings using happydoc and should
be helpful though it is known to have some formatting problems.
Alternatively, you can look at the docstrings yourself by opening the
python files in an editor.

To get good use out of gnuplot_py3, you will want to know something
about gnuplot, for which a good source is the gnuplot help (run
gnuplot then type `help', or read it online at

    http://www.gnuplot.info/gnuplot.html

).

For a relatively thorough test of gnuplot_py3, type `python test.py'
which goes systematically through most gnuplot_py3 features.


Installation
------------

Quick instructions:

1. Download gnuplot_py3 from GitHub.

TODO
2. Extract the archive to a temporary directory.

3. Install by changing to the directory and typing "python setup.py
   install".

More information:

Obviously, you must have the gnuplot program if Gnuplot.py is to be of
any use to you.  Gnuplot can be obtained via
<http://www.gnuplot.info>.  You also need a copy of the numpy package, which
is available from the Scipy group at <http://www.scipy.org/Download>.

Gnuplot.py uses Python distutils
<http://www.python.org/doc/current/inst/inst.html> and can be
installed by untarring the package, changing into the top-level
directory, and typing "python setup.py install".  The Gnuplot.py
package is pure Python--no compilation is necessary.

Gnuplot_py3 is structured as a python package.  That means that it
installs itself as a subdirectory called `gnuplot' under a directory
of your python path (usually site-packages).  If you don't want to use
distutils you can just move the main gnuplot_py3 directory there and
rename it to "gnuplot".

There are some configuration options that can be set near the top of
the platform-dependent files gp-unix.py (Unix), gp_mac.py (Macintosh),
gp_macosx.py (Mac OS X), gp_win32.py (Windows), and gp_java.py
(Jython/Java).  (Obviously, you should change the file corresponding
to your platform.)  See the extensive comments in gp_unix.py for a
description of the meaning of each configuration variable.  Sensible
values are already chosen, so it is quite possible that you don't have
to change anything.

Import the main part of the package into your python programs using
`import gnuplot'.  Some other features can be found in the modules
gnuplot.funcutils and gnuplot.PlotItems.


Installation via RPM (for Linux/Unix)
-------------------------------------

TODO


Installation on Windows
-----------------------

TODO


Installation on the Macintosh
-----------------------------

That will not happen.


Assistance
----------

If you are having trouble installing or using gnuplot_py3, please check
the following sources for help:

1. Read the documentation!  For simple questions, start with the
   Gnuplot.html, README.txt, and FAQ.txt files in the distribution.
   For more detailed information, check the online class documentation
   at

       http://gnuplot-py.sourceforge.net/doc/

2. Check the mailing list archives.  Chances are that somebody has
   already asked a similar questions and you are one quick search away
   from the answer.  Information about the mailing list is available
   at

       http://lists.sourceforge.net/mailman/listinfo/gnuplot-py-users



Feedback
--------

I would love to have feedback from people letting me know whether they
find gnuplot_py3 useful.  And certainly let me know about any problems,
suggestions, or enhancements.



Compatibility
-------------

gnuplot_py3 has been tested with version 3.8 of gnuplot.

gnuplot_py3 is being developped under Windows 10; it should work
on Linux (Ubuntu) but this is still a TODO.

TODO
gnuplot_py3 should also work under Linux (Ubuntu).


License
-------

See the file LICENSE.txt for license info.  In brief, Gnuplot is LGPL.


Credits
-------

See CREDITS.txt for a list of people who have contributed code and/or
ideas to Gnuplot.py.  Thanks especially to Konrad Hinsen
<hinsen@ibs.ibs.fr>, who wrote the first, procedural interface version
of Gnuplot.py.


--
Joaquin Abian
