# 1750. Minimum Length of String After Deleting Similar Ends
# https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/description/?envType=problem-list-v2&envId=string

def minimumLength(s):
    if len(s) == 1:
        return 1
    else:
        a = 0
        string_1 = ""
        string_2 = ""
        b = len(s) - 1
        while (a != b):
            string_1 += s[a]
            string_2 += s[b]
            print(s)
            if (string_1[-1] != string_2[-1]):
                break
            elif (string_1[-1] == string_2[-1]):
                while (a != b and a + 1 < len(s)):
                    if string_1[-1] == s[a + 1]:
                        string_1 += s[a + 1]
                        a += 1
                    else:
                        s = s[a + 1:]
                        a = 0
                        b = len(s) - 1
                        string_1 = ""
                        break
                while (b != a and b - 1 > -1):
                    if string_2[-1] == s[b - 1]:
                        string_2 += s[b - 1]
                        b -= 1
                    else:
                        s = s[:b]
                        string_2 = ""
                        b = len(s) - 1
                        a = 0
                        break
        a = 0
        b = len(s) - 1
        if ((a != b) and (s.count("a") == len(s) or s.count("b") == len(s) or s.count("c") == len(s))):
            return 0
        return len(s)
s = input()
print(minimumLength(s))

""" My solution in LeetCode
class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s) == 1:
            return 1
        else:
            a = 0
            string_1 = ""
            string_2 = ""
            b = len(s) - 1
            while (a != b):
                string_1 += s[a]
                string_2 += s[b]
                if (string_1[-1] != string_2[-1]):
                    break
                elif (string_1[-1] == string_2[-1]):
                    while (a != b and a + 1 < len(s)):
                        if string_1[-1] == s[a + 1]:
                            string_1 += s[a + 1]
                            a += 1
                        else:
                            s = s[a + 1:]
                            a = 0
                            b = len(s) - 1
                            string_1 = ""
                            break
                    while (b != a and b - 1 > -1):
                        if string_2[-1] == s[b - 1]:
                            string_2 += s[b - 1]
                            b -= 1
                        else:
                            s = s[:b]
                            string_2 = ""
                            b = len(s) - 1
                            a = 0
                            break
        a = 0
        b = len(s) - 1
        if ((a != b) and (s.count("a") == len(s) or s.count("b") == len(s) or s.count("c") == len(s))):
            return 0
        return len(s)
"""
 


