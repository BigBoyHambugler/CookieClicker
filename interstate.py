"""
interstate.py
Brycen Siv
interstate.py: Given the interstate number as input, tell whether its a major or auxiliary highway as well as if it runs north/south or east/west

Error check that the number is not 0, negative, divisible by 100, or over 1000. Repeat input if invalid number (use while loop).
Odd numbered highways run north/south, evens run east/west
Major highways end in 5 or 0 (divisible by 5)
"""
def interstate(): 
    # Variables
    major_auxiliary = ''
    direction = ''
    num = int (input("Input Highway Number:"))
    # Error checking 
    while (num <= 0 or num % 100 == 0 or num > 1000):
        print("Invalid Highway Number.")
        num = int (input("Input a Highway Number:"))
    # Checking for major or auxiliary highway
    if (num % 5 == 0): 
        major_auxiliary += 'a major'
    else:
        major_auxiliary += 'an auxiliary'
    # Checking whether if it runs north, south, east, or west.
    if (num % 2 == 0):
        direction += 'east/west'
    else:
        direction += 'north/south'
    # The sentence output
    print(f"Highway {num} is {major_auxiliary} highway that runs {direction}.")

