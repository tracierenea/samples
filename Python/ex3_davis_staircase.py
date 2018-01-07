#!/usr/bin/env python
#
# Author       : Tracie Conn
# Created      : Jan 6, 2018
#
# Tested with Python v3.5.2
#
######## Instructions
# Davis has staircases in his house and he likes to climb each 
# staircase 1, 2, or 3 steps at a time. Being a very precocious
# child, he wonders how many ways there are to reach the top of the
# staircase. Given the respective heights for each of the staircases
# in his house, find and print the number of ways he can climb each 
# staircase on a new line.

# Input Format: The first line contains a single integer, s, 
# denoting the number of staircases in his house. Each line of the
# subsequent lines contains a single integer, n, denoting the height
# of staircase i.
#
# Subtasks: 1 <= n <= 20 for 50% of maximum score
#

# Without memoization, this recursive function takes so long that the
# hackerrank submission test times out. So, the key here is to use
# a simple memoization implementation in the davis function.

davis_memo = {}
def davis(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    elif n not in davis_memo:
        davis_memo[n] = davis(n-1) + davis(n-2) + davis(n-3)
    return davis_memo[n]

# Get s, the number of staircases in the house
s = int(input().strip())
n_values = []
# n values, the number of steps in each staircase
for a0 in range(s):
    n = int(input().strip())
    n_values.append(n)
# call davis function for each case and print the results
for index in range(len(n_values)):
    print(davis(n_values[index]))