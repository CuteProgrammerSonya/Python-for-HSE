# 8. String to Integer (atoi)
# https://leetcode.com/problems/string-to-integer-atoi/description/?envType=problem-list-v2&envId=string

def myAtoi(s):
    res = ""
    i = 0
    while i < len(s):
        if s[i].isdigit():
            res += s[i]
        elif (len(res) != 0 and s[i] == ' '):
            break
        elif (s[i] != ' ') and (s[i].isdigit() != True):
            if (len(res) != 0 and (s[i] == '+' or s[i] == '-')):
                break
            elif len(res) == 0 and (s[i] == '-' or s[i] == '+'):
                res += s[i]
            else:
                break
        i += 1
    if (len(res) == 0) or (res == "+") or (res == "-"):
        return 0
    else:
        if int(res) <= -2 ** 31:
            return -2 ** 31
        elif int(res) >= 2 ** 31 -1:
            return 2 ** 31 - 1
        else:
            return int(res)
    
s = input()
print(myAtoi(s))

""" My solution in LeetCode
class Solution:
    def myAtoi(self, s: str) -> int:
        res = ""
        i = 0
        while i < len(s):
            if s[i].isdigit():
                res += s[i]
            elif (len(res) != 0 and s[i] == ' '):
                break
            elif (s[i] != ' ') and (s[i].isdigit() != True):
                if (len(res) != 0 and (s[i] == '+' or s[i] == '-')):
                    break
                elif len(res) == 0 and (s[i] == '-' or s[i] == '+'):
                    res += s[i]
                else:
                    break
            i += 1
        if (len(res) == 0) or (res == "+") or (res == "-"):
            return 0
        else:
            if int(res) <= -2 ** 31:
                return -2 ** 31
            elif int(res) >= 2 ** 31 -1:
                return 2 ** 31 - 1
            else:
                return int(res)
"""
            