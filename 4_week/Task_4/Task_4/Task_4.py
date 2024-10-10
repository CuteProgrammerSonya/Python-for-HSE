# 164. Maximum Gap
# https://leetcode.com/problems/maximum-gap/description/?envType=problem-list-v2&envId=array


def maximumGap(nums):
    max_digits = 0
    for i in range(0, len(nums)):
        if len(str(nums[i])) >= max_digits:
            max_digits = len(str(nums[i]))
    base = 10
    arr = [[] for i in range(0, base)]
    for i in range(0, max_digits):
        for element in nums:
            digit = (element // base**i) % base
            arr[digit].append(element)
        nums = [x for el in arr for x in el]
        arr = [[] for k in range(0, base)]
    max_gap = 0
    n = len(nums)
    for i in range(0, n - 1):
        if nums[i + 1] - nums[i] >= max_gap:
            max_gap = nums[i + 1] - nums[i]
    return max_gap


n = int(input())
nums = []
for i in range(0, n):
    a = int(input())
    nums.append(a)
print(maximumGap(nums))

""" My solution in LeetCode
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        max_digits = 0
        for i in range(0, len(nums)):
            if len(str(nums[i])) >= max_digits:
                max_digits = len(str(nums[i]))
        base = 10
        arr = [[] for i in range(0, base)]
        for i in range(0, max_digits):
            for element in nums:
                digit = (element // base ** i) % base
                arr[digit].append(element)
            nums = [x for el in arr for x in el]
            arr = [[] for k in range(0, base)]
        max_gap = 0
        n = len(nums)
        for i in range(0, n - 1):
            if (nums[i + 1] - nums[i] >= max_gap):
                max_gap = nums[i + 1] - nums[i]
        return max_gap
"""
