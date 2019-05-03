def even_number_of_evens(numbers):
    counter = 0

    for item in numbers:
        if item % 2 == 0:
            counter += 1

    if counter%2==0 and counter > 0:
        return True
    else:
        return False

assert even_number_of_evens([]) == False, "No number"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([2,4]) == True, "two even numbers"
assert even_number_of_evens([2,3]) == False, "two numbers, one even"
assert even_number_of_evens([2,3,9,10,13,7,8]) == False, "Multiple numbers, three even"
assert even_number_of_evens([2,3,9,10,13,7,8,5,12]) == True, "Multiple numbes, four even numbers"
assert even_number_of_evens([1,3,9]) == False, "No even numbers"

print("All test passed!!!")