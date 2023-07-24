#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            
            return left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left)
        return dfs(root.left, root.right)

    # def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    #     def walk_left(left_root):
    #         if left_root is None:
    #             return [None]
    #         return [left_root.val] + walk_left(left_root.left) + walk_left(left_root.right)

    #     def walk_right(right_root):
    #         if right_root is None:
    #             return [None]
    #         return [right_root.val] + walk_right(right_root.right) + walk_right(right_root.left)

    #     return walk_left(root) == walk_right(root)

        

# @lc code=end

