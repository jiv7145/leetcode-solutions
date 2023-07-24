#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_dupe(lst):
            lst = [x for x in lst if x != '.']
            return len(set(lst)) != len(lst)
        
        def is_row_valid(b):
            for row in b:
                if is_dupe(row):
                    return False
            return True
        
        def is_column_valid(b):
            b = list(zip(*b))
            for col in b:
                if is_dupe(col):
                    return False
            return True
        
        def get_squares(b):
            result = []
            temp = []
            for i in range(0, 9, 3):
                for j in range(0, 9, 3):
                    for x in range(3):
                        for y in range(3):
                            temp.append(b[i+x][j+y])
                    result.append(temp)
                    temp = []
            return result
        
        def is_squares_valid(b):
            b = get_squares(b)
            for row in b:
                if is_dupe(row):
                    return False
            return True
        
        return is_column_valid(board) and is_row_valid(board) and is_squares_valid(board)
        
# @lc code=end

