# Question
# Given a package with a weight limit limit and an array of integers items of where each integer represents the weight of an item, 
# implement a function merge_packages that finds the first two items in the items array whose sum of weights equals the given weight limit limit.
# Your function should return a pair [i, j] of the indices of the item weights, ordered such that i > j. If such a pair doesn't exist, 
# return an empty array.
# Examples:
# Input: items = [4, 6, 10, 15, 16], limit = 21
# Output: [3, 1]
# Explanation: The weight of the items at indices 3 and 1 sum up to the specified limit.
# [execution time limit] 4 seconds (py3)
# [input] array.integer items
# A list of item weights.
# [input] integer limit
# The weight limit we're aiming for by merging two packages.
# [output] array.integer
# A pair of item indices indicating the two items that, when merged, reach the specified limit.

# Answer
# Understanding:
#   - each package has an array of items (list of nums)
#   - each package has a limit (also a num)
#   - grab two items from package, whose weights add up to the limit of the package
#   - its possible that there is no answer, if so return an empty array
# Planning:
#   - see comments in code. Its preferrable.
#   - I can do this by subtracting the limit from each number.  
#   - I can then save a key/value pair in a hashtable where the key is the difference value just       
#     calculated and the value is the index where I got the number I used to subtract from limit
#   - after I've done this I can search each key and if I find that one of the other items
#   - is in the hash table, I've found my two indices so return them, else return empty list
# Execution:
#   - see merge_packages(items, limit) below:
# Reflection:
#   - Time Complexity:
#       - worst case scenario would be O(n) because there are no items that add up to limit, so I'd check every one. 
#   - Space Complexity:
#       - O(n) storage because it will potentially hold all items in differences hashtable. 
#   - What could I do better? closing thoughts?
#       -  I think this is the most optimal solution because using a hashtable increases speed big time compared to 
#          a nested for loop. I could consider naming conventions though.


def merge_packages(items, limit):
    # create hash table and solution array
    differences = {}
    solution = []
    # for every item in array, add the difference to the hashtable i.e. (limit - i) and set its value to the current index
    # As your iterating, check if current item is already in the hashtable keys. If it is, you've found your two indices that 
    # contain the items that add up to limit! So save them as a solution and return it. 
    for i in range(len(items)):
        if items[i] not in differences:
            differences[limit - items[i]] = i
        else:
            solution = [i, differences[items[i]]]
            return solution
    if len(solution) == 0:
        return []
