# Last updated: 7/10/2025, 11:58:27 AM
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            # Extract values, default to 0 if list is exhausted
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate total and carry in one step
            total = val1 + val2 + carry
            carry = total // 10
            
            # Create new node directly
            current.next = ListNode(total % 10)
            current = current.next
            
            # Move to next nodes
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next