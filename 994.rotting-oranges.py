#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()
        num_fresh_oranges = 0
        depth = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    num_fresh_oranges += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and num_fresh_oranges > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc
                    if new_r >= 0 and new_c >= 0 and new_r < ROWS and new_c < COLS and grid[new_r][new_c] == 1:
                        q.append((new_r, new_c))
                        visited.add((new_r, new_c))
                        grid[new_r][new_c] = 2
                        num_fresh_oranges -= 1
            depth += 1
        print(grid)
        return -1 if num_fresh_oranges != 0 else depth

        
# @lc code=end

Solution().orangesRotting([[2,1,1], [1,1,0], [0,1,1]])