#!/usr/bin/env python
#
# Author       : Tracie Conn
# Created      : Jan 6, 2018
#
# Tested with Python v3.5.2
#
######## Instructions 
# Given two strings, a and b, that may or may not be of the same
# length, determine the minimum number of character deletions 
# required to make and anagrams. Any characters can be deleted from
# either of the strings.
# Input Format:
#   The first line contains a single string, a.
#   The second line contains a single string, b.
# Constraints:
#   It is guaranteed that and consist of lowercase English 
#   alphabetic letters (i.e., a through z).
# Output Format
#   Print a single integer denoting the number of characters you 
#   must delete to make the two strings anagrams of each other.
# Sample Input:
#   cde
#   abc
# Sample Output:
#   4
# Explanation:
#   We delete the following characters from our two strings to turn 
#   them into anagrams of each other:
#
#   Remove d and e from cde to get c.
#   Remove a and b from abc to get c.
#
#   We must delete characters to make both strings anagrams, so we 
#   print on a new line.
######## 

# use the string module to get the lowercase letters 'abcdefghijklmnopqrstuvwxyz'
from string import ascii_lowercase
from collections import Counter

def number_needed(a, b):
  count = 0
  for letter in ascii_lowercase:

    # note that the count function from the string module is
    # deprecated and not in python3. Instead, we'll use the Counter
    # from the collections module

    counter    = Counter(a)
    count_in_a = counter[letter]
    counter    = Counter(b)
    count_in_b = counter[letter]

    count += abs(count_in_b-count_in_a)

  return count

a = input().strip()
b = input().strip()

print(number_needed(a, b)) 