#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # def addList(self, list1, list2):
    #     head = list1
    #     while head.next:
    #         head = head.next
    #     head.next = list2
    #     return head

    # def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #     """
    #     Accepted
    #     208/208 cases passed (34 ms)
    #     Your runtime beats 86.47 % of python3 submissions
    #     Your memory usage beats 20.5 % of python3 submissions (14.1 MB)
    #     """        
    #     if list1 is None and list2 is None:
    #         return None
    #     if list1 is not None and list2 is None:
    #         return list1
    #     if list2 is not None and list1 is None:
    #         return list2

    #     if list1.val < list2.val:
    #         return self.addList(ListNode(list1.val, None), self.mergeTwoLists(list1.next, list2))
    #     else:
    #         return self.addList(ListNode(list2.val, None), self.mergeTwoLists(list1, list2.next))

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Accepted
        208/208 cases passed (30 ms)
        Your runtime beats 96.29 % of python3 submissions
        Your memory usage beats 97.76 % of python3 submissions (13.8 MB)
        """
        head = ListNode()
        current = head
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 or list2
        

        return head.next
        


        
# @lc code=end

