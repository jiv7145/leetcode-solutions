#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    # def removeDuplicates(self, nums: List[int]):
    #     """
    #     Accepted
    #     361/361 cases passed (88 ms)
    #     Your runtime beats 63.79 % of python3 submissions
    #     Your memory usage beats 93.63 % of python3 submissions (15.5 MB)
    #     """
    #     prev = None
    #     unique_count = 0
    #     for i in range(len(nums)):
    #         if nums[i] == prev:
    #             nums[i] = None
    #             continue
    #         prev = nums[i]
    #         unique_count += 1
    #     index = 1
    #     for i in range(1, len(nums)):
    #         if nums[i - 1] != None and nums[i] != None:
    #             index += 1
    #         elif nums[i] != None:
    #             nums[index] = nums[i]
    #             nums[i] = None
    #             index += 1

    #     return unique_count
    def removeDuplicates(self, nums: List[int]):
        l_pointer = 1
        r_pointer = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]: # unique value
                nums[l_pointer] = nums[i]
                l_pointer += 1
        return l_pointer


print(Solution().removeDuplicates([1,2,2,3]))
# @lc code=end

