# Problem Statement:
# You are an ancient Egyptian mathematician, and you have been tasked with representing the fraction 6/14 as a sum of unique unit fractions. 
# You know that a unit fraction is a fraction with a numerator of 1 and a denominator of a positive integer. You also know that the sum of 
# any number of unit fractions is always a rational number.

# Example: The first step is to find the largest possible unit fraction that is less than or equal to 6/14. This fraction is 1/3. The remaining fraction 
# is 6/14 - 1/3 = 4/42. The largest possible unit fraction that is less than or equal to 4/42 is 1/11. The remaining fraction is 4/42 - 1/11 = 1/231.
# Therefore, the Egyptian fraction representation of 6/14 is 1/3 + 1/11 + 1/231.

# Exercise-1 :
# Input: 6 14
# Output: 3 11 231

# Exercise-2 :
# Input: 3 4
# Output: 2 4

import math
def getEF(num, den):
    str = ""
    op = getEFU(num, den, [])
    for denom in op:
        str += "1/{0} + ".format(denom)
    strCopy = str[:-3]
    return strCopy
def getEFU(num, den, loD):
    if num == 0:
        return loD
    newDenom = math.ceil(den/num)
    loD.append(newDenom)
    loD = getEFU(num*newDenom-den, newDenom*den, loD)
    return loD
    
n = int(input())
d = int(input())
res = getEF(n, d)
dens = [int(fraction.split("/")[1]) for fraction in res.split(" + ")]
for i in dens:
    print(i)