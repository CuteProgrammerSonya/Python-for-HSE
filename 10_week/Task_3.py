# 654. Maximum Binary Tree
# https://leetcode.com/problems/maximum-binary-tree/description/?envType=problem-list-v2&envId=binary-tree&favoriteSlug=&difficulty=MEDIUM%2CHARD

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, num: List[int]) -> Optional[TreeNode]:
        def buildMax(arr):
            if not arr:
                return None
            mx = max(arr)
            i = arr.index(mx)
            fin = i + 1
            length = len(arr)
            root = TreeNode(mx, buildMax(arr[0:i]), buildMax(arr[fin:length]))
            return root

        return buildMax(num)


nums = [3, 2, 1, 6, 0, 5]
solution = Solution()
solution.constructMaximumBinaryTree(nums)

""" My solution in LeetCode
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) ->
    Optional[TreeNode]:
        def buildMax(arr):
            if not arr:
                return None
            maximum = max(arr)
            index = arr.index(maximum)
            root = TreeNode(
            maximum,
            buildMax(arr[0:index]),
            buildMax(arr[index + 1:len(arr)])
            )
            return root
        return buildMax(nums)
"""
