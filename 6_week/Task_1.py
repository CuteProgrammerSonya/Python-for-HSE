# 2090. K Radius Subarray Averages
# https://leetcode.com/problems/k-radius-subarray-averages/description/?envType=problem-list-v2&envId=sliding-window


def getAverages(nums, k):
    res = [-1 for i in range(len(nums))]
    window = k * 2 + 1
    if window > len(nums):
        return res
    medium = k
    summa = 0
    for i in range(0, window):
        summa += nums[i]
    res[medium] = summa // window
    for i in range(1, len(nums)):
        if i + window - 1 <= len(nums) - 1:
            medium += 1
            summa -= nums[i - 1]
            summa += nums[i + window - 1]
            res[medium] = summa // window
        else:
            break
    return res


nums = [8]
k = 100000
print(getAverages(nums, k))

""" My solution in LeetCode
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
            res = [-1 for i in range(len(nums))]
            window = k * 2 + 1
            if window > len(nums):
                return res
            medium = k
            summa = 0
            for i in range(0, window):
                summa += nums[i]
            res[medium] = summa // window
            for i in range(1, len(nums)):
                if i + window - 1 <= len(nums) - 1:
                    medium += 1
                    summa -= nums[i - 1]
                    summa += nums[i + window - 1]
                    res[medium] = summa // window
                else:
                    break
            return res
"""
