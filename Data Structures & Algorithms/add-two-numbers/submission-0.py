# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ### 1. Initialize Result List and Helpers ###
        dummy = ListNode()  # Dummy node to simplify edge cases
        current = dummy     # Pointer to build the result list
        carry = 0           # Stores the carry-over between digit additions

        ### 2. Process Both Lists Digit-by-Digit ###
        while l1 or l2 or carry:
            # Get current digits (or 0 if list is exhausted)
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            ### 3. Core Addition Logic ###
            total = v1 + v2 + carry      # Sum current digits and carry
            carry = total // 10           # Calculate new carry (tens place)
            digit = total % 10            # Extract current digit (units place)
            current.next = ListNode(digit) # Append digit to result

            ### 4. Move Pointers Forward ###
            current = current.next        # Advance result pointer
            l1 = l1.next if l1 else None  # Move to next digit in l1
            l2 = l2.next if l2 else None  # Move to next digit in l2

        ### 5. Return the Result ###
        return dummy.next  # Skip dummy node to get actual result