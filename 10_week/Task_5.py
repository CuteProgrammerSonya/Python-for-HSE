# 508. Most Frequent Subtree Sum
# https://leetcode.com/problems/most-frequent-subtree-sum/description/?envType=problem-list-v2&envId=binary-tree&favoriteSlug=&difficulty=MEDIUM%2CHARD

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        summ_table = {}

        def sumSubtrees(root):
            if not root:
                return 0
            summa = root.val
            summa += sumSubtrees(root.left)
            summa += sumSubtrees(root.right)
            if summa not in summ_table:
                summ_table[summa] = 1
            else:
                summ_table[summa] += 1
            return summa

        sumSubtrees(root)
        max_frequency = max(summ_table.values())
        for i in summ_table:
            if summ_table[i] == max_frequency:
                res.append(i)
        return res


root = TreeNode(5, TreeNode(2), TreeNode(-3))
solution = Solution()
print(solution.findFrequentTreeSum(root))

""" My solution in LeetCode
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        summ_table = {}
        def sumSubtrees(root):
            if not root:
                return 0
            summa = root.val
            summa += sumSubtrees(root.left)
            summa += sumSubtrees(root.right)
            if summa not in summ_table:
                summ_table[summa] = 1
            else:
                summ_table[summa] += 1
            return summa
        sumSubtrees(root)
        max_frequency = max(summ_table.values())
        for i in summ_table:
            if summ_table[i] == max_frequency:
                res.append(i)
        return res
"""
