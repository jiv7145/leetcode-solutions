#
# @lc app=leetcode id=1572 lang=python3
#
# [1572] Matrix Diagonal Sum
#

# @lc code=start
from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        result = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    result += mat[i][j]
                if i + j == n - 1:
                    result += mat[i][j]
        if n % 2 != 0:
            result -= mat[n // 2][n // 2]
        return result
# @lc code=end

