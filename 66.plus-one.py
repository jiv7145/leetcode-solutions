#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
from typing import List


class Solution:
    # def plusOne(self, digits: List[int]) -> List[int]:
    #     """
    #     Accepted
    #     111/111 cases passed (37 ms)
    #     Your runtime beats 39.95 % of python3 submissions
    #     Your memory usage beats 5.48 % of python3 submissions (13.9 MB)
    #     """
    #     s = ""
    #     for i in digits:
    #         s += str(i)
        
    #     return map(int, str(int(s) + 1))

    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Accepted
        111/111 cases passed (29 ms)
        Your runtime beats 88.4 % of python3 submissions
        Your memory usage beats 43.88 % of python3 submissions (13.8 MB)
        """
        if digits == []:
            return []

        if digits[-1] + 1 < 10:
            return digits[:-1] + [digits[-1] + 1]

        if len(digits) == 1 and digits[-1] + 1 >= 10:
            return [1, digits[-1]+1-10]
        return self.plusOne(digits[:-1]) + [digits[-1]+1-10]



# @lc code=end

