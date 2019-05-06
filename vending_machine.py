from byotest import *

## Specification:
#  Given an amount of change that needs to be paid, we want to generate the list of coins that should be given to the customer.
#  Our function should pay the minimum number of coins possible, and the available coin denominations are 100, 50, 20, 10, 5, 2, and 1.

def get_change(amount):
    if amount == 0:
        return []

    return[amount]

test_are_equal(get_change(0), [])
test_are_equal(get_change(1), [1])
test_are_equal(get_change(2), [2])


print("All test pass!")
