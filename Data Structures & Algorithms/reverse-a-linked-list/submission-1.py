# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # set prev to none as no prev at head
        prev = None
        #first node
        current = head
        
        #while we have a node in the list
        while current:
            #save the next pointer before breaking the link
            next_ = current.next
            #set the pointer "current.next" = prev and that reverses the direction
            current.next = prev
            #move the pointers prev and current along the list
            prev = current
            current = next_
        
        #in the end we return prev which is now the head of the list 
        # because current and next_ both are None
        return prev
            

