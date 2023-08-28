#!/usr/bin/env python3
""" Unittesting Test Class """


import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    A Test Class that inherints from unittest
    """

    @parameterized.expand
    def test_access_nested_map(self):
        """
        First Test Case:
        Test Access for nested map
        """
        self.assertEqual()
        pass
