#!/usr/bin/env python
#
# Author       : Tracie Conn
# Created      : Dec 18, 2017
#
# Tested with Python v2.7.6
#
# Instructions: Given an array of n integers and a number d, perform
# d left rotations on the array. Then print the updated array as a
# single line of space-separated integers.
#
# Input instructions: The first line contains two space-separated
# integers denoting the respective values of n (the number of
# integers) and d, the number of left rotations you must perform.
# The second line contains n space-separated integers describing the
# respective elements of the array's initial state.
#
# Output instructions: Print a single line of space-separated 
# integers denoting the final state of the array after performing 
# left rotations.
#
# Note to self: instructions mention an array, but Python uses lists.
#


def left_rotate_list(list_to_rotate, num_rotations):
  # Simplify things if num_rotations is large
  num_rotations = num_rotations % len(a)

  # Create new list
  rotated_list = [0]*len(a)
  for new_list_index in range(len(a)):
    rotated_list[new_list_index] = list_to_rotate[(new_list_index+num_rotations)%len(a)]
  return rotated_list


# First, read in values per input instructions. We can accomplish
# this using map. n is the number of integers in the array. k is the
# number of rotations to perform.
n, k = map(int, raw_input().strip().split(' '))

# Note: although instructions require input of n, we don't require
# it; we could have used len(a)

# Similarly, read in the values to form a list
a = map(int, raw_input().strip().split(' '))

# Call function
answer = left_rotate_list(a, k)
print ' '.join(map(str,answer))

# Passed all test cases on hackerrank

