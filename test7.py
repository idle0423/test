# coding=utf-8
'''
File: test7.py
Project: test
File Created: Tuesday, 17th April 2018 10:03:44 pm
Author: <<dpj>> (<<idle0423@126.com>>)
'''
# num1 = float(raw_input("Enter the first number: "))
# num2 = float(raw_input("Enter the second number: "))
# answer = float(raw_input("Enter a number from 1 to 15: "))
# if num1 < num2:
#     print num1, "is less than", num2
# if num1 > num2:
#     print num1, "is greater than", num2
# if num1 == num2:
#     print num1, "is equal to", num2
# if num1 != num2:
#     print num1, "is not equal to", num2

# if answer >= 10:
#     print "You got at least 10!"
# elif answer >= 5:
#     print "You got at least 5!"
# elif answer >= 3:
#     print "You got at least 3!"
# else:
#     print "Yot got less than 3."

age = float(raw_input("Enter your age: "))
grade = float(raw_input("Enter your grade: "))
# if age >= 8:
#     if grade >= 3:
#         print "Yo can play this game."
#     else:
#         print "Sorry, your grade is too low, you can't play the game."
# else:
#     print "Sorry, your age is to low, you can't play the game."
# if age >= 8 and grade >= 3:
#     print "Yo can play this game."
# else:
#     print "Sorry, you can't play the game."

if not (age < 8):
    print "You are allowed to play the game."
else:
    print "Sorry, you can't play the game."
