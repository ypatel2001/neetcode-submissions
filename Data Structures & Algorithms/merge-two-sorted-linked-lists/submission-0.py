# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # make a dummy to start off the output list 
        # and avoid any edge cases
        dummy = ListNode()
        #curr node we are at in output
        tail = dummy 

        # while we have 2 non null nodes to compare
        while list1 and list2:
            #we take the smaller val
            if list1.val < list2.val:
                #take the list 1 val and insert it into the tail
                tail.next = list1
                #we move list1 over to the next node
                list1 = list1.next
            else:
            #else we insert list2 node
                tail.next = list2
            #we move list2 over to the next node
                list2 = list2.next
            #move over tail node
            tail = tail.next
        # if either of the lists end or is null, then we take the other list and 
        #add it to the tail of the output list 
        tail.next = list1 or list2

        return dummy.next
