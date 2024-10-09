# 41. First Missing Positive
# https://leetcode.com/problems/first-missing-positive/description/?envType=problem-list-v2&envId=array


def firstMissingPositive(nums):
    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(nums)
    for i in range(0, n):
        while 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
            swap(nums, i, nums[i] - 1)
    for i in range(0, n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1


n = int(input())
arr = []
for i in range(0, n):
    a = int(input())
    arr.append(a)
print(firstMissingPositive(arr))

""" My solurion in LeetCode:
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]
        n = len(nums)
        for i in range(0, n):
            while 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                swap(nums, i, nums[i] - 1)
        for i in range(0, n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
"""
