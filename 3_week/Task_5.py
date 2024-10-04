# 48. Rotate Image
# https://leetcode.com/problems/rotate-image/description/?envType=problem-list-v2&envId=array


def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(matrix)
print(matrix)

""" My solution in LeetCode
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
"""
