# 450. Delete Node in a BST
# https://leetcode.com/problems/delete-node-in-a-bst/description/?envType=problem-list-v2&envId=binary-tree&difficulty=MEDIUM%2CHARD

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int):
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:  # key == root
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                element = self.findMin(root.right)
                root.val = element.val
                root.right = self.deleteNode(root.right, element.val)
        return root

    def findMin(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node


root = TreeNode(
    5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7))
)
key = 3
solution = Solution()
solution.deleteNode(root, key)

""" My solution in LeetCode
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int)\
   -> Optional[TreeNode]:
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else: # key == root
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                element = self.findMin(root.right)
                root.val = element.val
                root.right = self.deleteNode(root.right, element.val)
        return root
    def findMin(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node
"""
