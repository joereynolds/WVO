import math
import unittest

import weight as w


class TestWeight(unittest.TestCase):


    def test_instantiation(self):
        weight = w.Weight(5, 'lb')

    def test_weight_conversion(self):
        weight = w.Weight(5, 'lb')
        self.assertEqual(weight.convert('kg').value, 2.2679618500000003)

    def test_weight_conversion_against_same_type(self):
        weight = w.Weight(5, 'lb')
        self.assertEqual(weight.convert('lb').value, 5)

    def test_weight_conversion_thats_circular(self):
        weight = w.Weight(5, 'lb')
        self.assertEqual(weight.convert('kg').convert('lb').value, 5)

    def test_simple_weight_addition(self):
        weight = w.Weight(5, 'lb')
        other_weight = w.Weight(5, 'lb') 
        self.assertEqual(weight.value + other_weight.value, 10)

    def test_weight_addition_against_different_types(self):
        weight = w.Weight(5, 'lb')
        other_weight = w.Weight(5, 'kg')
        self.assertEqual((weight + other_weight).value, 16.02311310924388)

    def test_simple_weight_subtraction(self):
        weight = w.Weight(5, 'lb')
        other_weight = w.Weight(2, 'lb')
        self.assertEqual((weight - other_weight).value, 3)

    def test_weight_subtraction_against_different_type(self):
        weight = w.Weight(5, 'kg')
        other_weight = w.Weight(5, 'lb')
        self.assertEqual((weight - other_weight).value, 2.7320381499999997)


if __name__ == '__main__':
    unittest.main()
