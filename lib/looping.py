#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
      print(i)
      i = i - 1
      print ("Happy New Year!")
    

int_list = [1, 2, 3, 4, 5]

def square_integers(int_list):
    return [x**2 for x in int_list]

result = square_integers(int_list)
print(result)
    

def fizzbuzz():
   for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
fizzbuzz()            
