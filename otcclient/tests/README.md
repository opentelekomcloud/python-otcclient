OTC Testsuite
=============

The OTC testsuite is a set of scripts that tests and verifys a range
of OTC functions that are exposed by means of the Python OTC tools. It
is easily extendable and generates an summary report as well as more
detailed protocols of the outcome of the single probes.

Installation
------------

The testsuite comes as part of the Python OTC tools, but can exist
independently. All necessary files are in the `otcclient/tests`
subfolder. If installed independently, it requires the Python OTC
tools installed and included in the `PATH`.

Configuration and Running a Test
--------------------------------

The toplevel `do_tests.sh` script requires no arguments and can be
called from everywhere. For your convenience the Python OTC tools have
a `Makefile` in the main folder that has a `test` target, so `make
test` initiates a full testrun.

The script briefly reports its progress while it executes. For more
details see the report that is generated with a unique timestamp in
the `reports` subfolder by default. You can configure the directory by
passing the `TESTREPORTS` environment variable.

By default all probes starting with a digit in the `probes`
subdirectory are executed. The filenames organize the probes into
chapters and sections. To disable single probes, just move them to the
`probes/disabled` folder. Each probe contains one or more checks.

Extending Probes
----------------

Probes are easy to extend: They are simple shellscripts in the
`probes` folder. Just prefix an OTC command with `apitest` to record
some actions and to report the result in the summary.

It is ok to use variables and other bash mechanics in the probes but
they should be used with care.

Ressources created in a probe script should be dismantled by the same
script. Don't use production credentials in the probes.

The filename of the probes uses a few conventions: The leading digits
are used to organize and group the single probes into chapters (OTC
subsystems) and sections and are used in the report.

License
-------

Copyright (c) 2016, 2017 by Open Telekom Cloud, T-Systems
International GmbH. Authors Kurt Garloff, Zsolt Nagy, and Nils Magnus.

The OTC testsuite is released under the MIT license. See `LICENSE` for
details.
