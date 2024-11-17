# 567. Permutation in String
# https://leetcode.com/problems/permutation-in-string/description/?envType=problem-list-v2&envId=sliding-window


def checkInclusion(s1, s2):
    if len(s2) < len(s1):
        return False
    pattern = {}
    for i in range(0, len(s1)):
        if s1[i] in pattern:
            pattern[s1[i]] += 1
        else:
            pattern[s1[i]] = 1
    window = len(s1)
    substr = {}
    for i in range(0, window):
        if s2[i] in substr:
            substr[s2[i]] += 1
        else:
            substr[s2[i]] = 1
    if all(substr.get(char, 0) == pattern.get(char, 0) for char in pattern):
        return True
    for i in range(window, len(s2)):
        if s2[i] in substr:
            substr[s2[i]] += 1
        else:
            substr[s2[i]] = 1

        substr[s2[i - window]] -= 1
        if substr[s2[i - window]] == 0:
            del substr[s2[i - window]]

        if all(substr.get(c, 0) == pattern.get(c, 0) for c in pattern):
            return True

    return False


# s1 = "ab"
# s2 = "eidbaooo"
# s1 = "ab"
# s2 = "eidboaoo"
s1 = "a"
s2 = "ab"
print(checkInclusion(s1, s2))

""" My solution in LeetCode
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        pattern = {}
        if len(s2) < len(s1):
            return False
        for i in range(0, len(s1)):
            if s1[i] in pattern:
                pattern[s1[i]] += 1
            else:
                pattern[s1[i]] = 1
        window = len(s1)
        substr = {}
        for i in range(0, window):
            if s2[i] in substr:
                substr[s2[i]] += 1
            else:
                substr[s2[i]] = 1
        if all(substr.get(char, 0) == pattern.get(char, 0) \
        for char in pattern):
            return True
        for i in range(window, len(s2)):
            if s2[i] in substr:
                substr[s2[i]] += 1
            else:
                substr[s2[i]] = 1
            substr[s2[i - window]] -= 1
            if substr[s2[i - window]] == 0:
                del substr[s2[i - window]]

            if all(substr.get(char, 0) == pattern.get(char, 0) \
            for char in pattern):
                return True
        return False
"""
