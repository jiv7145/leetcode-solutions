#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
from typing import List


class Solution:
    # def minPathSum(self, grid: List[List[int]]) -> int:
    #     hori_len = len(grid[0])
    #     vert_len = len(grid)
    #     def traverse(i, j, curr_res, final_results):
    #         if i == vert_len - 1 and j == hori_len - 1:
    #             return final_results + [curr_res + grid[i][j]]

    #         if i == vert_len or j == hori_len:
    #             return []
            
    #         curr_val = grid[i][j]
    #         return traverse(i + 1, j, curr_res + curr_val, final_results) +\
    #             traverse(i, j + 1, curr_res + curr_val, final_results)

    #     return min(traverse(0,0,0,[]))

    # def minPathSum(self, grid: List[List[int]]) -> int:
    #     hori_len = len(grid[0])
    #     vert_len = len(grid)
        
    #     def traverse(i, j, curr_res):
    #         if i == vert_len - 1 and j == hori_len - 1:
    #             return curr_res + grid[i][j]

    #         if i == vert_len or j == hori_len:
    #             return float('inf')

    #         curr_val = grid[i][j]
    #         return min(traverse(i + 1, j, curr_res + curr_val),
    #             traverse(i, j + 1, curr_res + curr_val))

    #     return traverse(0, 0, 0)

    # def minPathSum(self, grid: List[List[int]]) -> int:
    #     hori_len = len(grid[0])
    #     vert_len = len(grid)
        
    #     # Create a memoization table to store the computed results
    #     memo = [[-1] * hori_len for _ in range(vert_len)]
        
    #     def traverse(i, j):
    #         if i == vert_len - 1 and j == hori_len - 1:
    #             return grid[i][j]
            
    #         if i == vert_len or j == hori_len:
    #             return float('inf')
            
    #         if memo[i][j] != -1:
    #             return memo[i][j]
            
    #         curr_val = grid[i][j]
    #         right_sum = traverse(i, j + 1)
    #         down_sum = traverse(i + 1, j)
            
    #         min_sum = curr_val + min(right_sum, down_sum)
            
    #         memo[i][j] = min_sum
    #         return min_sum

    #     return traverse(0, 0)

    def minPathSum(self, grid: List[List[int]]) -> int:
        hori_len = len(grid[0])
        vert_len = len(grid)

        memo = [[-1] * hori_len for _ in range(vert_len)]
        def traverse(i, j):
            if i == 0 and j == 0:
                return grid[i][j]

            if i < 0 or j < 0:
                return float('inf')
            
            if memo[i][j] != -1:
                return memo[i][j]
            
            memo[i][j] = grid[i][j] + min(traverse(i - 1, j), traverse(i, j - 1))

            return memo[i][j]
        
        return traverse(vert_len - 1, hori_len - 1)
            
        

        
# @lc code=end

