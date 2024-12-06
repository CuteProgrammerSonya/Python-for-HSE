# 658. Find K Closest Elements
# https://leetcode.com/problems/find-k-closest-elements/description/?envType=problem-list-v2&envId=sliding-window&favoriteSlug=&difficulty=MEDIUM%2CHARD


def findClosestElements(arr, k, x):
    start = 0
    end = len(arr) - 1
    while end - start + 1 > k:
        if x - arr[start] <= arr[end] - x:
            end -= 1
        else:
            start += 1
    fin = end + 1
    return arr[start:fin]


arr = [1, 2, 3, 4, 5]
k = 4
x = 3
arr = [1, 1, 2, 3, 4, 5]
k = 4
x = -1
print(findClosestElements(arr, k, x))

""" My solution in LeetCode
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        start = 0
        end = len(arr) - 1
        while end - start + 1 > k:
            if x - arr[start] <= arr[end] - x:
                end -= 1
            else:
                start += 1
        fin = end + 1
        return arr[start:fin]
"""
