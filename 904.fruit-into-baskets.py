#
# @lc app=leetcode id=904 lang=python3
#
# [904] Fruit Into Baskets
#

# @lc code=start
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        if n == 0:
            return 0
        if n == 1:
            return 1
        l, r, max_val = 0, 1, 0
        while r < n and fruits[l] == fruits[r]:
            r += 1
        if r == n:
            return n
        curr_set = {fruits[l], fruits[r]}
        while r <= n:
            if r < n and fruits[r] in curr_set:
                r += 1
            else:
                count = r - l
                if count >= max_val:
                    max_val = count
                if r != n:
                    l = r - 1
                    while l > 0 and fruits[l - 1] == fruits[l]:
                        l -= 1
                    curr_set = {fruits[l], fruits[r]}
                else:
                    break
        return max_val

# @lc code=end

