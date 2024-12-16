# 2196. Create Binary Tree From Descriptions
# https://leetcode.com/problems/create-binary-tree-from-descriptions/description/?envType=problem-list-v2&envId=binary-tree&difficulty=MEDIUM%2CHARD

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, desc: List[List[int]]) -> Optional[TreeNode]:
        tree = {}
        children = set()
        for i in range(0, len(desc)):
            if desc[i][0] not in tree:
                tree[desc[i][0]] = TreeNode(desc[i][0])
            if desc[i][1] not in tree:
                tree[desc[i][1]] = TreeNode(desc[i][1])
            if desc[i][2] == 1:
                tree[desc[i][0]].left = tree[desc[i][1]]
            else:
                tree[desc[i][0]].right = tree[desc[i][1]]
            children.add(desc[i][1])
        for node in tree:
            if node not in children:
                return tree[node]


# descriptions = [[20, 15, 1], [20, 17, 0], [50, 20, 1],
#               [50, 80, 0], [80, 19, 1]]
# solution = Solution()
# solution.createBinaryTree(descriptions)

""" My solution in LeetCode
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) ->
    Optional[TreeNode]:
        tree = {}
        children = set()
        for i in range(0, len(descriptions)):
            if descriptions[i][0] not in tree:
                tree[descriptions[i][0]] = TreeNode(descriptions[i][0])
            if descriptions[i][1] not in tree:
                tree[descriptions[i][1]] = TreeNode(descriptions[i][1])
            if descriptions[i][2] == 1:
                tree[descriptions[i][0]].left = tree[descriptions[i][1]]
            else:
                tree[descriptions[i][0]].right = tree[descriptions[i][1]]
            children.add(descriptions[i][1])
        for node in tree:
            if node not in children:
                return tree[node]
"""
