from setuptools import setup

def readme():
    with open('../README.md') as f:
        return f.read()

setup(
      name='router_statistics',

      # https://packaging.python.org/single_source_version/
      version='0.1',
      
      description='retrieve router statistics and display on graph',
      long_description=readme(),

      # https://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Development Status :: 5 - Production/Stable',
                   'License :: OSI Approved :: Apache Software License',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.5',
                   'Topic :: System :: Networking :: Monitoring'],

      keywords='asus monitoring graph',

      url='https://github.com/jasonwee/asus-rt-n14uhp-mrtg',

      download_url='https://github.com/jasonwee/asus-rt-n14uhp-mrtg/tarball/master',

      author='Jason Wee',
      author_email='peichieh@gmail.com',

      license='Apache version 2.0',

      packages=['router_statistics'],

      install_requires=['PyYAML'],

      include_package_data=True,

      data_files=[],

      zip_safe=False,

      test_suite='nose.collector',
      tests_require=['nose'],
      scripts=['bin/routerStats.py'],
)
