#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr:
            if curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

    # def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     def helper(head, prev_head=None):
    #         if head == None:
    #             return None


    #         if prev_head and head.val == prev_head.val:
    #             prev_head.next = head.next
    #             return helper(head.next, prev_head)

    #         return helper(head.next, head)
        
    #     helper(head)
    #     return head
        
# @lc code=end


