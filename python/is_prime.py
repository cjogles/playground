# DATE 6/27/2020

# QUESTION
# Write a program to determine if a number, given on the command line, is prime.

def solution(num):
    if (num < 1):
        return f"{num} is not a prime number"
    else:
        for x in range(2, num):
            if (num % x) == 0:
                return f"{num} is not a prime number"
    return f"{num} is a prime number"


# TEST
print(solution(13))  # should return string ==> "{number}is a prime number."

# My explanation for this problem:
# - In order for a number to be considered "PRIME", it needs to be greater then 1, and its only factors can be 1 and itself.
# - To solve this, I would first take care of the edge case of it being less then 1, if so, its not prime.
# - next, I realize that every non-negative integer greater then 0 has 1 and itself as its factors. I just need to check if any other
#   number is a factor of the given number. So I take 2 through (num -1), loop through each one of them and run the following:
#   num % x == 0... if that evaluates to true, that means there is a factor of num outside of 1 and itself, which makes it NOT prime. 
#   otherwise return prime

# TIME COMPLEXITY
# -

# SPACE COMPLEXITY
# -

# FUTURE NOTES FOR OPTIMIZATION
# -
