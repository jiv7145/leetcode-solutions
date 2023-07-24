#
# @lc app=leetcode id=1161 lang=python3
#
# [1161] Maximum Level Sum of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import Optional
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        store = {}
        level = 1
        while q:
            sum = 0
            for _ in range(len(q)):
                curr = q.popleft()
                val = curr.val
                print(val)
                sum += val
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
            store[level] = sum
            sum = 0
            level += 1
        print(store)
        return max(store, key=store.get)

# @lc code=end

