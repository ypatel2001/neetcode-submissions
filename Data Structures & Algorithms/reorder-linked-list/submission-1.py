# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Step 1: Find the middle of the linked list using slow and fast pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
        
        # Step 2: Split the list into two halves and prepare to reverse the second half
        second = slow.next  # The start of the second half
        prev, slow.next = None, None  # Break the link between first and second half
        
        # Step 3: Reverse the second half of the linked list
        while second:
            tmp = second.next  # Store next node before breaking the link
            second.next = prev  # Reverse the current node's pointer
            prev = second  # Move prev to current node
            second = tmp  # Move to next node in original list
        
        # Step 4: Merge the two halves by alternating nodes
        first, second = head, prev  # prev is now the head of the reversed second half
        while second:
            tmp1, tmp2 = first.next, second.next  # Store next nodes of both halves
            first.next = second  # Link first half's node to second half's node
            second.next = tmp1  # Link second half's node back to first half's next node
            first, second = tmp1, tmp2  # Move both pointers forward