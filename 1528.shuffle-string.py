#
# @lc app=leetcode id=1528 lang=python3
#
# [1528] Shuffle String
#

# @lc code=start
from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [""] * len(indices)
        count = 0
        
        for val in indices:
            result[val] = s[count]
            count += 1
        
        return "".join(result)

# @lc code=end

