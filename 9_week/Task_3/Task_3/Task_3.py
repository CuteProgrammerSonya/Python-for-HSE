# 129. Sum Root to Leaf Numbers
# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/?envType=problem-list-v2&envId=binary-tree&difficulty=MEDIUM%2CHARD

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    summa = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def calculateSum(node, summa):
            if not node:
                return 0
            summa = summa * 10 + node.val
            if not node.left and not node.right:
                return summa
            left_sum = calculateSum(node.left, summa)
            right_sum = calculateSum(node.right, summa)
            return left_sum + right_sum

        return calculateSum(root, 0)


root = TreeNode(1, TreeNode(2), TreeNode(3))
solution = Solution()
root = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
print(solution.sumNumbers(root))

""" My solution in LeetCode
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def calculateSum(node, summa):
            if not node:
                return 0
            summa = summa * 10 + node.val
            if not node.left and not node.right:
                return summa
            left_sum = calculateSum(node.left, summa)
            right_sum = calculateSum(node.right, summa)
            return left_sum + right_sum
        return calculateSum(root, 0)
"""
