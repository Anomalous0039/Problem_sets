
def removes_duplicates(duplicate_list):
    new_list = []
    for item in duplicate_list:
        if item not in new_list:
            new_list.append(item)
    return new_list

"""
this is a function that takes a list as input returns a new list with all 
the dupicates removed, keeping only the first occurance of each element. 

"""

    
def custom_fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizzbuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

"""
this is a functon that prints a number from 1 to n. but:
for multiples of 3, print "Fizz" instead of the number. 
for multiples of 5, print "Buzz" instead of the number. 
for numbers which are multiples of both 3 and 5, print "Fizzbuzz"
for all other numbers, just print the number. 
"""    


def handle_command(command):
    match command:
        case "start":
            print("Starting the system...")
        case "stop":
            print("Stopping the system")
        case "restart":
            print("Restarting the system...")
        case "status":
            print("system is running normally.")
        case _:
            print("unkown command")
"""
The supported commands are:

    "start" → print "Starting the system..."

    "stop" → print "Stopping the system..."

    "restart" → print "Restarting the system..."

    "status" → print "System is running normally."

    Anything else → print "Unknown command."

"""


def count_sentences(paragraph):
    sentence_count = 0
    for char in paragraph:
        if char in "!?.":
            sentence_count += 1
    return sentence_count
"""
Write a function called count_sentences(paragraph) that counts how many sentences are in a given string.
Rules:

    A sentence ends with a period ., exclamation mark !, or question mark ?.

    Ignore extra whitespace and assume no punctuation is used mid-sentence (only at the end).

    Do not use .split() or .count().

"""