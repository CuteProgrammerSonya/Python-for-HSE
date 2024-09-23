# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/?envType=problem-list-v2&envId=string

def letterCombinations(digits):
    res = []
    numbers =  ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    digits = digits.replace("1", "")
    count = len(digits)
    if (count == 1):
        for i in numbers[int(digits[0]) - 2]:
            res.append(i)
    elif (count == 2):
        for i in numbers[int(digits[0]) - 2]:
            for j in numbers[int(digits[1]) - 2]:
                res.append(i + j)
    elif (count == 3):
        for i in numbers[int(digits[0]) - 2]:
            for j in numbers[int(digits[1]) - 2]:
                for k in numbers[int(digits[2]) - 2]:
                    res.append(i + j + k)
    elif (count == 4):
        for i in numbers[int(digits[0]) - 2]:
            for j in numbers[int(digits[1]) - 2]:
                for k in numbers[int(digits[2]) - 2]:
                    for l in numbers[int(digits[3]) - 2]:
                        res.append(i + j + k + l)
    return res
digits = input()
print(letterCombinations(digits))

""" My solution in LeetCode
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        numbers =  ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        count = len(digits)
        if (count == 1):
            for i in numbers[int(digits[0]) - 2]:
                res.append(i)
        elif (count == 2):
            for i in numbers[int(digits[0]) - 2]:
                for j in numbers[int(digits[1]) - 2]:
                    res.append(i + j)
        elif (count == 3):
            for i in numbers[int(digits[0]) - 2]:
                for j in numbers[int(digits[1]) - 2]:
                    for k in numbers[int(digits[2]) - 2]:
                        res.append(i + j + k)
        elif (count == 4):
            for i in numbers[int(digits[0]) - 2]:
                for j in numbers[int(digits[1]) - 2]:
                    for k in numbers[int(digits[2]) - 2]:
                        for l in numbers[int(digits[3]) - 2]:
                            res.append(i + j + k + l)
        return res
"""       
        
            
    