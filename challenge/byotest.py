# Testing framework
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


# Challange 2

def test_exception(f, args):
    try:
        f(*args)
        assert False, "Exception did not occured!"
    except Exception as ex:
        print("Exception Occured: " + str(ex))
