#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def traverse(root, n=0):
            if not root:
                return False

            if n + root.val == targetSum:
                if not root.left and not root.right:
                    return True

            return traverse(root.left, n + root.val) or traverse(root.right, n + root.val)

        return traverse(root)
            
# @lc code=end

