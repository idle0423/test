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

# age = float(raw_input("Enter your age: "))
# grade = float(raw_input("Enter your grade: "))
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

# if not (age < 8):
#     print "You are allowed to play the game."
# else:
#     print "Sorry, you can't play the game."

# pay = float(raw_input("Enter your pay money: "))
# if pay <= 10:
#     pay = pay * (1 - 0.1)
#     print "sale off 10%,the pay is:"+str(pay)
# else:
#     pay = pay * (1 - 0.2)
#     print "sale off 20%,the pay is:"+str(pay)

# gender = raw_input("Enter your gender: ")
# if gender == 'f':
#     age = int(raw_input("Enter your age: "))
#     if 10 <= age <= 12:
#         print "You can join in!"
#     else:
#         print "You can't join in!"
# else:
#     print "You can't join in!"

password = "123a456"
guess = raw_input("Please Enter the password :")
if guess == password:
    print "You're in!"
    size = int(raw_input("size of tank: "))
    percent = int(raw_input("percent of full: "))
    km_per = int(raw_input("km per liter: "))
    # 距离下一个加油站距离
    s = 200
    s1 = (size * percent / 100) * km_per
    if s1 >= s:
        print "You can go another " + str(s1) + " km away"
        print "The next gas station is " + str(s) + " km away"
        print "You can wait for the next station."
    else:
        print "You can't go away!"
else:
    print "Your password is not right! You can't play the game!"
