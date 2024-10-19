# 12. Integer to Roman
# https://leetcode.com/problems/integer-to-roman/description/?envType=problem-list-v2&envId=hash-table


def intToRoman(num):
    roman = {}
    roman[1] = "I"
    roman[5] = "V"
    roman[10] = "X"
    roman[50] = "L"
    roman[100] = "C"
    roman[500] = "D"
    roman[1000] = "M"
    number = str(num)
    radix = len(number)
    result = ""
    for i in range(0, radix):
        rad = 10 ** (radix - 1 - i)
        if 1 <= int(number[i]) <= 3:
            result += roman[rad] * int(number[i])
        elif int(number[i]) == 4:
            result += roman[rad] + roman[5 * rad]
        elif 6 <= int(number[i]) <= 8:
            result += roman[5 * rad] + (roman[rad]) * (int(number[i]) - 5)
        elif int(number[i]) == 9:
            result += roman[rad] + roman[rad * 10]
        elif int(number[i]) == 5:
            result += roman[rad * int(number[i])]
    return result


n = int(input())
print(intToRoman(n))

""" My solution in LeetCode
class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {}
        roman[1] = 'I'
        roman[5] = 'V'
        roman[10] = 'X'
        roman[50] = 'L'
        roman[100] = 'C'
        roman[500] = 'D'
        roman[1000] = 'M'
        number = str(num)
        radix = len(number)
        result = ""
        for i in range(0, radix):
            rad = 10 ** (radix - 1 - i)
            if 1 <= int(number[i]) <= 3:
                result += roman[rad] * int(number[i])
            elif int(number[i]) == 4:
                result += roman[rad] + roman[5 * rad]
            elif 6 <= int(number[i]) <= 8:
                result += roman[5 * rad] + (roman[rad]) * (int(number[i]) - 5)
            elif int(number[i]) == 9:
                result += roman[rad] + roman[rad * 10]
            elif int(number[i]) == 5:
                result += roman[rad * int(number[i])]
        return result
"""
