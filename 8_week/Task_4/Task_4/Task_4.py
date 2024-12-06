# 2730. Find the Longest Semi-Repetitive Substring
# https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/description/?envType=problem-list-v2&envId=sliding-window&favoriteSlug=&difficulty=MEDIUM%2CHARD


def longestSemiRepetitiveSubstring(s):
    res = 1
    length = 1
    j = -1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            if j != -1:
                length = i - j - 1
            j = i - 1
        length += 1
        if length >= res:
            res = length
    return res


s = "52233"
s = "5494"
s = "1111111"
print(longestSemiRepetitiveSubstring(s))

""" My solution in LeetCode:
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        res = 1
        length = 1
        j = -1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                if j != -1:
                    length = i - j - 1
                j = i - 1
            length += 1
            if length >= res:
                res = length
        return res
"""
