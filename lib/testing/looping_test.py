#!/usr/bin/env python3

from looping import happy_new_year, square_integers, fizzbuzz

import io
import sys

class TestHappyNewYear:
    '''happy_new_year() in looping.py'''

    def test_prints_10_to_1_hny(self):
        '''prints 10 to 1 countdown then "Happy New Year!"'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        happy_new_year()
        sys.stdout = sys.__stdout__
        answer = captured_out.getvalue()
        
        #answer.split(\n) produces a list that ends in ''
        answer_list = answer.split('\n')
        #second to last value should be the HNY string
        assert answer_list[-2] == "Happy New Year!", "Your final line does not match 'Happy New Year!', check spelling/capitalization!"
        digit_strings = [str(i) for i in range(1,11)]
        remaining_digits = [i for i in digit_strings if i not in answer_list] 
        assert remaining_digits == [], f"You didn't print all digits 1-10, missing {', '.join(remaining_digits)}"

class TestSquareIntegers:
    '''square_integers() in looping.py'''

    def test_square_integers(self):
        '''returns squared ints for [1, 2, 3, 4, 5] and [-1, -2, -3, -4, -5]'''
        assert(square_integers([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25])
        assert(square_integers([-1, -2, -3, -4, -5]) == [1, 4, 9, 16, 25])

class TestFizzBuzz:
    '''fizzbuzz() in looping.py'''

    def test_prints_1_to_100_fizzbuzz(self):
        '''prints 1 to 100 with fizz 3s, buzz 5s, fizzbuzz 3and5s'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        fizzbuzz()
        sys.stdout = sys.__stdout__
        answer = captured_out.getvalue()
        assert len(answer) != 0, "Nothing printed! Check your loop condition. Also do you have print statements?"
        assert "Fizz" in answer, "The string 'Fizz' not found in your answer, check spelling/capitalization!"
        assert "Buzz" in answer, "The string 'Buzz' not found in your answer, check spelling/capitalization!"
        i = 1
        for line in answer.split('\n'):
            if(line): #answer.split(\n) produces a list that ends in ''
                if i % 15 == 0: assert line == "FizzBuzz", f"Should have printed 'Buzz' when number is {i}, got {line} instead"
                elif i % 3 == 0: assert line == "Fizz", f"Should have printed 'Fizz' when number is {i}, got {line} instead"
                elif i % 5 == 0: assert line == "Buzz", f"Should have printed 'Buzz' when number is {i}, got {line} instead"
                else: assert str(i) == line, f"Should have printed {i}, got {line} instead"
                i += 1
        
        i = i - 1
        assert i == 100, f"Only looped {i} times, should have looped 100 times. Check your loop condition!" 