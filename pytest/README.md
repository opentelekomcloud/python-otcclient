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

Coverage
--------

The coverage plugin ca be used like this:

	nosetests --with-coverage -w pytest --cover-package otcclient
	  ...............
	  Name                              Stmts   Miss  Cover   Missing
	  ---------------------------------------------------------------
	  otcclient                             0      0   100%   
	  otcclient.core                        0      0   100%   
	  otcclient.core.OtcConfig            339    339     0%   7-524
	  otcclient.core.argmanager            19     19     0%   8-52
	  otcclient.core.configloader          90     90     0%   7-135
	  otcclient.core.otcpluginbase          9      9     0%   7-20
	  otcclient.core.pluginmanager         45     45     0%   7-60
	  otcclient.core.userconfigaction      69     69     0%   7-128
	  otcclient.plugins                     0      0   100%   
	  otcclient.plugins.ecs               558    558     0%   7-798
	  otcclient.utils                       0      0   100%   
	  otcclient.utils.utils_http           64     64     0%   7-85
	  otcclient.utils.utils_output         62     62     0%   6-86
	  otcclient.utils.utils_s3             84     84     0%   6-128
	  otcclient.utils.utils_templates      14     14     0%   6-30
	  ---------------------------------------------------------------
	  TOTAL                              1353   1353     0%   
	  ----------------------------------------------------------------------
	  Ran 16 tests in 11.909s

	  OK

