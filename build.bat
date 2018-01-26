rem http://peterdowns.com/posts/first-time-with-pypi.html
rem ## register 
rem python setup.py register
rem python setup.py register -r pypitest
rem ## build 
del build /Q /S
del python_otcclient.egg-info /Q /S
del dist /Q /S 
python setup.py build
rem ## soruce dist + wheel dist + upload 
python setup.py sdist bdist_wheel
twine upload dist/*

rem python setup.py bdist_wheel upload 
rem python setup.py sdist bdist_wheel upload -r pypitest
