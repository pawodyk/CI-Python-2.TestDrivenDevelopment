def even_number_of_evens(numbers):
    if numbers == []:
        return False
    else:
        evens = 0

    for item in numbers:
        if item % 2 == 0:
            evens += 1
    if evens == 0:
        return False
    else:
        return evens % 2 == 0
        

assert even_number_of_evens([]) == False, "No number"
assert even_number_of_evens([2,4]) == True, "Two even numbers"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([1,3,9]) == False, "No even numbers"


print("All test passed!!!")