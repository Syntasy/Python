#!/bin/python3

name = input("enter name ")
drink = input("favorite drink? ")
print(f"Hello {name}! Have a {drink}.")


x = float(input("give me a number: "))
o = input("give me an operator: ")
y = float(input("give me another number: "))

if o == "+":
    print (x + y)
elif o == "-":
    print (x - y)
elif o == "/":
    print (x / y)
elif o == "*":
    print (x * y)
elif o == "**" or o == "^":
    print (x ** y)
else: 
    print("unknown operator")