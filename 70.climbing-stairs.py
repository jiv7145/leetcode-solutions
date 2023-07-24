#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
import math


class Solution:
    # def climbStairs(self, n: int) -> int:
    #     # zero_twos = n C 0
    #     # one_twos = n - 1 C 1
    #     # two_twos = n-2 C 2

    #     max_num_of_twos = n // 2

    #     result = 0
    #     for i in range(max_num_of_twos + 1):
    #         result += math.comb(n - i, i)

    #     return result

    # def climbStairs(self, n: int) -> int:
    #     if n == 1:
    #         return 1
    #     if n == 2:
    #         return 2
    #     return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    # def climbStairs(self, n: int) -> int:
    #     def helper(num):
    #         if num == 1:
    #             return 1
    #         if num == 2:
    #             return 2
            
    #         if not cache[num]:
    #             cache[num] = helper(num - 1) + helper(num - 2)
    #         return cache[num]

    #     cache = [None] * 46

    #     return helper(n)

    def climbStairs(self, n: int) -> int:
        memo = [None] * 46
        memo[1] = 1
        memo[2] = 2
        for i in range(3, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]
        return memo[n]
        
# @lc code=end
