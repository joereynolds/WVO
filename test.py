import math
import unittest

import weight as w


class TestWeight(unittest.TestCase):

    def test_instantiation(self):
        weight = w.Weight(5, 'lb')

    def test_type(self):
        weight = w.Weight(5, 'lb')
        self.assertEqual(weight.measurement(), 'pounds(lb)')

    def test_weight_conversion(self):
        weight = w.Weight(5, 'lb')
        self.assertEqual(weight.convert('kg').value, 2.2679618500000003)

    def test_weight_conversion_against_same_type(self):
        weight = w.Weight(5, 'lb')
        self.assertEqual(weight.convert('lb').value, 5)

    def test_weight_conversion_thats_circular(self):
        weight = w.Weight(5, 'lb')
        self.assertEqual(weight.convert('kg').convert('lb').value, 5)

    def test_weight_conversion_thats_nested(self):
        pass

    def test_weight_addition(self):
        pass

    def test_weight_subtraction(self):
        pass


if __name__ == '__main__':
    unittest.main()
