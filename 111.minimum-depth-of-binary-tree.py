#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left, right = self.minDepth(root.left), self.minDepth(root.right)
        
        if root.left and not root.right:
            return 1 + left
              
        if not root.left and root.right:
            return 1 + right
        
        return 1 + min(left, right)



# @lc code=end

