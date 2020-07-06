# DATE 6/27/2020

# https://www.khanacademy.org/computing/computer-science/cryptography/comp-number-theory/v/sieve-of-eratosthenes-prime-adventure-part-4
# Implement [The Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes), one
# of the oldest algorithms known (ca. 200 BC).
# this algorithim finds all prime numbers up to a given limit

def sieve_of_eratosthenes(limit):
    composites = []
    candidates = set([*range(2, limit)])
    for x in range(2, (limit+1)):
        if (x not in candidates):
            continue
        composite = x + x
        while composite < limit + 1:
            candidates.discard(composite)
            composite += x
    return ("Here are your list of primes: ", candidates)


print(sieve_of_eratosthenes(45))
# My explanation for this problem:
# - Basically I just follow the sieve of eratosthenes algorithim to solve this problem. It works in the following way:
# - All numbers from 2 through to the limit given are possible prime numbers. At the beginning, they are all considered "unmarked"
# - Start iterating over each number. If you come across an "unmarked" number, that means its prime.
# - So, you would reach the first number, 2, and you would "mark it" therefore declaring your first prime number.
# - After you mark a prime number, you can now "mark" all multiples of that marked number (2), because we know they are composite (i.e. not prime)
# - After you mark every multiple of 2, you can repeat. The next "unmarked" number is 3. Add this to your list of primes that you collect.
# - Same as before, you can now take multiples of the newly "marked" number (3), and "mark" each of them, declaring them NOT prime.
# - You'll notice that "6" is a multiple of BOTH "2" AND "3". So a neat optimizaation to this algorithim is always start at the square of the newly
#   marked number, when you are "marking off" new composite numbers to declare them NOT prime. That way you don't waste your time looking to "mark"
#   off "6" again.
# - Continue! You'll come across a "marked" number, "4". Since its "marked", you can skip it and you'll come to "5". Repeat the same process
#   you did with "3 and your on your way!"
# - Eventually you'll get to an "unmarked" number whose square is greater then the original limit given at the beginning. Once you've reached
#   this point that means the rest of the unmarked numbers ARE PRIME. Fill in the rest of them as prime and your done!
# TIME COMPLEXITY
# -

# SPACE COMPLEXITY
# -

# FUTURE NOTES FOR OPTIMIZATION
# -
