# Problem Statement:
# You are given a list of activities with their start and finish times. Each activity is represented as a pair of integers (start, finish), 
# where start represents the start time of the activity and finish represents the finish time. Your task is to implement a function maxActivities(arr) 
# that takes in an array of activity pairs and returns a new array containing the maximum number of non-overlapping activities that can be performed.

# Example 1 arr = [(1, 3), (2, 4), (3, 6), (5, 7), (8, 9)] the maximum number of non-overlapping activities that can be performed is 3, represented by 
# the activity pairs (1, 3), (5, 7), and (8, 9).

# Important Note: Ensure that you save your solution before progressing to the next question and before submitting your answer.

# Exercise-1 :
# Input:
# 6 1 3 0 5 5 8 2 4 6 7 9 9
# Note: Line -1 : event count Line -2 : start time Line -3 : end time
# Output: 1 2 3 4 5 7 8 9

# Exercise-2 :
# Input:
# 4 1020 1110 1330 1200 1300 1200 1430 1400
# Output:
# 1020 1300 1330 1430

def maxAct(arr):
    n = arr[0]
    start = arr[1]
    finish = arr[2]
    activities = list(zip(start, finish))
    
    if n <= 1:
        return activities
        
    activities.sort(key=lambda x: x[1])
    s_activities = [activities[0]]
    prev_f_time = activities[0][1]
    
    for i in range(1, n):
        curr_s_time, curr_f_time = activities[i]
        if curr_s_time >= prev_f_time:
            s_activities.append(activities[i])
            prev_f_time = curr_f_time
    return s_activities
    
def take_input():
    n = int(input())
    start = list(map(int, input().split()))
    finish = list(map(int, input().split()))
    return [n, start, finish]

input_data = take_input()
res = maxAct(input_data)
for activity in res:
    print(activity[0], activity[1])