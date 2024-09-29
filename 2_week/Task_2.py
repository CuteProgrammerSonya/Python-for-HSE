# 402. Remove K Digits
# https://leetcode.com/problems/remove-k-digits/description/?envType=problem-list-v2&envId=string

def removeKdigits(num, k):
    temp = ""
    for i in range(0, len(num)):
        while temp != "" and k != 0 and int(temp[-1]) > int(num[i]):
            temp = temp[0:-1]
            k -= 1
        temp += num[i]
    if k != 0:
        res = temp[:-k]
    else:
        res = temp
    return res.lstrip('0') or '0'

k = int(input())
num = input()
print(removeKdigits(num, k))

""" My solution in LeetCode
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        temp = ""
        for i in range(0, len(num)):
            while temp != "" and k != 0 and int(temp[-1]) > int(num[i]):
                temp = temp[0:-1]
                k -= 1
            temp += num[i]
        if k != 0:
            res = temp[:-k]
        else:
            res = temp
        return res.lstrip('0') or '0'
"""

        
