# 515. Find Largest Value in Each Tree Row
# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/?envType=problem-list-v2&envId=binary-tree&favoriteSlug=&difficulty=MEDIUM%2CHARD

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
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
            res.append(max(level))
            moveLevels(next_level, level_arr)

        arr = [root]
        moveLevels(arr, level_arr)
        return res


root = TreeNode(
    1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9))
)
solution = Solution()
print(solution.largestValues(root))
