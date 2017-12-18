#!/usr/bin/env python
#
# Author       : Tracie Conn, tracierenea@mac.com
# Created      : Dec 17, 2017
# This script tested with Python 2.7.6

def FibonacciFizzBuzz(n):
  # Instructions:
  # In the programming language of your choice, write a program 
  # generating the first n Fibonacci numbers F(n), printing:
  #   "Buzz" when F(n) is divisible by 3.
  #   "Fizz" when F(n) is divisible by 5.
  #   "FizzBuzz" when F(n) is divisible by 15.
  #   "BuzzFizz" when F(n) is prime.
  #    the value F(n) otherwise.
  #
  # TODO: Ask customer about the cases of F(n)=3 and F(n)=5, which
  # satisfy two conditions (are divisible by 3 or 5, but also prime)

  # TODO: Ask customer if first value for the sequence is 1 or 0.
  # Assume 1 for now.
  n_first = 1

  # Print some column headings
  print '\nIndex\tOutput'

  # Initialize a list with the first 2 values in the Fib sequence
  F_n = [n_first, n_first+1]

  # Initialize a list for the output
  F_fizzbuzzed = []

  # Loop through defining the Fibonacci numbers in the sequence and
  # print according to defined rules.
  for index in range(n):
    if index == 0:
      F_n = [n_first]
    elif index == 1:
      F_n.append(n_first+1)
    else:
      F_n.append(F_n[index-1]+F_n[index-2])

    # Check if F(n) is prime. If F(n) is divisible by any int less
    # less than F(n), then it is not prime. So we'll check via a
    # loop.
    if F_n[index] == 1:
      # Prime numbers are greater than 1, so we'll define 1 
      # explicitly as not prime.
      prime_flag = False
    else:
      prime_flag = True
      # TODO: Look for a more efficient algorithm for identifying
      # prime numbers. This is very slow for assessing large numbers.
      for test_divisor in range(2,F_n[index]):
        if F_n[index] % test_divisor == 0:
          prime_flag = False


    # Next, print output per instructions
    print index, '\t',

    # If F(n) is divisible by 15, print "FizzBuzz" 
    if F_n[index] % 15 == 0:
      print 'FizzBuzz'
      F_fizzbuzzed.append('FizzBuzz')
    # If F(n) is divisible by 3, print "Buzz"
    elif F_n[index] % 3 == 0:
      print 'Buzz'
      F_fizzbuzzed.append('Buzz')
    # If F(n) is divisible by 5, print "Fizz"
    elif F_n[index] % 5 == 0:
      print 'Fizz'
      F_fizzbuzzed.append('Fizz')
    # If F(n) is prime, print "BuzzFizz"
    elif prime_flag == True:
      print 'BuzzFizz'
      F_fizzbuzzed.append('BuzzFizz')
    # Print the value otherwise
    else:
      print F_n[index]
      F_fizzbuzzed.append(str(F_n[index]))
  
  return F_fizzbuzzed
