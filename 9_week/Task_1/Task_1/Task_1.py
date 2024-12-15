# 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/description/?envType=problem-list-v2&envId=binary-tree&difficulty=MEDIUM%2CHARD
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def check_valid(node, minimum=-(2**31) - 1, maximum=2**31):
            if node is None:
                return True
            if node.val <= minimum or node.val >= maximum:
                return False
            return check_valid(node.left, minimum, node.val) and check_valid(
                node.right, node.val, maximum
            )

        return check_valid(root)


# root = TreeNode(2, TreeNode(1), TreeNode(3))
root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
solution = Solution()
print(solution.isValidBST(root))

""" My solution in Leetcode
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        def check_valid(node, minimum = -2 ** 31 - 1, maximum = 2 ** 31):
            if node is None:
                return True
            if node.val <= minimum or node.val >= maximum:
                return False
            return (check_valid(node.left, minimum, node.val) and
                    check_valid(node.right, node.val, maximum))
        return check_valid(root)
"""
