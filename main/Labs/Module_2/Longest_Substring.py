# Problem Statement:
# You are tasked with developing a function that finds the length of the longest substring without repeating characters in a given string s. 
# Consider different scenarios involving various characters in the input string.

# Scenario: String with No Repeating Characters Input: "abcdef" Expected Output: 6 Explanation: In this scenario, the input string contains 
# no repeating characters, so the entire string itself is the longest substring without repeating characters.

# Scenario: String with Repeating Characters Input: "abccba" Expected Output: 3 Explanation: In this case, the longest substring without repeating 
# characters is "abc" with a length of 3. The characters 'c' and 'b' are repeated, so the substring ends at the first occurrence of the repeated character

# Important Note: Ensure that you save your solution before progressing to the next question and before submitting your answer.

# Exercise-1 Input : pqrsstu
# Output : 4

# Exercise-2 Input: abbedfgi
# Output: 6

import sys
def longestSubstring(s):
    lastIdx = {}
    start = 0
    longest = 0
    
    for i in range(len(s)):
        if s[i] in lastIdx:
            start = max(start, lastIdx[s[i]]+1)
        lastIdx[s[i]] = i
        longest = max(longest, i-start+1)
    print(longest)
string = input()
longestSubstring(string)