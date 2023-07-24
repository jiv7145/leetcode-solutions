#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_copy = set([i for i in range(len(nums) + 1)])
        for i in nums:
            if i in nums_copy:
                nums_copy.remove(i)
        
        return list(nums_copy)[0]

# @lc code=end

