#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
from typing import List


class Solution:
    # def majorityElement(self, nums: List[int]) -> int:
    #     tab = {}
    #     for num in nums:
    #         tab[num] = 1 + tab.get(num, 0)
    #         # if num not in tab:
    #         #     tab[num] = 1
    #         # else:
    #         #     tab[num] += 1
        
    #     return max(tab, key=tab.get)

    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        res = nums[0]
        for n in nums:
            if n == res:
                count += 1
            else:
                count -= 1
                if count == 0:
                    res = n
                    count = 1
        return res

            
# @lc code=end
