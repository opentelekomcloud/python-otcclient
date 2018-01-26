#!/bin/sh
# http://peterdowns.com/posts/first-time-with-pypi.html
# ## register 
# python setup.py register
# python setup.py register -r pypitest
# ## build 
python setup.py build
# ## soruce dist + wheel dist + upload 
python setup.py sdist bdist_wheel upload 
python setup.py sdist bdist_wheel upload -r pypitest
