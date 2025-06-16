"""
This is a python function that asks the user for a number, and returns if it's 
even or odd. 
"""
def odd_even(num):
    if num % 2 == 0:
        return "The number is even"
    else:
        return "The number is odd"
odd_even(2)


"""
This is a python function that asks the user to enter two numbers and returns the following. 
The sum, the difference, the product, and the quotient.
"""
def simple_calculator(num1,num2):
    sum = num1 + num2 
    difference = num1 - num2
    product = num1 * num2 
    quotient = num1/num2
    print(f"Your sum is {sum}, the difference is {difference}, the product is {product}, the quotient is {quotient}")
simple_calculator(1,2)


"""
This is a python function that: Takes the list of numbers, calculates the average, and then returns the average.
"""
def print_average(list):
    sum_of_list = 0
    total_number_list = 0
    for numbers in list:
        sum_of_list += numbers
        total_number_list += 1
    average = sum_of_list/total_number_list
    return average

"""
This is a python function that: asks the user to enter a string. and then prints that string in reverse. 
"""
def reverse_string(string):
    reverse_string = []
    for words in string:
        reverse_string.insert(0, words)
    return "".join(reverse_string)



"""
This is a python function that: Takes a string input from a user, counts how many vowels are in the string,
prints the total number of vowels. 
"""
def vowel_count(string):
    vowel_count = 0
    for char in string:
        if char.lower() in "aeiou":
            vowel_count += 1
        else:
            continue
    return vowel_count
