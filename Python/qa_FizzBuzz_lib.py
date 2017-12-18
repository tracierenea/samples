#!/usr/bin/env python
#
# Author       : Tracie Conn, tracierenea@mac.com
# Created      : Dec 17, 2017
#
# This script tested with Python 2.7.6
# Unit test for the FibonacciFizzBuzz function

import unittest
from FizzBuzz_lib import FibonacciFizzBuzz

class test_FibFizzBuzz(unittest.TestCase):
  def test_n_5(self):
    test_list = FibonacciFizzBuzz(5)
    self.expected = ["1","BuzzFizz","Buzz","Fizz","8"]
    self.assertEqual(self.expected, test_list)

  def test_n_10(self):
    test_list = FibonacciFizzBuzz(10)
    self.expected = ["1","BuzzFizz","Buzz","Fizz","8","BuzzFizz","Buzz","34","Fizz","BuzzFizz"]
    self.assertEqual(self.expected, test_list)

  def test_n_20(self):
    test_list = FibonacciFizzBuzz(20)
    self.expected = ["1","BuzzFizz","Buzz","Fizz","8","BuzzFizz","Buzz","34","Fizz","BuzzFizz","Buzz","BuzzFizz","377","Fizz","Buzz","BuzzFizz","2584","4181","FizzBuzz","10946"]
    self.assertEqual(self.expected, test_list)

if __name__ == '__main__':
    unittest.main()