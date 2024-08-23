# Problem Statement:
# On the first day, one person discovers a secret.

# You are given two integers, delay and forget. Each person will share the secret with a new person every day, starting from delay days after discovering the secret. 
# Additionally, each person will forget the secret days after discovering it. It means they cannot share the secret on the same day they forget it or on any day afterward.

# Your task is to find the number of people who know the secret at the end of day n.

# Important Note: Ensure that you save your solution before progressing to the next question and before submitting your answer.

# Example :
# INPUT
# 6
# 2
# 4
# Note: 
# Line 1 :  number of days secret get spread
# Line 2: delay day
# Line 3 : forgetting day
# OUTPUT
# 5

# Exercise-1 :
# Input : 
# 4
# 1
# 3
# Output:
# 6

# Exercise-2 :
# Input:
# 3
# 2
# 3
# Output:
# 2

def cpws(n, delay, forget):
    kp = 0
    sk = [0] * (n+1)
    
    for day in range(1, n+1):
        if day >= delay:
            kp += sk[day - delay]
        if day not in forget:
            sk[day] = kp+1
    return sum(sk)
    
n = int(input())
delay = int(input())
forget = list(map(int, input().split()))

res = cpws(n, delay, forget)
print(res)