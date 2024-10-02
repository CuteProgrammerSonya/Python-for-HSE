# 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/description/?envType=problem-list-v2&envId=array


def isValidSudoku(board):
    def is_true(elem, i, j):
        if board[i].count(elem) > 1:
            return False
        for k in range(0, len(board)):
            if k != i:
                if board[k][j] == elem:
                    return False
        start_i = i // 3 * 3
        start_j = j // 3 * 3
        for m in range(start_i, start_i + 3):
            for n in range(start_j, start_j + 3):
                if m != i and n != j:
                    if board[m][n] == elem:
                        return False
        return True

    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] != ".":
                if not (is_true(board[i][j], i, j)):
                    return False
    return True


board = [[] for i in range(0, 9)]
for i in range(0, 9):
    for k in range(0, 9):
        j = input()
        board[i].append(j)
print(isValidSudoku(board))

""" My solution in LeetCode
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_true(elem, i, j):
            if board[i].count(elem) > 1:
                return False
            for k in range(0, len(board)):
                if k != i:
                    if board[k][j] == elem:
                        return False
            start_i = i // 3 * 3
            start_j = j // 3 * 3
            for m in range(start_i, start_i + 3):
                for n in range(start_j, start_j + 3):
                    if m != i and n != j:
                        if board[m][n] == elem:
                            return False
            return True
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if board[i][j] != ".":
                    if (not(is_true(board[i][j], i, j))):
                        return False
        return True
"""
