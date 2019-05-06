# Testing framework functions
def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)


def test_not_equal(a, b):
    assert a != b, "Did not expect {0} but got {1}".format(a, b)


def test_between(a, min, max):
    assert a >= min and a <= max, "{0} is not in a range between {1} and {2}".format(
        a, min, max)


def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(
        collection, item)


def test_not_in(collection, item):
    assert item not in collection, "set {0} contains {1}".format(
        collection, item)


# Test function:
def number_of_evens(nums):
    return sum([1 for num in nums if num % 2 == 0])


numberSet = [1, 2, 3, 4, 5]

# Testing correct execution of number_of_events function

test_are_equal(number_of_evens(numberSet), 2)
test_not_equal(number_of_evens(numberSet), 0)
test_not_equal(number_of_evens(numberSet), 5)
test_is_in(numberSet, 2)
test_is_in(numberSet, 5)

print("The number_of_evens function passed all tests!")


# this tests are designed to fail, please uncomment the one you wish to execute

print("\nNow, testing the testing framework")

# test_are_equal(number_of_evens(numberSet), 0)

# test_not_equal(number_of_evens(numberSet), 2)

# test_between(number_of_evens(numberSet), 3, 5)

# test_is_in(numberSet, 0)

# test_not_in(numberSet, 3)
