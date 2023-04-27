#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
from typing import List


class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         """
#         Accepted
#     113/113 cases passed (25 ms)
#     Your runtime beats 97.96 % of python3 submissions
#     Your memory usage beats 6.62 % of python3 submissions (14 MB)
#         """
#         def loop():
#             for i in range(len(nums) - 1):
#                 if nums[i] == val:
#                     j = i + 1
#                     while j < len(nums) and nums[j] == val:
#                         if j == len(nums) - 1:
#                             return
#                         j += 1
#                     nums[i], nums[j] = nums[j], nums[i]

#         loop()
#         count = 0
#         for v in nums:
#             if v == val:
#                 break
#             count += 1
#         return count

    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            else:
                i += 1
        return i



# @lc code=end

