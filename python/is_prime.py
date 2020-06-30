# DATE 6/27/2020

# QUESTION
# Write a program to determine if a number, given on the command line, is prime.

def solution(num):
    if (num >= 1):
        for x in range(1, num):
            print(x, "---x")
            # if (num % x == 0):
            #     return f"{num} is NOT a prime number"
            # else: 
            #     return f"{num} IS a prime number."
    elif (num == 0):
        return f"{num} is NOT a prime number."


# TEST
print(solution(3))  # should return string ==> "{number}is a prime number."

# My explanation for this problem:
# - In order for a number to be considered "PRIME", it needs to be greater then 1, and its only factors can be 1 and itself.
# - To solve this, I would first take care of the edge case of it being less then 1.

# TIME COMPLEXITY
# -

# SPACE COMPLEXITY
# -

# FUTURE NOTES FOR OPTIMIZATION
# -
