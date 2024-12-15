# 102. Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/?envType=problem-list-v2&envId=binary-tree&difficulty=MEDIUM%2CHARD

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        level_arr = []
        if not root:
            return res

        def moveLevels(nodes, level_arr):
            if not nodes:
                return
            next_level = []  # nodes
            level = []  # values
            for node in nodes:
                level.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append(level)
            moveLevels(next_level, level_arr)

        arr = [root]
        moveLevels(arr, level_arr)
        return res


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
root = TreeNode(1)
solution = Solution()
print(solution.levelOrder(root))

""" My solution in LeetCode
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        level_arr = []
        if not root:
           return res
        def moveLevels(nodes, level_arr):
            if not nodes:
                return
            next_level = [] # nodes
            level = [] # values
            for node in nodes:
                level.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append(level)
            moveLevels(next_level, level_arr)
        arr = [root]
        moveLevels(arr, level_arr)
        return res
"""
