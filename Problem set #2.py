"""
This is a function that: takes a string, finds the reverse of that string, checks if it's a
palindrome. 
"""

def palindrome_check(user_string):
    user_string = user_string.lower()
    reversed_user_string = user_string[::-1]
    if reversed_user_string == user_string:
        return True 
    else:
        return False
    

"""
This is a function that: takes a list, and finds the largest number within that list
without using max().

"""


def find_largest(numbers):
    largest_number = numbers[0] 
    for number in numbers:
        if number > largest_number:
            largest_number = number
    return largest_number



"""
This is a function that: takes a list of numbers, returns the smallest one.

"""

def find_smallest(numbers_list):
    smallest_number = numbers_list[0]
    for number in numbers_list:
        if smallest_number > number:
            smallest_number = number
        else:
            continue
    return smallest_number




"""
This is a function that: takes a list of numbers and a target, returns the amount
of times that target is inside of the list. 

"""

def count_occurances(list,num):
    occurance_count = 0
    for numbers in list:
        if numbers == num:
            occurance_count += 1
        else:
            continue
    return occurance_count

