#!/usr/bin/env python3

def happy_new_year():
    i=10
    while i>0:
        print(i)
        i-=1
    return print("Happy New Year!")

def square_integers(int_list):
    return [value**2 for value in int_list]

def fizzbuzz():
   for i in range(1,101):
    if (i/3).is_integer() and (i/5).is_integer():
        print("FizzBuzz")
    elif (i/3).is_integer():
        print("Fizz")
    elif (i/5).is_integer():
        print("Buzz")
    else :
        print(i)
