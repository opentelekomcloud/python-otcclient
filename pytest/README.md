Unittests for python-otcclient
==============================

How to run tests
----------------

From the repository top level directory run:

	nosetests -w pytest

As usual you can increase verbosity with the '-v' command line option. 'nose'
defaults to capturing stdout so any print output is invisible unless you tell
it not to.

	nosetests -v -s -w pytest
