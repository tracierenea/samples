#!/usr/bin/env python
#
# Author       : Tracie Conn, tracierenea@mac.com
# Created      : Dec 17, 2017
#

from FizzBuzz_lib import FibonacciFizzBuzz

# Prompt the user for how many numbers to evaluate 
print 'This program will print the first n Fibonacci numbers '
print 'according to FizzBuzz rules. Note that entering a large '
print 'value for n (n>30) may take a while to process.'
n = input('\nPlease enter an integer, n : ')

# Pass n to the FibonacciFizzBuzz function, which will print the
# output
FibonacciFizzBuzz(n)