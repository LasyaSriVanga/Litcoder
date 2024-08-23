# Problem Statement:
# Given a string composed of 'L', 'R', and 'X' characters, such as "RXXLRXRXL", a move can be made by replacing either one 
# occurrence of "XL" with "LX" or one occurrence of "RX" with "XR". The task is to determine if it is possible to transform the 
# starting string, "start," into the ending string, "end," by a sequence of these moves. Return True only if such a sequence exists.

# Example 1: 
# Input: start = "RXXLRXRXL", end = "XRLXXRRLX" Output: true Explanation: The starting string can be transformed into the ending string using the following steps: RXXLRXRXL -> XRXLRXRXL -> XRLXRXRXL -> XRLXXRRXL -> XRLXXRRLX

# Example 2:
# Input: start = "LLR", end = "RRL" Output: false

# Important Note:* Ensure that you save your solution before progressing to the next question and before submitting your answer.*

# Exercise-1 :
# Input: RXXLRXRXL XRLXXRRLX
# Output: true

# Exercise-2 :
# Input: RXXL XRLX
# Output: true

def canTm(start, end):
    if len(start) != len(end):
        return False
    i, j = 0, 0
    while i < len(start) and j < len(end):
        while i < len(start) and start[i] == 'X':
            i += 1
        while j < len(end) and end[j] == 'X':
            j += 1
        if (i < len(start)) != (j < len(end)):
            return False
        if i < len(start) and j < len(end):
            if start[i] != end[j] or (start[i] == 'L' and i < j) or (start[i] == 'R' and i > j):
                return False
            i += 1
            j += 1
            
    while i < len(start) and start[i] == 'X':
        i += 1
    while j < len(end) and end[j] == 'X':
        j += 1
    return i == len(start) and j ==len(end)
    
start_str = input("")
end_str = input("")
res = canTm(start_str, end_str)
print(res)