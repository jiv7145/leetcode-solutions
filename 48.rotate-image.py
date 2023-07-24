#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
from typing import List


class Solution:
    # def rotate(self, matrix: List[List[int]]) -> None:
    #     """
    #     Do not return anything, modify matrix in-place instead.
    #     """
    #     n = len(matrix)
    #     for i in range(n):
    #         for j in range(i):
    #             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
    #     for i in range(n):
    #         matrix[i].reverse()

    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        l = 0
        r = n - 1
        t = 0
        b = n - 1
        
        while l < r and t < b:
            for i in range(r - l):
                # one = matrix[t][l+i]
                # two = matrix[t+i][r]
                # three = matrix[b][r-i]
                # four = matrix[b-i][l]

                # matrix[t][l+i] = four
                # matrix[t+i][r] = one
                # matrix[b][r-i] = two
                # matrix[b-i][l] = three

                temp = matrix[t][l+i]
                matrix[t][l+i] = matrix[b-i][l]
                matrix[b-i][l] = matrix[b][r-i]
                matrix[b][r-i] = matrix[t+i][r]
                matrix[t+i][r] = temp
            l += 1
            r -= 1
            t += 1
            b -= 1

        
# @lc code=end

