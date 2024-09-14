#Task 1: Identify the Greatest Write a Python program that asks the user to enter three numbers. 
# Your code should then identify and print out the largest number among the three.

x, y, z = input("Please provide three numbers: ").split()

if x > y and y > z:
    print("x is the greatest!")
if y > z and z > x:
    print("y is the greatest!")