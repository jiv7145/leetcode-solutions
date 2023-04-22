#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List


class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     """
    #     Accepted
    #     57/57 cases passed (3621 ms)
    #     Your runtime beats 33.03 % of python3 submissions
    #     Your memory usage beats 66.97 % of python3 submissions (15 MB)
    #     """
    #     for i in range(len(nums)):
    #         for j in range(i+1, len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Accepted
        57/57 cases passed (56 ms)
        Your runtime beats 92.2 % of python3 submissions
        Your memory usage beats 35.87 % of python3 submissions (15.2 MB)
        """
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            complement_index = d.get(complement)
            if not complement_index or complement_index == i:
                continue
            return [i, complement_index]

# @lc code=end

