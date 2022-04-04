# Test that:
# the value is zero on creation
# Value is correct after adding some items
# Value is correct after adding some additional items (duplicate)
# Cannot add a negative quantity (Error)
# Cannot add something not in the pricelist (Should give a ValueError!)
# Submit on Moodle by tomorrow's class

import unittest
from class_basket.basket import Basket, Product


class TestBasket(unittest.TestCase):
    def test_when_create_new_basket_value_is_zero(self):
        empty_basket = Basket()
        self.assertEqual(empty_basket.value(), 0)

    def test_value_is_correct_after_adding_items(self):
        new_basket = Basket()
        new_basket.add_item(Product("yam", 10))
        self.assertEqual(new_basket.value(), 2000)

    def test_value_is_correct_after_adding_duplicate_item(self):
        new_basket = Basket()
        new_basket.add_item(Product("yam", 1))
        new_basket.add_item(Product("yam", 2))
        self.assertEqual(new_basket.value(), 600)

    def test_that_negative_quantity_cannot_be_added(self):
        with self.assertRaises(ValueError):
            new_basket = Basket()
            new_basket.add_item(Product("yam", -10))

    def test_that_only_items_in_price_list_can_be_added(self):
        with self.assertRaises(ValueError):
            new_basket = Basket()
            new_basket.add_item(Product("coke", 10))
