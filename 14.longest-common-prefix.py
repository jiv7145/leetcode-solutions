#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        result = strs[0]
        for s in strs:
            if len(s) < len(result):
                result = result[:len(s)]
            for i in range(len(result)):
                if s[i] != result[i]:
                    result = result[:i]
                    break
        return result

        
# @lc code=end

