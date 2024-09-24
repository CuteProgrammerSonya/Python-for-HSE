# 151. Reverse Words in a String
# https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=problem-list-v2&envId=string

def reverseWords(s):
    res = ""
    arr = []
    s = s.strip()
    for i in range(0, len(s)):
        if (s[i] != ' '):
            res += s[i]
        if (i + 1 < len(s)):
            if (s[i] != ' ' and s[i + 1] == ' '):
                arr.append(res)
                res = ""
        if (i + 1 == len(s)):
            if (s[i] != " "):
                arr.append(res)
                res = ""
    arr = arr[::-1]
    for i in range(0,  len(arr)):
        res += arr[i]
        if (i != len(arr) - 1):
            res += ' '
    return res
s = input()
print(reverseWords(s))

""" My solution in LeetCode
class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        arr = []
        s = s.strip()
        for i in range(0, len(s)):
            if (s[i] != ' '):
                res += s[i]
            if (i + 1 < len(s)):
                if (s[i] != ' ' and s[i + 1] == ' '):
                    arr.append(res)
                    res = ""
            if (i + 1 == len(s)):
                if (s[i] != " "):
                    arr.append(res)
                    res = ""
        arr = arr[::-1]
        for i in range(0,  len(arr)):
            res += arr[i]
            if (i != len(arr) - 1):
                res += ' '
        return res
"""
    
