#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from typing import List
from collections import Counter, defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        d = defaultdict(list)
        for key, v in c.items():
            d[v].append(key)
        d = dict(sorted(d.items(), reverse=True))
        result = []
        i = 0
        it = iter(d.items())
        while i < k:
            pair = next(it)
            for l in pair[1]:
                result.append(l)
                i += 1
                if i == k:
                    break
        
        return result

        
# @lc code=end

