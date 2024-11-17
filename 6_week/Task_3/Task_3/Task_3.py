# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=problem-list-v2&envId=sliding-window


def lengthOfLongestSubstring(s):
    symbols = {}
    left = 0
    right = 0
    window = 0
    while right < len(s):
        if s[right] not in symbols or not (left <= symbols[s[right]] <= right):
            symbols[s[right]] = right
            window = max(window, right - left + 1)
            right += 1
        elif s[right] in symbols and left <= symbols[s[right]] <= right:
            left = symbols[s[right]] + 1
            symbols[s[right]] = right
            right += 1
    return window


s = "abba"
print(lengthOfLongestSubstring(s))

""" My solution in LeetCode
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        symbols = {}
        left = 0
        right = 0
        window = 0
        while right < len(s):
            if (s[right] not in symbols or \
            not(left <= symbols[s[right]] <= right)):
                symbols[s[right]] = right
                window = max(window, right - left + 1)
                right += 1
            elif \
            (s[right] in symbols and left <= symbols[s[right]] <= right):
                left = symbols[s[right]] + 1
                symbols[s[right]] = right
                right += 1
        return window
"""
