# Problem Statement:
# Given a 0-indexed integer array nums of length n and an integer k, you are allowed to perform an operation on any element by multiplying it by 2. 
# The goal is to find the maximum possible value of the bitwise OR operation performed on all elements in the nums array after applying the operation 
# at most k times.

# Note that the bitwise OR operation (|) between two integers a and b results in a new integer where each bit is set if it is set in either a or b.

# Important Note: Ensure that you save your solution before progressing to the next question and before submitting your answer.

# Example :
# INPUT [12,9] 1 OUTPUT 30

# Exercise-1 :
# Input : 
# 12 9
# 2
# Output :
# 57

# Exercise-2 :
# Input:
# 3 2 4
# 2
# Output:
# 19

def max_bwor(nums, k):
    for _ in range(k):
        max_unb = -1
        tar_index = -1
        
        for i, num in enumerate(nums):
            b_rep = bin(num)[2:][::-1]
            ubi = b_rep.find('0')
            
            if ubi > max_unb:
                max_unb = ubi
                tar_index = i
                
        if max_unb == -1:
            break
        nums[tar_index] *= 2
        
    res = 0
    for num in nums:
        res |= num
    return res
    
nums = list(map(int, input().split()))
k = int(input())

op = max_bwor(nums, k)
print(op)