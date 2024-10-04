# 74. Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/description/?envType=problem-list-v2&envId=array


def searchMatrix(matrix, target):
    n = len(matrix)
    m = len(matrix[0])
    start = 0
    end = n * m - 1
    while start <= end:
        mid = (start + end) // 2
        if target == matrix[mid // m][mid % m]:
            return True
        if target > matrix[mid // m][mid % m]:
            start = mid + 1
        else:
            end = mid - 1
    return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
print(searchMatrix(matrix, target))

""" My solution in LeetCode
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        start = 0
        end = n * m - 1
        while(start <= end):
            mid = (start + end) // 2
            if (target == matrix[mid // m][mid % m]):
                return True
            if (target > matrix[mid // m][mid % m]):
                start = mid + 1
            else:
                end = mid - 1
        return False
"""
