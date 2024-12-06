# 424. Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/description/?envType=problem-list-v2&envId=sliding-window&favoriteSlug=&difficulty=MEDIUM%2CHARD


def characterReplacement(s, k):
    res = 0
    start = 0
    end = 0
    count = {}
    max_len = 0

    for i in range(0, len(s)):
        if s[end] not in count:
            count[s[end]] = 1
        else:
            count[s[end]] += 1
        if max_len < count[s[end]]:
            max_len = count[s[end]]
        if end - start - max_len + 1 > k:
            count[s[start]] -= 1
            start += 1
        if res < end - start + 1:
            res = end - start + 1
        end += 1

    return res


s = "AABABBA"
k = 1
s = "ABAB"
k = 2
print(characterReplacement(s, k))

""" My solution in LeetCode
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        start = 0
        end = 0
        count = {}
        max_len = 0

        for i in range(0, len(s)):
            if s[end] not in count:
                count[s[end]] = 1
            else:
                count[s[end]] += 1
            if max_len < count[s[end]]:
                max_len = count[s[end]]
            if end - start - max_len + 1 > k:
                count[s[start]] -= 1
                start += 1
            if res < end - start + 1:
                res = end - start + 1
            end += 1
        return res
"""
