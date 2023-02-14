""" 
    Given two non-negative integers low and high. 
    Return the count of odd numbers between low and high (inclusive).
"""

# Returns the count of odds between two non-negative numbs
def countOdds(low: int, high: int) -> int:
    return (high+1)//2 - (low//2)


print(countOdds(32,100000))

"""
at first I started using brute force which is as follows

x = range(low,high)
for i in x:
    if x%2 != 0:
       print(i)

First its wrong as it is printing the numbers not the COUNT of numbers
Second it will be slow if the range is high
Third we are still missing the high as it should high + 1

As leetCode expalined that between if low starts at odd the next odd will be + 1
The code that was given on top takes high+1 // 2 and keeps the Quotient
Takes low+//2 keeps the quotient 
the result of both is minus from high-low

"""
# How to find number of even numbers


