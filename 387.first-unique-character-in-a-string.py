#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = defaultdict(int)
        for i in s:
            d[i] += 1
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1

# @lc code=end

