# 1695. Maximum Erasure Value
# https://leetcode.com/problems/maximum-erasure-value/description/?envType=problem-list-v2&envId=sliding-window


def maximumUniqueSubarray(nums):
    symbols = {}
    left = 0
    right = 0
    window = 0
    summ = 0
    while right < len(nums):
        if (nums[right] not in symbols) or (
            not (left <= symbols[nums[right]] <= right)
        ):
            symbols[nums[right]] = right
            window = max(window, right - left + 1)
            n = right + 1
            summ = max(summ, sum(nums[left:n]))
            right += 1
        elif nums[right] in symbols and left <= symbols[nums[right]] <= right:
            left = symbols[nums[right]] + 1
            symbols[nums[right]] = right
            right += 1
    return summ


# nums = [4,2,4,5,6]
nums = [5, 2, 1, 2, 5, 2, 1, 2, 5]
print(maximumUniqueSubarray(nums))

""" My solution in LeetCode
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        symbols = {}
        left = 0
        right = 0
        window = 0
        summ = 0
        while right < len(nums):
            if nums[right] not in symbols or\
           not (left <= symbols[nums[right]] <= right):
                symbols[nums[right]] = right
                window = max(window, right - left + 1)
                summ = max(summ, sum(nums[left:right + 1]))
                right += 1
            elif nums[right] in symbols and\
           left <= symbols[nums[right]] <= right:
                left = symbols[nums[right]] + 1
                symbols[nums[right]] = right
                right += 1
        return summ
"""
