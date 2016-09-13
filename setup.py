#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of OTC Tool released under MIT license.
# Copyright (C) 2016 T-systems Kurt Garloff, Zsolt Nagy

import os
from setuptools import setup

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.rst')
    + '\n' +
    'Download\n'
    '********\n'
    )

setup(name='python-otcclient',
			version=read('VER').strip(),
			description='Open Telecom Client Tool',
			long_description=long_description,
			url='https://github.com/OpenTelekomCloud/python-otcclient',
			author='Zsolt Nagy',
			author_email='Z.Nagy@t-systems.com',
			license='MIT License',
			packages=['otcclient','otcclient.utils','otcclient.core','otcclient.plugins','otcclient.bin','otcclient.tests','otcclient.templates'],
			package_data={
			   'otcclient.bin': ['*'],     # All files from folder A
			   'otcclient.tests': ['*'],  #All text files from folder B
			   'otcclient.templates': ['*']  #All text files from folder B
			   },
			# package_dir={'': 'otcclient'},
			keywords="otc, openstack, huawei, cloud, devops, t-systems, s3, obs, containers, docker, rds",
			classifiers=[
				"Development Status :: 6 - Mature",
				"Intended Audience :: Developers",
				"Intended Audience :: Science/Research",
				"License :: OSI Approved :: MIT License",
				"Programming Language :: Python",
				"Topic :: Software Development :: Libraries :: Python Modules"
			],
			zip_safe=True,
			entry_points = {
				'console_scripts': [
					'otc = otcclient.shell:main'
				]
			},
			test_suite="tests"
		)
