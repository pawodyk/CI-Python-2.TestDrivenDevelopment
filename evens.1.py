def is_even(num):
    return num % 2 == 0

def even_number_of_evens(numbers):
    
    # evens = 0

    # for item in numbers:
    #     if is_even(item):
    #         evens += 1

    # if evens == 0:
    #     return False
    # else:
    #     return is_even(evens)

    evens = sum([1 for number in numbers if is_even(number)])
    return False if evens == 0 else is_even(evens)
        

assert even_number_of_evens([]) == False, "No number"
assert even_number_of_evens([2,4]) == True, "Two even numbers"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([1,3,9]) == False, "No even numbers"


print("All test passed!!!")