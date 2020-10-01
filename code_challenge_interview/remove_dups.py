# Question
# Given a linked list of integers, remove any nodes from the linked list that have values that have previously occurred in the linked list. 
# Your function should return a reference to the head of the updated linked list.
# Example:
# Input: (3) -> (4) -> (3) -> (2) -> (6) -> (1) -> (2) -> (6) -> N
# Output: (3) -> (4) -> (2) -> (6) -> (1) -> N
# Explanation: The input list contains redundant nodes (3), (6), and (2), so those should be removed from the list.
# [execution time limit] 4 seconds (py3)
# [input] linkedlist.integer node
# The head node of the linked list.
# [output] linkedlist.integer
# The head node of the updated linked list.

# Answer
# Understanding:
#   - I have a singly linked list of numbers
#   - I need to remove redundant nodes.
#   - After removing them, return the head node of new singly linked list! Easy Peasy!
#   - Singly linked list nodes are defined as a ListNode(x) where self.value = x, and self.next = None
# Planning:
#   - create an array to save all the elements I want to save in a singly linked list
#   - create a hash table to save all those same elements, with a count of how many are there
#   - Traverse the linked list,and save all non duplicate items in hashtable
#   - Traverse hash table and save each item (so non duplicates) in solution array
#   - save solution array items in a linked list. then return the head! Easy Peasy!
# Execution:
#   - See condense_linked_list(node) below...
# Reflection:
#   - Time Complexity:
#       - O(n) + (O(n) - duplicates) + (O(n) - duplicates) === O(n) linear time
#       - then again, the only input is a single node... so maybe its 1^n?
#   - Space Complexity:
#       - O(n) * 2 - duplicates^2
#   - What could I do better? closing thoughts?
#       - instead of saving things in a solution array, I could of just traversed the hash table only instead
#       - I think linear time is best, I HAVE to check each node for duplicates. 

def condense_linked_list(node):
    # create a place to store 
    solution_arr = []
    cache = {}

    # traverse singly linked list and add each node to a hashtable. No duplicates.
    # keys should represent each distinct node in singly linked list, 
    # values should be the count of how many times they appear in the linked list
    current_node = node
    while current_node != None: # O(n) because I need to go through each node in singly linked list
        if current_node.value not in cache:
            cache[current_node.value] = 1
        else:
            # (current_node.value) is a redundancy, so just increase its value, 
            # don't add a new item to hash table
            cache[current_node.value] += 1
        current_node = current_node.next

    # for each key in cache append it to the solution array.
    for item in cache.items(): # O(n) - all duplicates [key, value]
        solution_arr.append(item[0]) 

    # now iterate through solution array, and change it back into a linked list,
    # return the head of the singly linked list
    # save max_length of solution array to help with logic inside while loop
    # i.e. when to save head value, and when to set the end of the linked list
    curr = ListNode(None)
    max_length = len(solution_arr)
    head = None
    while len(solution_arr) > 0: # O(n) - duplicates
        curr.value = solution_arr[0]
        if len(solution_arr) == max_length:
            head = curr
        if (len(solution_arr) == 1):
            curr.next = None
        else:
            curr.next = ListNode(None)
        curr = curr.next
        solution_arr.pop(0)
    return head