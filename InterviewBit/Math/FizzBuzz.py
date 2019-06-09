# -*- coding: utf8 -*-
"""
FizzBuzz
========

Fizzbuzz is one of the most basic problems in the coding interview world. Try to write a small and elegant code for this problem. 

Given a positive integer A, return an array of strings with all the integers from 1 to N. 
But for multiples of 3 the array should have “Fizz” instead of the number. 
For the multiples of 5, the array should have “Buzz” instead of the number. 
For numbers which are multiple of 3 and 5 both, the array should have “FizzBuzz” instead of the number.

Look at the example for more details.

Example

A = 5
Return: [1 2 Fizz 4 Buzz]
"""

from __future__ import print_function


FIZBUZZ = {
    (False, True): "Fizz",
    (True, False): "Buzz",
    (False, False): "FizzBuzz"
}

def fizzbuzz(n):
    return FIZBUZZ.get((bool(n%3), bool(n%5)), str(n))


print([fizzbuzz(n) for n in range(1, 31)])
