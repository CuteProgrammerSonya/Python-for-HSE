# 655. Print Binary Tree
# https://leetcode.com/problems/print-binary-tree/description/?envType=problem-list-v2&envId=binary-tree&favoriteSlug=&difficulty=MEDIUM%2CHARD

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def calculateHeight(node):
            if not node:
                return 0
            h_left = calculateHeight(node.left)
            h_right = calculateHeight(node.right)
            return 1 + max(h_left, h_right)

        height = calculateHeight(root)
        xx = height
        yy = 2**height - 1
        res = [["" for i in range(yy)] for j in range(xx)]

        def fill(node, x, y):
            if not node:
                return
            res[x][y] = str(node.val)
            if node.left:
                fill(node.left, x + 1, y - 2 ** (height - x - 2))
            if node.right:
                fill(node.right, x + 1, y + 2 ** (height - x - 2))

        if root:
            fill(root, 0, (yy - 1) // 2)
        return res


root = TreeNode(1, TreeNode(2), None)
solution = Solution()
print(solution.printTree(root))

""" My solution in LeetCode
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def calculateHeight(node):
            if not node:
                return 0
            return 1 + \
            max(calculateHeight(node.left), calculateHeight(node.right))
        height = calculateHeight(root)
        xx = height
        yy = 2 ** height - 1
        res = [["" for i in range(yy)] for j in range(xx)]
        def fill(node, x, y):
            if not node:
                return
            res[x][y] = str(node.val)
            if node.left:
                fill(node.left, x + 1, y - 2 ** (height - x - 2))
            if node.right:
                fill(node.right, x + 1, y + 2 ** (height - x - 2))
        if root:
            fill(root, 0, (yy - 1) // 2)
        return res
"""
