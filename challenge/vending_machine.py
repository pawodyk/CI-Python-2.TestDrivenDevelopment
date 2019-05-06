from byotest import *

# Specification:
#  Given an amount of change that needs to be paid, we want to generate the list of coins that should be given to the customer.
#  Our function should pay the minimum number of coins possible, and the available coin denominations are 100, 50, 20, 10, 5, 2, and 1.

# Challange 1
# Change the function so that instead of a list of coins, the function works with a dictionary that contains the coin denominations,
#   and the quantity of each coin available.
# By default, assume there are 20 of each coin, but this can be overridden by passing a dictionary to the function as with the previous example.
# If a coin that would normally be used to make change isn't available the program should attempt to use smaller coins to make up the change.
# If it is not possible to make the change with the coins available, the function should raise an error.

# Challenge 2
# Think about how you could write a test that checks if a particular error is raised.
# What kind of problems does that cause?


usd_coins = {100: 20, 50: 20, 25: 20, 10: 20, 1: 20}
eur_coins = {100: 20, 50: 20, 20: 20, 10: 20, 5: 20, 2: 20, 1: 20}


def get_change(amount, coins=eur_coins):
    change = []

    for key in coins.keys():
        while key <= amount and coins[key] > 0:
            amount -= key
            coins[key] -= 1
            change.append(key)

    if amount > 0:
        raise Exception("Error: Not enough coins to give change")

    return change


# test for no change
test_are_equal(get_change(0), [])

# test for change equal to coin denominator
test_are_equal(get_change(1), [1])
test_are_equal(get_change(2), [2])
test_are_equal(get_change(5), [5])
test_are_equal(get_change(10), [10])
test_are_equal(get_change(20), [20])
test_are_equal(get_change(50), [50])
test_are_equal(get_change(100), [100])

test_are_equal(get_change(3), [2, 1])
test_are_equal(get_change(7), [5, 2])
test_are_equal(get_change(9), [5, 2, 2])

test_are_equal(get_change(35, usd_coins), [25, 10])
test_are_equal(get_change(35), [20, 10, 5])
test_not_equal(get_change(35, usd_coins), [20, 10, 5])

#while True: get_change(100)

test_exception(get_change, (10, {5: 1, 2: 2}))
#test_exception(get_change(7, {5: 1, 2: 2}))


print("All test pass!")
