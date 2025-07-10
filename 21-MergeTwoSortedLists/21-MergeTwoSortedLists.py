# Last updated: 7/10/2025, 11:58:24 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        head = ListNode()
        if list1.val > list2.val:
            head = list2
            list2 = list2.next
        else:
            head = list1
            list1 = list1.next
        temp = head
        while list1 and list2:
            if list1.val > list2.val:
                temp.next = list2
                list2 = list2.next
            else:
                temp.next = list1
                list1 = list1.next
            temp = temp.next

        if not list1:
            temp.next = list2
        if not list2:
            temp.next = list1
        return head

