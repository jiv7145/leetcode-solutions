#
# @lc app=leetcode id=1464 lang=python3
#
# [1464] Maximum Product of Two Elements in an Array
#

# @lc code=start
from typing import List


class Solution:
    # def maxProduct(self, nums: List[int]) -> int:
    #     results = (-1, 0, 0)
    #     for i in range(len(nums)):
    #         for j in range(i+1, len(nums)):
    #             product = (nums[i] - 1) * (nums[j] - 1)
    #             if product > results[0]:
    #                 results = (product, i, j)
    #     return results[0]

    def maxProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return (nums[0] - 1) * (nums[1] - 1)
        
# @lc code=end

