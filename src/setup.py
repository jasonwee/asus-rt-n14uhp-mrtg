from setuptools import setup

def readme():
    with open('../README.md') as f:
        return f.read()

setup(name='router_statistics',
      version='0.1',
      description='retrieve router statistics and display on graph',
      long_description=readme(),
      classifiers=['Development Status :: 3 - Alpha',
                   'License :: OSI Approved :: Apache Software License',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: System :: Networking :: Monitoring'],
      keywords='asus monitoring graph',
      url='https://github.com/jasonwee/asus-rt-n14uhp-mrtg',
      author='Jason Wee',
      author_email='peichieh@gmail.com',
      license='Apache version 2.0',
      packages=['router_statistics'],
      include_package_data=False,
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'],
      scripts=['bin/routerStats.py'])
