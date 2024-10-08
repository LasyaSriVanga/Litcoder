# Problem Statement:
# You have been tasked with developing an algorithm to validate a 9 x 9 Sudoku board. Your algorithm needs to verify the validity of the filled cells on the board, 
# adhering to the following conditions:

# Every row should contain the numbers 1-9 exactly once, without repetition. Every column should contain the numbers 1-9 exactly once, without repetition. 
# Each of the nine 3 x 3 sub-boxes within the grid should contain the numbers 1-9 exactly once, without repetition.

# Can you outline an algorithm or a step-by-step approach to determine if the given Sudoku board configuration is valid based on these conditions?

# Important Note: Ensure that you save your solution before progressing to the next question and before submitting your answer.

# Exercise-1 :
# Input :
# 9 5 3 . . 7 . . . . 6 . . 1 9 5 . . . . 9 8 . . . . 6 . 8 . . . 6 . . . 3 4 . . 8 . 3 . . 1 7 . . . 2 . . . 6 . 6 . . . . 2 8 . . . . 4 1 9 . . 5 . . . . 8 . . 7 9

# Output :
# YES

# Exercise-2 :
# Input:
# 9 5 3 . . 7 . . . . 5 . . 1 9 5 . . . . 9 8 . . . . 6 . 8 . . . 6 . . . 3 4 . . 8 . 3 . . 1 7 . . . 2 . . . 6 . 6 . . . . 2 8 . . . . 4 1 9 . . 5 . . . . 8 . . 7 9

# Output: 
# NO

def isValidSudoku(board):
    def isValidRow(board,row):
        used = [False]*9
        for i in range(9):
            if not isValidEntry(board[row][i], used):
                return False
        return True
    def isValidColumn(board,col):
        used = [False]*9
        for i in range(9):
            if not isValidEntry(board[i][col], used):
                return False
            return True
    def isValidSubgrid(board,startRow,startCol):
        used = [False]*9
        for i in range(3):
            for j in range(3):
                if not isValidEntry(board[startRow + i][startCol + j], used):
                    return False
        return True
    def isValidEntry(entry,used):
        if entry == '.':
            return True
        num = int(entry)-1
        if used[num]:
            return False
        used[num] = True
        return True
    for i in range(9):
        if not isValidRow(board,i) or not isValidColumn(board,i):
            return False
    for i in range(0,9,3):
        for j in range(0,9,3):
            if not isValidSubgrid(board,i,j):
                return False
    return True
n = int(input())
sudokuBoard = []
for i in range(n):
    row = input()
    sudokuBoard.append(list(row))
if isValidSudoku(sudokuBoard):
    print("YES")
else:
    print("NO")