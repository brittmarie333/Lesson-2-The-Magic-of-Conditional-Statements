#Task 1: Leap Year Checker Write a Python program that prompts the user to input a year. 
# The program should determine if the given year is a leap year or not and then display an appropriate message. 
# Please note that this is the definition of a leap year: Every year that is exactly divisible by four is a leap year, 
# except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400.

#stack overflow helped me with the code structure a bit but used nesting "if" and I'm not quite there. Struggling with input on vscode to check this 

year_type = input("Please provide a year: ")

if year_type % 4 == 0 and year_type % 100 == 0:
    print("This is a leap year!")
elif year_type % 400 == 0:
    print("This is a leap year!")
else:
    print("This is NOT a leap year!")