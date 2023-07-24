#
# @lc app=leetcode id=376 lang=python3
#
# [376] Wiggle Subsequence
#

# @lc code=start
from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        subsequence = []
        for i in range(len(nums) - 1):
            subsequence.append(nums[i + 1] - nums[i])

        max_len = 1
        subsequence = list(filter(lambda x: x != 0, subsequence))
        if not subsequence:
            return 1
        
        for i in range(len(subsequence) - 1):
            if subsequence[i] * subsequence[i + 1] < 0:
                max_len += 1

            
        return max_len + 1
    



# Solution().wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8])

# @lc code=end

