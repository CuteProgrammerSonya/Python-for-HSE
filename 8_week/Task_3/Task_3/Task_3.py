# 930. Binary Subarrays With Sum
# https://leetcode.com/problems/binary-subarrays-with-sum/description/?envType=problem-list-v2&envId=sliding-window&favoriteSlug=&difficulty=MEDIUM%2CHARD


def numSubarraysWithSum(nums, goal):
    count = 0
    max_count = 0
    arrs = {0: 1}
    for i in range(0, len(nums)):
        count += nums[i]
        if count - goal in arrs:
            max_count += arrs[count - goal]
        if count not in arrs:
            arrs[count] = 1
        else:
            arrs[count] += 1
    return max_count


nums = [1, 0, 1, 0, 1]
goal = 2
nums = [0, 0, 0, 0, 0]
goal = 0
print(numSubarraysWithSum(nums, goal))

""" My solution in LeetCode
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        max_count = 0
        arrs = {0: 1}
        for i in range(0, len(nums)):
            count += nums[i]
            if count - goal in arrs:
                max_count += arrs[count - goal]
            if count not in arrs:
                arrs[count] = 1
            else:
                arrs[count] += 1
        return max_count
"""
