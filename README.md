asus-rt-n14uhp-mrtg
===================

Poll Asus rt n14uhp hardware statistics such as cpu, ram, network statistics
and plot in mrtg.


how to test
===========
```sh
$ python setup.py test
$ python setup.py nosetests
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
