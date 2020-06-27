# DATE 6/27/2020

# QUESTION
# Write a program to determine if a number, given on the command line, is prime.

def solution(num):
    if (num >= 1):
        for x in range(1, num//2):
            if (num % x) == 0:
                return f"{num} is not a prime number"
    return f"{num} is a prime number"
    
# TEST
print(solution(4)) # should return string ==> "{number}is a prime number."

# My explanation for this problem:
# - In order for a number to be considered "PRIME", it needs to be greater then 1, and its only factors can be 1 and itself.
# - To solve this, I would first take care of the edge case of it being less then 1. 

# TIME COMPLEXITY
# -

# SPACE COMPLEXITY
# - 

# FUTURE NOTES FOR OPTIMIZATION
# - 