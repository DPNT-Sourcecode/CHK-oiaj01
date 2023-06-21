

# noinspection PyUnusedLocal
# skus = unicode string

"""
+------+-------+----------------+
| Item | Price | Special offers |
+------+-------+----------------+
| A    | 50    | 3A for 130     |
| B    | 30    | 2B for 45      |
| C    | 20    |                |
| D    | 15    |                |
+------+-------+----------------+
"""
from enum import unique


PRICES = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15
}

DISCOUNTS = {
    "A": {
        "quantity": 3,
        "price": 130
    },
    "B": {
        "quantity": 2,
        "price": 45
    }
}
def checkout(skus: str):
    skus_list = sorted(list(skus))
    unique_skus = set(skus_list)
    total = 0

    if any([sku not in PRICES for sku in skus_list]):
        return -1

    for sku in unique_skus:
        number_of_item = skus_list.count(sku)
        if sku in DISCOUNTS:
            discount = DISCOUNTS[sku]
            while number_of_item >= discount["quantity"]:
                total += discount["price"]
                number_of_item -= discount["quantity"]
        total += number_of_item * PRICES[sku]

    return total
