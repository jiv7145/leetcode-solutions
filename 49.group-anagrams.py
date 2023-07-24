#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from collections import Counter, defaultdict
from typing import List


class Solution:
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     d = {}
    #     result = []
    #     for st in strs:
    #         _sorted_str = ''.join(sorted(st))
    #         d[_sorted_str] = d.get(_sorted_str, []) + [st]
    #     for _, v in d.items():
    #         result.append(v)
    #     return result
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            k = [0] * 26
            for c in s:
                pos = ord(c) - ord('a')
                k[pos] += 1
            d[tuple(k)].append(s)

        return d.values()

        # @lc code=end


