# 438. Find All Anagrams in a String
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/?envType=problem-list-v2&envId=hash-table


def findAnagrams(s, p):
    pattern = {}
    res = []
    for i in range(0, len(p)):
        pattern[p[i]] = pattern.get(p[i], 0) + 1
    i = 0
    j = 0
    copy_pattern = {}
    while j < len(s):
        copy_pattern[s[j]] = copy_pattern.get(s[j], 0) + 1
        while j - i + 1 > len(p):
            copy_pattern[s[i]] -= 1
            if copy_pattern[s[i]] == 0:
                del copy_pattern[s[i]]
            i += 1
        if copy_pattern == pattern:
            res.append(i)
        j += 1
    return res


s = input()
p = input()
print(findAnagrams(s, p))

""" My solution in LeetCode:
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pattern = {}
        res = []
        for i in range(0, len(p)):
            pattern[p[i]] = pattern.get(p[i], 0) + 1
        i = 0
        j = 0
        copy_pattern = {}
        while j < len(s):
            copy_pattern[s[j]] = copy_pattern.get(s[j], 0) + 1
            while j - i + 1 > len(p):
                copy_pattern[s[i]] -= 1
                if copy_pattern[s[i]] == 0:
                    del copy_pattern[s[i]]
                i += 1
            if copy_pattern == pattern:
                res.append(i)
            j += 1
        return res
"""
