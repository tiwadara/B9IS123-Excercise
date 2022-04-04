# Create a function returning the total cost of the basket, given two files,
# prices, containing:
# product price
# product2 price2
# ...
# basket, containing:
# product quantity
# product6 quantity6
# prices and basket are filenames which should be passed to the function as parameters.
#
# handle appropriate errors.


def total_cost(basket, prices):
    _prices = {}
    _basket = {}
    _total = 0
    with open(prices, 'r') as file:
        for line in file:
            (key, value) = line.split()
            try:
                _prices[str(key)] = float(value)
            except ValueError:
                pass

    with open(basket, 'r') as file:
        for line in file:
            (key, value) = line.split()
            try:
                _basket[str(key)] = int(value)
            except ValueError:
                pass
    for i in _basket:
        try:
            _total += _prices[i] * _basket[i]
        except KeyError:
            pass
    return _total


print(total_cost('basket.txt', 'prices.txt'))
