# 78. Subsets

# https://leetcode.com/problems/subsets/?envType=problem-list-v2&envId=array


def subsets(nums):
    sets = []
    for i in range(0, 2 ** len(nums)):
        arr = []
        for j in range(0, len(nums)):
            if (i >> j) & 1:
                arr.append(nums[j])
        sets.append(arr)
    return sets


n = int(input())
nums = []
for i in range(0, n):
    a = int(input())
    nums.append(a)
print(subsets(nums))

""" My solution in LeetCode
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = []
        for i in range(0, 2 ** len(nums)):
            arr = []
            for j in range(0, len(nums)):
                if (i >> j) & 1:
                    arr.append(nums[j])
            sets.append(arr)
        return sets
"""
