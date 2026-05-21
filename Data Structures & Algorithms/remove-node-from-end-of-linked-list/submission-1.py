# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head 
        while n > 0 and right is not None:
            right = right.next
            #when n = 0 we have shifted the correct distance
            n -= 1
            # shifts the points to the end to get them in 
            #the correct spot for replacement
        while right: 
            left = left.next
            right = right.next
            
        # delete
        left.next = left.next.next
        # we do not include the dummy node in the return hence .next
        return dummy.next


        


