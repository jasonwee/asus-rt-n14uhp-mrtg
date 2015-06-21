#!/usr/bin/python

#require python-mock

import unittest
import yaml

from mock import MagicMock

class RouterStatsTestCase(unittest.TestCase):
    """Tests for routerStats.py. """

    def test_get_cpu_stat_from_router(self):
        stream = open("../conf/config.yaml", "r")
        config = yaml.load(stream)
        self.assertTrue(get_cpu_stat_from_router(config) is not None)

if __name__ == '__main__':
        from os import sys, path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
        from src.routerStats import get_cpu_stat_from_router
        unittest.main()

