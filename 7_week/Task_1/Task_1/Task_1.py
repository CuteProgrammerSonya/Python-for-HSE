# 904. Fruit Into Baskets
# https://leetcode.com/problems/fruit-into-baskets/description/?envType=problem-list-v2&envId=sliding-window&favoriteSlug=&difficulty=MEDIUM%2CHARD


def totalFruit(fruits):
    max_fruits = 0
    start = 0
    end = 0
    baskets = {}
    if len(fruits) == 1:
        return 1
    while end <= len(fruits) - 1:
        if fruits[end] not in baskets:
            if len(baskets) < 2:
                baskets[fruits[end]] = 1
            else:
                if sum(baskets.values()) >= max_fruits:
                    max_fruits = sum(baskets.values())
                while 1:
                    baskets[fruits[start]] -= 1
                    if baskets[fruits[start]] == 0:
                        del baskets[fruits[start]]
                        start += 1
                        break
                    start += 1
                baskets[fruits[end]] = 1
        else:
            baskets[fruits[end]] += 1
        if end == len(fruits) - 1:
            if sum(baskets.values()) >= max_fruits:
                max_fruits = sum(baskets.values())
        end += 1
    return max_fruits


fruits = [0, 1, 2, 2]
print(totalFruit(fruits))

""" My solution in LeetCode
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits = 0
        start = 0
        end = 0
        baskets = {}
        if len(fruits) == 1:
            return 1
        while end <= len(fruits) - 1:
            if fruits[end] not in baskets:
                if len(baskets) < 2:
                    baskets[fruits[end]] = 1
                else:
                    if sum(baskets.values()) >= max_fruits:
                        max_fruits = sum(baskets.values())
                    while(1):
                        baskets[fruits[start]] -= 1
                        if baskets[fruits[start]] == 0:
                            del baskets[fruits[start]]
                            start += 1
                            break
                        start += 1
                    baskets[fruits[end]] = 1
            else:
                baskets[fruits[end]] += 1
            if end == len(fruits) - 1:
                if sum(baskets.values()) >= max_fruits:
                    max_fruits = sum(baskets.values())
            end += 1
        return max_fruits
"""
