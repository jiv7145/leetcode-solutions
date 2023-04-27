#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Accepted
        65/65 cases passed (50 ms)
        Your runtime beats 68.53 % of python3 submissions
        Your memory usage beats 97.69 % of python3 submissions (14.6 MB)
        """
        r_pointer = len(nums) - 1
        l_pointer = 0
        while l_pointer <= r_pointer:
            curr = int((l_pointer + r_pointer) / 2)
            if target < nums[curr]:
                r_pointer = curr - 1
            elif target > nums[curr]:
                l_pointer = curr + 1
            else:
                return curr
        return l_pointer

# @lc code=end
# Solution().searchInsert([1,3,5,6],7)
