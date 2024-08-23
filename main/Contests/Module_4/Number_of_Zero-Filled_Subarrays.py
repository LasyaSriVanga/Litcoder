# Problem Statement:
# You are given an integer array nums, and the task is to determine the number of subarrays within the given array that are filled entirely with zeros. 
# A subarray is defined as a contiguous and non-empty sequence of elements within the array. 
# Input: nums: A non-empty integer array of length n (1 <= n <= 10^5). Each element of the array nums is an integer. The integers in the array nums can be positive, negative, or zero. 
# Output: The output should be a single integer, representing the total number of subarrays in nums that consist of only zeros.

# Example :
# INPUT
# [1,3,0,0,2,0,0,4]
# OUTPUT
# 6

# Exercise-1 :
# Input : 
# 1 2 0 0 0 
# Output :
# 6

# Exercise-2 :
# Input:
# 1 0 0 2 0 3 0
# Output:
# 5

def count_zsa(nums):
    count = 0
    curr_count = 0
    
    for num in nums:
        if num == 0:
            curr_count += 1
            count += curr_count
        else:
            curr_count = 0
    return count
    
def main():
    user_input = input()
    nums = list(map(int, user_input.split()))
    output = count_zsa(nums)
    print(output)
    
if __name__ == "__main__":
    main()