# 179 Largest Number
# https://leetcode.com/problems/largest-number/description/?envType=problem-list-v2&envId=string

from functools import cmp_to_key

def largestNumber(nums):
    strs = []    
    for i in range (0, len(nums)):
        strs.append(str(nums[i]))
        
    def comparator(a, b):
            if a + b > b + a:
                return -1  
            elif a + b < b + a:
                return 1 
            else:
                return 0
        
    strs.sort(key=cmp_to_key(comparator))
    res = ''.join(strs)
    if res[0] == '0':
        return '0'
    else:
        return res

nums = []
n = int(input())
for i in range(0, n):
    a = int(input())
    nums.append(a)
print(largestNumber(nums))

""" My solution in LeetCode
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = []    
        for i in range (0, len(nums)):
            strs.append(str(nums[i]))
    
        def comparator(a, b):
            if a + b > b + a:
                return -1  
            elif a + b < b + a:
                return 1 
            else:
                return 0
    
        strs.sort(key=cmp_to_key(comparator))
        res = ''.join(strs)
        if res[0] == '0':
            return '0'
        else:
            return res
"""