Unittests for python-otcclient
==============================

Prerequisites
-------------

On debian derived systems install the *python-nose* package. This
introduces no additional dependencies for end users as unit testing
is a developer task.

Currently tests require access to OTC and a working configuration in
*~/.otc/*

How to run tests
----------------

From the repository top level directory run:

	nosetests -w pytest

As usual you can increase verbosity with the *-v* command line option. *nose*
defaults to capturing *stdout* so any print output is invisible unless you tell
it not to.

	nosetests -v -s -w pytest
