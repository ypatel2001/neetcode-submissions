"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Initialize a dictionary to map original nodes to their copies.
        # We pre-set {None: None} to handle cases where next/random is None.
        oldToCopy = {None: None}  

        # FIRST PASS: Create copies of all nodes and store mappings.
        current = head
        while current:
            # Create a new node with the same value as the original.
            copy = Node(current.val)  
            # Map the original node to its copy in the dictionary.
            oldToCopy[current] = copy  
            # Move to the next node in the original list.
            current = current.next  

        # SECOND PASS: Assign 'next' and 'random' pointers for the copied nodes.
        current = head
        while current:
            # Get the copy of the current node.
            copy = oldToCopy[current]  
            # Assign 'next' pointer: 
            # The copy's next is the copy of the original's next.
            copy.next = oldToCopy[current.next]  
            # Assign 'random' pointer: 
            # The copy's random is the copy of the original's random.
            copy.random = oldToCopy[current.random]  
            # Move to the next node in the original list.
            current = current.next  

        # Return the head of the copied list, which is oldToCopy[head].
        return oldToCopy[head]  