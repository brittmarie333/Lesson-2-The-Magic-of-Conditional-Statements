#Task 2: Identify the Smallest Improve upon your code from Task 1 to also determine the smallest number among the three and print it out.

x, y, z = input("Please provide three numbers: ").split()

if x > y and y > z:
    print("z is th!")
elif y > z and z > x:
    print("y is the greatest!")
elif z > x and x > y:
    print("z is the greatest!")
else:
    print("all variables are zero!")