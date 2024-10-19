# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/description/?envType=problem-list-v2&envId=hash-table


def topKFrequent(nums, k):
    el_count = {}
    res = []
    j = 0
    for i in range(len(nums)):
        if nums[i] not in el_count:
            el_count[nums[i]] = nums.count(nums[i])
    el_count_sorted = dict(
        sorted(el_count.items(), key=lambda item: item[1], reverse=True)
    )
    for i in el_count_sorted.keys():
        if j == k:
            break
        res.append(i)
        j += 1
    return res


n = int(input())
k = int(input())
arr = []
for i in range(0, n):
    a = int(input())
    arr.append(a)
print(topKFrequent(arr, k))

""" My solution in LeetCode
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        el_count = {}
        res = []
        j = 0
        for i in range(len(nums)):
            if nums[i] not in el_count:
                el_count[nums[i]] = nums.count(nums[i])
        el_count_sorted = dict(
        sorted(el_count.items(), key=lambda item: item[1], reverse=True)
        )
        for i in el_count_sorted.keys():
            if (j == k):
                break
            res.append(i)
            j += 1
        return res
"""
