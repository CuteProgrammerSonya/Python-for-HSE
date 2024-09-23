# 43. Multiply Strings
# https://leetcode.com/problems/multiply-strings/description/?envType=problem-list-v2&envId=string

def multiply(num1, num2):
    number_1 = 0
    number_2 = 0
    number_3 = 0
    for i in range(0, len(num1)):
        if i == 0:
            number_1 += int(num1[i])
        else:
            number_1 *= 10;
            number_1 += int(num1[i])
    for i in range(0, len(num2)):
        if i == 0:
            number_2 += int(num2[i])
        else:
            number_2 *= 10
            number_2 += int(num2[i])
    number_3 = number_1 * number_2
    return str(number_3)
num_1 = input()
num_2 = input()
print(multiply(num_1, num_2))

""" My solution in LeetCode
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        number_1 = 0
        number_2 = 0
        number_3 = 0
        for i in range(0, len(num1)):
            if i == 0:
                number_1 += int(num1[i])
            else:
                number_1 *= 10;
                number_1 += int(num1[i])
        for i in range(0, len(num2)):
            if i == 0:
                number_2 += int(num2[i])
            else:
                number_2 *= 10
                number_2 += int(num2[i])
        number_3 = number_1 * number_2
        return str(number_3)
"""
