# 1343.
# Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/?envType=problem-list-v2&envId=sliding-window&favoriteSlug=&difficulty=MEDIUM%2CHARD


def numOfSubarrays(arr, k, threshold):
    count = 0
    start = 0
    end = 0
    summa = 0
    for i in range(0, k):
        summa += arr[i]
    if summa / k >= threshold:
        count += 1
    end = k - 1
    while end <= len(arr) - 2:
        summa -= arr[start]
        summa += arr[end + 1]
        if summa / k >= threshold:
            count += 1
        start += 1
        end += 1
    return count


# arr = [2,2,2,2,5,5,5,8]
# k = 3
# threshold = 4
arr = [11, 13, 17, 23, 29, 31, 7, 5, 2, 3]
k = 3
threshold = 5
print(numOfSubarrays(arr, k, threshold))

""" My solution in LeetCode
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        start = 0
        end = 0
        summa = 0
        for i in range(0, k):
            summa += arr[i]
        if summa / k >= threshold:
            count += 1
        end = k - 1
        while end <= len(arr) - 2:
            summa -= arr[start]
            summa += arr[end + 1]
            if summa / k >= threshold:
                count += 1
            start += 1
            end += 1
        return count
"""
