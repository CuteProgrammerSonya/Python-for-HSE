# 187. Repeated DNA Sequences
# https://leetcode.com/problems/repeated-dna-sequences/description/?envType=problem-list-v2&envId=sliding-window&favoriteSlug=&difficulty=MEDIUM%2CHARD


def findRepeatedDnaSequences(s):
    res = []
    dna = {}
    window = 10
    if len(s) < window:
        return res
    string = ""
    for i in range(0, window):
        string += s[i]
    dna[string] = 1
    start = 0
    end = window - 1
    while end <= len(s) - 1:
        start += 1
        end += 1
        fin = end + 1
        string = s[start:fin]
        if string in dna:
            dna[string] += 1
        else:
            dna[string] = 1
    for i in dna:
        if dna[i] > 1:
            res.append(i)
    return res


s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(findRepeatedDnaSequences(s))

""" My solution in LeetCode
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = []
        dna = {}
        window = 10
        if len(s) < window:
            return res
        string = ""
        for i in range(0, window):
            string += s[i]
        dna[string] = 1
        start = 0
        end = window - 1
        while end <= len(s) - 1:
            start += 1
            end += 1
            fin = end + 1
            string = s[start:fin]
            if string in dna:
                dna[string] += 1
            else:
                dna[string] = 1
        for i in dna:
            if dna[i] > 1:
                res.append(i)
        return res
"""
