#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    # def mySqrt(self, x: int) -> int:
    #     for i in range(x + 1):
    #         if i * i == x:
    #             return i
    #         if i * i > x:
    #             return i - 1

    def mySqrt(self, x: int) -> int:
        l = 0
        r = x

        result = None
        while l <= r:
            m = (l + r) // 2
            if m * m > x:
                r = m - 1
            elif m * m < x:
                l = m + 1
                result = m
            else:
                return m
        return result
# @lc code=end

