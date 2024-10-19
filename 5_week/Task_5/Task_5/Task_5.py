# 30. Substring with Concatenation of All Words
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/?envType=problem-list-v2&envId=hash-table


def findSubstring(s, words):
    if not s or not words:
        return []
    pattern = {}
    res = []
    length = len(words[0])
    k = len(words)
    total_length = length * k
    for word in words:
        pattern[word] = pattern.get(word, 0) + 1

    for i in range(len(s) - total_length + 1):
        copy_pattern = {}
        j = i
        while j < i + total_length:
            index = j + length
            word = s[j:index]
            if word in pattern:
                copy_pattern[word] = copy_pattern.get(word, 0) + 1
                if copy_pattern[word] > pattern[word]:
                    break
            else:
                break
            j += length
        if copy_pattern == pattern:
            res.append(i)
    return res


s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
words = ["fooo", "barr", "wing", "ding", "wing"]
print(findSubstring(s, words))

""" My solution in LeetCode
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        pattern = {}
        res = []
        l = len(words[0])
        k = len(words)
        total_length = l * k
        for word in words:
            pattern[word] = pattern.get(word, 0) + 1

        for i in range(len(s) - total_length + 1):
            copy_pattern = {}
            j = i
            while j < i + total_length:
                word = s[j:j + l]
                if word in pattern:
                    copy_pattern[word] = copy_pattern.get(word, 0) + 1
                    if copy_pattern[word] > pattern[word]:
                        break
                else:
                    break
                j += l
            if copy_pattern == pattern:
                res.append(i)
        return res
"""
