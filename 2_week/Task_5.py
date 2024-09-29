# 165. Compare Version Numbers
# https://leetcode.com/problems/compare-version-numbers/description/?envType=problem-list-v2&envId=string

def compareVersion(version1, version2):
    v_1 = version1.split('.')
    v_2 = version2.split('.')
    i = 0
    while i < len(v_1) and i < len(v_2):
            if int(v_1[i]) == int(v_2[i]):
                i += 1
                continue
            if int(v_1[i]) < int(v_2[i]):
                return -1
            else:
                return 1
    while i < len(v_1):
        if int(v_1[i]):
            return 1
        i += 1
    while i < len(v_2):
         if int(v_2[i]):
            return -1
         i +=1
    return 0

str_1 = input()
str_2 = input()
print(compareVersion(str_1, str_2))

""" My solution in LeetCode
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v_1 = version1.split('.')
        v_2 = version2.split('.')
        i = 0
        while i < len(v_1) and i < len(v_2):
            if int(v_1[i]) == int(v_2[i]):
                i += 1
                continue
            if int(v_1[i]) < int(v_2[i]):
                return -1
            else:
                return 1
        while i < len(v_1):
            if int(v_1[i]):
                return 1
            i += 1
        while i < len(v_2):
            if int(v_2[i]):
                return -1
            i +=1
        return 0
"""