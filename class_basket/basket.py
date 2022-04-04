import unittest

prices = {"yam": 200, "cheese": 50, "bread": 20}


class Product:
    def __init__(self, n='Unknown', q=0):
        self.name = n
        self.quantity = q


class Basket:
    def __init__(self, c='Unknown'):
        self.__Content = {}
        self.__CustomerName = c

    def get_customer_name(self):
        return self.__CustomerName

    def add_item(self, p=Product("name", 3)):
        if p.quantity > 0 and p.name in prices:
            self.__Content[p.name] = self.__Content.get(p.name, 0) + p.quantity
        else:
            raise ValueError("Invalid Input")

    def get_quantity(self, n=""):
        return self.__Content.get(n, 0)

    def value(self):
        current_price = 0
        for item, quantity in self.__Content.items():
            try:
                current_price = current_price + (prices[item] * quantity)
            except KeyError:
                print("There was a missing item")
                pass
        return current_price


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
