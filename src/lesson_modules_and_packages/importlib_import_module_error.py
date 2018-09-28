import importlib


try:
    importlib.import_module('example.nosuchmodule')
except ImportError as err:
    print('Error:', err)
