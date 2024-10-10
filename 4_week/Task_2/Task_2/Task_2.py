# 75. Sort Colors
# https://leetcode.com/problems/sort-colors/description/?envType=problem-list-v2&envId=array


def sortColors(nums):
    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    count = 0
    i = 0
    j = 0
    n = len(nums)
    while count != 2:
        if i == n:
            count += 1
            i = j
        elif nums[i] != count:
            i += 1
        elif nums[i] == count:
            swap(nums, i, j)
            i += 1
            j += 1


n = int(input())
nums = []
for i in range(0, n):
    a = int(input())
    nums.append(a)
sortColors(nums)
print(nums)

""" My solution in LeetCode:
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]
        count = 0
        i = 0
        j = 0
        n = len(nums)
        while count != 2:
            if i == n:
                count += 1
                i = j
            elif nums[i] != count:
                i += 1
            elif nums[i] == count:
                swap(nums, i, j)
                i += 1
                j += 1
"""
