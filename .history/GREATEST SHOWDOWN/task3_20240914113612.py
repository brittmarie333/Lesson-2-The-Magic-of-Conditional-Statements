#If we provide the numbers 3, 3, and 4, it should print out that "The smallest number is 3. The largest number is 4. "

x, y, z = 3,3,4

if x > y and y > z:
    print("z is the smallest!")
elif y > z and z > x:
    print("x is the smallest!")
elif z > x and x > y:
    print("y is the smallest!")
else:
    print("all variables are zero!")