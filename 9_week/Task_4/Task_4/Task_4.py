# 988. Smallest String Starting From Leaf
# https://leetcode.com/problems/smallest-string-starting-from-leaf/description/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    res = ""

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def minimumString(node, res):
            if not node:
                return ""
            res = chr(node.val + 97) + res
            if not node.left and not node.right:
                return res
            if node.left:
                left_sum = minimumString(node.left, res)
            else:
                left_sum = ""
            if node.right:
                right_sum = minimumString(node.right, res)
            else:
                right_sum = ""
            if not left_sum:
                return right_sum
            if not right_sum:
                return left_sum
            return min(left_sum, right_sum)

        return minimumString(root, self.res)


# root = TreeNode(
#    0, TreeNode(1, TreeNode(3), TreeNode(4)),
#    TreeNode(2, TreeNode(3), TreeNode(4))
# )
# solution = Solution()
# root = TreeNode(
#    25, TreeNode(1, TreeNode(1), TreeNode(3)),
#    TreeNode(3, TreeNode(0), TreeNode(2))
# )
# print(solution.smallestFromLeaf(root))

""" My solution in LeetCode
class Solution:
    res = ""
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def minimumString(node, res):
            if not node:
                return ""
            res = chr(node.val + 97) + res
            if not node.left and not node.right:
                return res
            if node.left:
                left_sum = minimumString(node.left, res)
            else:
                left_sum = ""
            if node.right:
                right_sum = minimumString(node.right, res)
            else:
                right_sum = ""
            if not left_sum:
                return right_sum
            if not right_sum:
                return left_sum
            return min(left_sum, right_sum)
        return minimumString(root, self.res)
"""
