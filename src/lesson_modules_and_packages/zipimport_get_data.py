import sys
sys.path.insert(0, 'zipimport_example.zip')

import os
import example_package
print(example_package.__file__)
data = example_package.__loader__.get_data(
    'example_package/README.txt')
print(data.decode('utf-8'))
