# 166. Fraction to Recurring Decimal
# https://leetcode.com/problems/fraction-to-recurring-decimal/description/?envType=problem-list-v2&envId=hash-table


def fractionToDecimal(numerator, denominator):
    result = ""
    if numerator < 0 and denominator > 0 or numerator > 0 and denominator < 0:
        result += "-"
    numerator = abs(numerator)
    denominator = abs(denominator)
    remainders = {}
    index = 0
    result += str(numerator // denominator)
    ost = numerator % denominator
    if ost == 0:
        return result
    result += "."
    index = len(result) - 1
    i = index + 1
    if ost not in remainders:
        remainders[ost] = str(i)
        ost *= 10
        result += str(ost // denominator)
        i += 1
    while 1:
        if ost % denominator in remainders:
            start = int(remainders[ost % denominator])
            result = result[:start] + "(" + result[start:] + ")"
            return result
        else:
            ost %= denominator
            if ost == 0:
                return result
            remainders[ost] = str(i)
            ost *= 10
            result += str(ost // denominator)
            i += 1


numerator = int(input())
denominator = int(input())
print(fractionToDecimal(numerator, denominator))

""" My solution in LeetCode
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        result = ""
        if (numerator < 0 and denominator > 0
        or numerator > 0 and denominator < 0):
            result += '-'
        numerator = abs(numerator)
        denominator = abs(denominator)
        remainders = {}
        index = 0
        result += str(numerator // denominator)
        ost = numerator % denominator
        if ost == 0:
            return result
        result += '.'
        index = len(result) - 1
        i = index + 1
        if ost not in remainders:
            remainders[ost] = str(i)
            ost *= 10
            result += str(ost // denominator)
            i += 1
        while(1):
            if ost % denominator in remainders:
                result = (
                result[: int(remainders[ost % denominator])]
                + "("
                + result[int(remainders[ost % denominator]) :]
                + ")"
                )
                return result
            else:
                ost %= denominator
                if ost == 0:
                    return result
                remainders[ost] = str(i)
                ost *= 10
                result += str(ost // denominator)
                i += 1
"""
