#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    # def shift_list(self, lst: List[int], i):
    #     if i == len(lst) - 1:
    #         return
    #     x = lst[i]
    #     y = lst[i + 1]
    #     i += 1
    #     while i < len(lst):
    #         lst[i] = x
    #         x = y
    #         if i < len(lst) - 1:
    #             y = lst[i + 1]
    #         i += 1


    # def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    #     """
    #     Do not return anything, modify nums1 in-place instead.
    #     """
    #     if not nums1:
    #         nums1 = nums2
    #         return
    #     if not nums2:
    #         return nums1

    #     l = 0
    #     r = 0

    #     for i in range(m, len(nums1)):
    #         if nums1[i] == 0:
    #             nums1[i] = 201

    #     while l < m + n and r < n:
    #         if nums2[r] < nums1[l]:
    #             self.shift_list(nums1, l)
    #             nums1[l] = nums2[r]
    #             l += 1
    #             r += 1
    #         else:
    #             l += 1

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:        
        l = m - 1
        r = n - 1
        curr = m + n - 1

        while l >= 0 and r >= 0:
            if nums1[l] > nums2[r]:
                nums1[curr] = nums1[l]
                l -=1
            else:
                nums1[curr] = nums2[r]
                r -= 1
            curr -= 1

        while r >= 0:
            nums1[r] = nums2[r]
            r -= 1




# @lc code=end
print(Solution().merge([2,0], 1, [1], 1))
