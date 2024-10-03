# 54. Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/description/?envType=problem-list-v2&envId=array


def spiralOrder(matrix):
    m = len(matrix)
    n = len(matrix[0])
    res = []
    start_i = 0
    start_j = 0

    def process(start_i, start_j, fin_i, fin_j):
        for j in range(start_j, fin_j):
            res.append(matrix[start_i][j])
        if start_i == fin_i - 1:
            return
        for i in range(start_i + 1, fin_i):
            res.append(matrix[i][fin_j - 1])
        for j in range(fin_j - 2, start_j - 1, -1):
            res.append(matrix[fin_i - 1][j])
        if start_j == fin_j - 1:
            return
        for i in range(fin_i - 2, start_i, -1):
            res.append(matrix[i][start_j])

    while start_i < m and start_j < n:
        process(start_i, start_j, m, n)
        start_i += 1
        start_j += 1
        m -= 1
        n -= 1
    return res


m = int(input())
n = int(input())
matrix = [[] for i in range(0, m)]
for i in range(0, len(matrix)):
    for j in range(0, n):
        a = int(input())
        matrix[i].append(a)
print(matrix)
print(spiralOrder(matrix))

""" My solution in LeetCode
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        res = []
        start_i = 0
        start_j = 0
        def process(start_i, start_j, fin_i, fin_j):
            for j in range(start_j , fin_j):
                res.append(matrix[start_i][j])
            if start_i == fin_i - 1:
                return
            for i in range(start_i + 1, fin_i):
                res.append(matrix[i][fin_j - 1])
            for j in range(fin_j - 2, start_j - 1, -1):
                res.append(matrix[fin_i - 1][j])
            if start_j == fin_j - 1:
                return
            for i in range(fin_i - 2, start_i, -1):
                res.append(matrix[i][start_j])
        while (start_i < m and start_j < n):
            process(start_i, start_j, m, n)
            start_i += 1
            start_j += 1
            m -= 1
            n -= 1
        return res
"""
