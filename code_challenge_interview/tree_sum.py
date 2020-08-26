# Question
# Given the root of a binary tree where each node contains an integer, determine the sum of all of the integer values in the tree.
# Example:
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
# The expected output given the above tree is 5 + 4 + 8 + 11 + 13 + 4 + 7 + 2 + 1, so your function should return 55.
# [execution time limit] 4 seconds (py3)
# [input] tree.integer root
# Root node of a binary tree of integers.
# [output] integer
# The sum of all of the integers in the tree.

# Answer
# Understanding:
#   - I have a binary tree of numbers. I need to find the sum of all of them!
#   - each node in the tree can be instantiated via a value, left, and right where x = value, this is all for the root node
# Planning:
#   - use a depth first traversal to visit each node in the tree. 
#   - as I visit each node, add it to a count/sum. 
#   - return the sum
# Execution:
#   - See tree_paths_sum below...
# Reflection:
#   - Time Complexity:
#       - O(n) every node needs to be visited to create the sum
#   - Space Complexity:
#       - Extra Space required for Depth First Traversals is O(h) where h is maximum height of Binary Tree. 
#         In Depth First Traversals, stack (or function call stack) stores all ancestors of a node.
#   - What could I do better? closing thoughts?
#       - If the width of the tree isn't large, I could use a BFT instead of a DFT to save some space. But if the width is large the height
#       - will be as well.... hmm...

def tree_paths_sum(root):
    stack = []
    sum = 0
    stack.append(root)
    while len(stack) > 0:
        curr_node = stack.pop()
        sum += curr_node.value
        if curr_node.left:
            stack.append(curr_node.left)
        if curr_node.right:
            stack.append(curr_node.right)
    return sum