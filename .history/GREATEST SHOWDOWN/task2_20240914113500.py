#Task 2: Identify the Smallest Improve upon your code from Task 1 to also determine the smallest number among the three and print it out.

x, y, z = input("Please provide three numbers: ").split()

if x > y and y > z:
    print("z is the smallest!")
elif y > z and z > x:
    print("x is the smallest!")
elif z > x and x > y:
    print("y is the greatest!")
else:
    print("all variables are zero!")