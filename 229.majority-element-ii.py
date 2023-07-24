#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#

# @lc code=start
import math
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        times = len(nums) // 3
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        return [k for k in count if count[k] > times]
# @lc code=end

