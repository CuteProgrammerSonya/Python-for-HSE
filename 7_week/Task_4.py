# 1052. Grumpy Bookstore Owner
# https://leetcode.com/problems/grumpy-bookstore-owner/description/?envType=problem-list-v2&envId=sliding-window&favoriteSlug=&difficulty=MEDIUM%2CHARD


def maxSatisfied(customers, grumpy, minutes):
    summa = 0
    start = 0
    end = 0
    max_buyers = 0
    for i in range(0, len(customers)):
        if 0 <= i <= minutes - 1:
            summa += customers[i]
        else:
            if grumpy[i] == 0:
                summa += customers[i]
    end = minutes - 1
    max_buyers = summa
    while end <= len(grumpy) - 2:
        if grumpy[start] == 1:
            summa -= customers[start]
        if grumpy[end + 1] == 1:
            summa += customers[end + 1]
        if summa >= max_buyers:
            max_buyers = summa
        start += 1
        end += 1
    return max_buyers


customers = [1, 0, 1, 2, 1, 1, 7, 5]
grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
minutes = 3
# customers = [1]
# grumpy = [0]
# minutes = 1
print(maxSatisfied(customers, grumpy, minutes))

""" My solution in LeetCode
class Solution:
    def maxSatisfied(self,
    customers:List[int],
    grumpy:List[int],
    minutes:int) -> int:
        summa = 0
        start = 0
        end = 0
        max_buyers = 0
        for i in range(0, len(customers)):
            if 0 <= i <= minutes - 1:
                summa += customers[i]
            else:
                if grumpy[i] == 0:
                    summa += customers[i]
        end = minutes - 1
        max_buyers = summa
        while end <= len(grumpy) - 2:
            if grumpy[start] == 1:
                summa -= customers[start]
            if grumpy[end + 1] == 1:
                summa += customers[end + 1]
            if summa >= max_buyers:
                max_buyers = summa
            start += 1
            end += 1
        return max_buyers
"""
