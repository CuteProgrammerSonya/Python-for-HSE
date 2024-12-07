# 2904. Shortest and Lexicographically Smallest Beautiful String
# https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/description/?envType=problem-list-v2&envId=sliding-window&favoriteSlug=&difficulty=MEDIUM%2CHARD


def shortestBeautifulSubstring(s, k):
    res = float("inf")
    arr = []
    count = j = 0
    for i in range(len(s)):
        if s[i] == "1":
            arr.append(i)
            count += 1
        if count == k:
            fin = i + 1
            res = min(res, int(s[j:fin]))
            j = arr[0] + 1
            arr.pop(0)
            count -= 1
    if res == float("inf"):
        return ""
    else:
        return str(res)


s = "100011001"
k = 3
s = "1011"
k = 2
s = "000"
k = 1
print(shortestBeautifulSubstring(s, k))

""" My solution in LeetCode
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        res = float('inf')
        arr = []
        count = j = 0
        for i in range(len(s)):
            if s[i] == "1":
                arr.append(i)
                count += 1
            if count == k:
                res = min(res, int(s[j:i+1]))
                j = arr[0] + 1
                arr.pop(0)
                count -= 1
        if res == float('inf'):
            return ""
        else:
            return str(res)
"""
