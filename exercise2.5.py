#Exercise 2.5
import math

s = input("Input a list of float numbers: ")
numbers = list(map(float, s.split()))

for x in numbers:
    y = math.sin(x)
    print("The sine of " + str(x) + " is " + str(y))