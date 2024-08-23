# Problem Statement:
# The clumsy factorial of a positive integer n is obtained by applying a fixed rotation of operations, including multiplication '*', division '/', addition '+', and subtraction '-', to the integers in decreasing order. 
# The operations are applied according to the usual order of operations in arithmetic, where multiplication and division are done before addition and subtraction. For example, the clumsy factorial of n = 10 is calculated as follows: 
# clumsy(10) = 10 x 9 / 8 + 7 - 6 x 5 / 4 + 3 - 2 x 1. We use floor division for the division operation, meaning the result is rounded down to the nearest integer. 

# Your task is to implement a function that takes a positive integer n as input and returns the clumsy factorial of n.

# Important Note: Ensure that you save your solution before progressing to the next question and before submitting your answer.

# Exercise-1 :
# Input : 
# 5
# Output :
# 7

# Exercise-2 :
# Input:
# 10
# Output:
# 11

def clumsy(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 6
    else:
        return n * (n-1) // (n-2) + (n-3) - clumsy(n-4)
        
n = int(input())
print(clumsy(n))