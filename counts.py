# def count_upper_case(message):
#     count = 0
#     for c in message:
#         if c.isupper():
#             count += 1
#     return count


def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])


assert count_upper_case("") == 0, "Empty String"
assert count_upper_case("A") == 1, "One Upper Letter"
assert count_upper_case("a") == 0, "One Lower Letter"
assert count_upper_case("Abcd") == 1, "One Upper Letter"
assert count_upper_case("AbcD") == 2, "One Upper Letter"
assert count_upper_case("abCD") == 2, "One Lower Letter"

assert count_upper_case("£$%^&*") == 0, "Special chars"
assert count_upper_case("A£B$C%\a^b&c*") == 3, "Special chars with mixed letters"

# assert count_upper_case(123456789) == 0, "Number instead of string"
# assert count_upper_case("A") == 0, "Testing the test fail"

print("all test passed")
