asus-rt-n14uhp-mrtg
===================

Poll Asus rt n14uhp hardware statistics such as cpu, ram, network statistics
and plot in mrtg.

how to setup environment
========================
```sh
$ virtualenv -p python3.4 tmp/ve_asus-rt-n14uhp-mrtg
$ source tmp/ve_asus-rt-n14uhp-mrtg/bin/activate
$ pip install -r src/requirements.txt
$ # when you are done, deactivate the environment
$ deactivate
```

how to test
===========
```sh
$ python setup.py test
$ python setup.py nosetests
```
for django test, locate where is manage.py located and cd into the directory.
```sh
$ python manage.py test polls
```

read more [here](https://nose.readthedocs.io/en/latest/setuptools_integration.html)

how to quickly test in development environment
==============================================
```sh
$ python setup.py develop
```


how to quickly build a source distribution
==========================================
```sh
$ python setup.py sdist
```

how to create a tarball
=========================================
```sh
$ python setup.py bdist_egg
```

how to install
==========================================
```sh
$ sudo python setup.py install
```


code style
==========================================
you can read this link https://www.python.org/dev/peps/pep-0008/ or better yet
if you are on debian, just install this package using apt-get.

```sh
$ sudo apt-get install python-autopep8 pep8 python-pep8 python3-pep8
```

and then check source file using this command

```sh
$ autopep8 -v bin/routerStats.py
```

