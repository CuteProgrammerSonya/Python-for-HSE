# 120. Triangle
# https://leetcode.com/problems/triangle/description/?envType=problem-list-v2&envId=array


def minimumTotal(triangle):
    dp = [[0] * len(row) for row in triangle]
    dp[0][0] = triangle[0][0]
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = dp[i - 1][j] + triangle[i][j]
            elif j == len(triangle[i]) - 1:
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

    return min(dp[-1])


triangle = [[2], [3, 4], [2, 2, 5], [1, 1, 1, 6], [4, 5, 6, 7, 8]]
print(minimumTotal(triangle))

""" Recursive solution
def minimumTotal(triangle):
    summa = 0
    def counter(first_index_i, first_index_j, summa):
        summa = triangle[first_index_i][first_index_j]
        for i in range(first_index_i + 1, len(triangle)):
            summa +=
            min(counter(i, first_index_j, summa),
            counter(i, first_index_j + 1, summa))
            return summa
        return summa
    res = counter(0, 0, summa)
    return res
"""

""" My solution in LeetCode
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[0] * len(row) for row in triangle]
        dp[0][0] = triangle[0][0]

        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

        return min(dp[-1])
"""
