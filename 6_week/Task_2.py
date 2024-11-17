# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=problem-list-v2&envId=sliding-window


def minSubArrayLen(target, nums):
    left = 0
    summa = 0
    window = 10**5 + 1

    for right in range(len(nums)):
        summa += nums[right]
        while summa >= target:
            window = min(window, right - left + 1)
            summa -= nums[left]
            left += 1
    if window != 10**5 + 1:
        return window
    return 0


nums = [2, 3, 1, 2, 4, 3]
target = 7
# target = 4
# nums = [1,4,4]
# target = 11
# nums = [1,1,1,1,1,1,1,1]
print(minSubArrayLen(target, nums))

""" My solution in LeetCode
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        summa = 0
        window = 10 ** 5 + 1

        for right in range(len(nums)):
            summa += nums[right]
            while summa >= target:
                window = min(window, right - left + 1)
                summa -= nums[left]
                left += 1
        if window != 10 ** 5 + 1:
            return window
        return 0
"""
