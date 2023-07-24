#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        result = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or (r, c) in visited or grid[r][c] == "0":
                return

            visited.add((r, c))
            dfs(r, c+1)
            dfs(r, c-1)
            dfs(r-1, c)
            dfs(r+1, c)

        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == "1":
                    dfs(i, j)
                    result += 1

        return result


# @lc code=end

