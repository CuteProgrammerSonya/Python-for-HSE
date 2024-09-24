# 273. Integer to English Words
# https://leetcode.com/problems/integer-to-english-words/description/?envType=problem-list-v2&envId=string

def numberToWords(num):
    def numberToWords(self, num: int) -> str:
        size = 1000000
        value = ""
        numbers = [value] * size
        numbers[0] = "Zero"
        numbers[1] = "One"
        numbers[2] = "Two"
        numbers[3] = "Three"
        numbers[4] = "Four"
        numbers[5] = "Five"
        numbers[6] = "Six"
        numbers[7] = "Seven"
        numbers[8] = "Eight"
        numbers[9] = "Nine"
        numbers[10] = "Ten"
        numbers[11] = "Eleven"
        numbers[12] = "Twelve"
        for i in range (13, 20):
            if (i == 13):
                numbers[i] = "Thirteen"
            elif (i == 15):
                numbers[i] = "Fifteen"
            elif (i == 18):
                numbers[i] = "Eighteen"
            else:
                numbers[i] = numbers[i % 10] + "teen"
        numbers[20] = "Twenty"
        for i in range(21, 100):
            if (i % 10 == 0):
                if (i == 30):
                    numbers[i] = "Thirty"
                elif (i == 40):
                    numbers[i] = "Forty"
                elif (i == 50):
                    numbers[i] = "Fifty"
                elif (i == 80):
                    numbers[i] = "Eighty"
                else:
                    numbers[i] = numbers[i // 10] + "ty"
            else:
                numbers[i] = numbers[i // 10 * 10] + " " + numbers[i % 10]
        if (num <= 99):
            return numbers[num]
        for i in range(100, 1000):
            if (i % 100 == 0):
                numbers[i] = numbers[i // 100] + " " + "Hundred"
            else:
                numbers[i] = numbers[i // 100 * 100] + " " + numbers[i % 100]
        if (num <= 999):
            return numbers[num]
        """
        for i in range (1000, 1000000):
            if (i % 1000 == 0):
                numbers[i] = numbers[i // 1000] + " " + "Thousand"
            else:
                numbers[i] = numbers[i // 1000 * 1000] + " " + numbers[i % 1000]
        """
        if (num < 1000):
            return numbers[num]
        elif (1000 <= num < 1000000):
            if (num % 1000 == 0):
                numbers[num] = numbers[num // 1000] + " " + "Thousand"
            else:
                numbers[num] = numbers[num // 1000] + " " + "Thousand" + " " + numbers[num % 1000]
            return numbers[num]
        elif (1000000 <= num < 1000000000):
            if (num % 1000000 == 0):
                res = numbers[num // 1000000] + " " + "Million"
            else:
                res = numbers[num // 1000000] + " " + "Million" + " " + numbers[num % 1000000 // 1000] + " " + "Thousand" + " " + numbers[num % 1000000 % 1000]
            res = res.replace("Zero Thousand ", "")
            res = res.replace("Zero", "")
            res = res.strip()
            return res
        else:
            res = numbers[num // 1000000000] + " " + "Billion" + " " + numbers[num % 1000000000 // 1000000] + " " + "Million" + " " + numbers[num % 1000000000 % 1000000 // 1000] + " " + "Thousand" + " " + numbers[num % 1000000000 % 1000000 % 1000]
            res = res.replace("Zero Thousand ", "")
            res = res.replace("Zero Million ", "")
            res = res.replace("Zero", "")
            res = res.strip()
            return res    
num = int(input())
print(numberToWords(num))

""" My solution in LeetCode
class Solution:
    def numberToWords(self, num: int) -> str:
        size = 1000000
        value = ""
        numbers = [value] * size
        numbers[0] = "Zero"
        numbers[1] = "One"
        numbers[2] = "Two"
        numbers[3] = "Three"
        numbers[4] = "Four"
        numbers[5] = "Five"
        numbers[6] = "Six"
        numbers[7] = "Seven"
        numbers[8] = "Eight"
        numbers[9] = "Nine"
        numbers[10] = "Ten"
        numbers[11] = "Eleven"
        numbers[12] = "Twelve"
        for i in range (13, 20):
            if (i == 13):
                numbers[i] = "Thirteen"
            elif (i == 15):
                numbers[i] = "Fifteen"
            elif (i == 18):
                numbers[i] = "Eighteen"
            else:
                numbers[i] = numbers[i % 10] + "teen"
        numbers[20] = "Twenty"
        for i in range(21, 100):
            if (i % 10 == 0):
                if (i == 30):
                    numbers[i] = "Thirty"
                elif (i == 40):
                    numbers[i] = "Forty"
                elif (i == 50):
                    numbers[i] = "Fifty"
                elif (i == 80):
                    numbers[i] = "Eighty"
                else:
                    numbers[i] = numbers[i // 10] + "ty"
            else:
                numbers[i] = numbers[i // 10 * 10] + " " + numbers[i % 10]
        if (num <= 99):
            return numbers[num]
        for i in range(100, 1000):
            if (i % 100 == 0):
                numbers[i] = numbers[i // 100] + " " + "Hundred"
            else:
                numbers[i] = numbers[i // 100 * 100] + " " + numbers[i % 100]
        if (num <= 999):
            return numbers[num]
        if (num < 1000):
            return numbers[num]
        elif (1000 <= num < 1000000):
            if (num % 1000 == 0):
                numbers[num] = numbers[num // 1000] + " " + "Thousand"
            else:
                numbers[num] = numbers[num // 1000] + " " + "Thousand" + " " + numbers[num % 1000]
            return numbers[num]
        elif (1000000 <= num < 1000000000):
            if (num % 1000000 == 0):
                res = numbers[num // 1000000] + " " + "Million"
            else:
                res = numbers[num // 1000000] + " " + "Million" + " " + numbers[num % 1000000 // 1000] + " " + "Thousand" + " " + numbers[num % 1000000 % 1000]
            res = res.replace("Zero Thousand ", "")
            res = res.replace("Zero", "")
            res = res.strip()
            return res
        else:
            res = numbers[num // 1000000000] + " " + "Billion" + " " + numbers[num % 1000000000 // 1000000] + " " + "Million" + " " + numbers[num % 1000000000 % 1000000 // 1000] + " " + "Thousand" + " " + numbers[num % 1000000000 % 1000000 % 1000]
            res = res.replace("Zero Thousand ", "")
            res = res.replace("Zero Million ", "")
            res = res.replace("Zero", "")
            res = res.strip()
            return res    
"""
    

