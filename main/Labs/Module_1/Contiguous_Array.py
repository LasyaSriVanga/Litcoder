# Problem Statement:
# Given a binary array 'nums', you are required to find the maximum length of a contiguous subarray that contains an equal number of 0s and 1s.

# Explanation:
# A binary array is an array that contains only 0s and 1s.
# A subarray is any subset of the indices of the original array.
# A contiguous subarray is a subarray in which all the elements are consecutive, i.e., any 
# element between the first and last element of the subarray is also part of it.

# Examples: Input :nums = [0, 1] Output : 2 Explanation: The longest contiguous subarray with an equal number of 0s and 1s is [0, 1] with a 
# length of 2. Input : nums = [0, 1, 0] Output : 2 Explanation: The longest contiguous subarray with an equal number of 0s and 1s is either 
# [0, 1] or [1, 0], both with a length of 2. Input : nums = [0, 0, 0, 1, 1, 1] Output : 6 Explanation: The longest contiguous subarray with an 
# equal number of 0s and 1s is [0, 0, 0, 1, 1, 1] with a length of 6. The problem requires finding the maximum length of a contiguous subarray 
# in the binary array 'nums' that contains an equal number of 0s and 1s.

# Important Note: Ensure that you save your solution before progressing to the next question and before submitting your answer.

# Exercise-1 ;
# Input : 
# 0 0 0 1 1 1 1 0

# Output :
# 8

# Exercise-2 :
# Input:
# 1 0 0 1 1 1 1 0

# Output:
# 4

import sys
from typing import List
def doSomething(nums: List[int]) -> int:
    count = {0:-1}
    max_len = count_diff = 0
    for i, num in enumerate(nums):
        count_diff += 1 if num == 1 else -1
        if count_diff in count:
            max_len = max(max_len, i-count[count_diff])
        else:
            count[count_diff] = i
    return max_len
input_string = input("")    
inputList = [int(x) for x in input_string.split()]
outputVal = doSomething(inputList)
print (outputVal)