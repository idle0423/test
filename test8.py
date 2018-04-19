# coding=utf-8
'''
File: test8.py
Project: test
File Created: Wednesday, 18th April 2018 10:18:49 pm
Author: <<dpj>> (<<idle0423@126.com>>)
'''
# for looper in ["a", "b", "c", "d", "e"]:
#     print "hello"
#     print "looper=" + looper

# for looper in [1, 2, 3, 4, 5]:
#     print looper, "times 8 = ", looper * 8

# for looper in range(1, 11):
#     print looper, "times 8 =", looper * 8

# for letter in "dupeijing":
#     print letter

# for looper in range(10):
#     print looper

# for i in range(1, 10, 2):
#     print i

# for i in range(10, 1, -1):
#     print i

# import time
# for i in range(10, 0, -1):
#     print i
#     time.sleep(1)
# print "BLAST OFF!"

# name = ["Spongebob", "Spiderman", "Justin Timberlake", "My Dad"]
# for cool_guy in name:
#     print cool_guy, "is the coolest guy ever!"

# print "Type 3 to continue, anything else to quit."
# someInput = raw_input()
# while someInput == "3":
#     print "Thank you for the 3. Very kind of you."
#     print "Type 3 to continue, anythin else to quit."
#     someInput = raw_input()
# print "That's not 3, so I'm quitting now."

# for i in range(1, 6):
#     print
#     print "i =", i,
#     print "Hello, how",
#     if i == 3:
#         continue
#     print "are you today?"

# for i in range(1, 6):
#     print
#     print "i =", i,
#     print "Hello, how",
#     if i == 3:
#         break
#     print "are you today?"

# 测试题answer
# 1.5次
# 2.3次，1,3,5
# 3.1234567
# 4.01234567
# 5.2468
# 6.10,8,6,4,2
# 7.continue
# 8.条件为false

# 动手试一试answer
# print "Which multiplication table would you like?"
# someNumber = int(raw_input())
# print "Here's your table:"
# for i in range(10):
#     print str(someNumber) + " * " + str(i + 1),
#     print " = " + str(someNumber * (i + 1))

# print "Which multiplication table would you like?"
# someNumber = int(raw_input())
# i = 0
# print "Here's your table:"
# while i < 10:
#     print str(someNumber) + " * " + str(i + 1),
#     print " = " + str(someNumber * (i + 1))
#     i = i + 1

# print "Which multiplication table would you like?"
# someNumber = int(raw_input())
# print "How high do you want to go?"
# high = int(raw_input())
# i = 0
# print "Here's your table:"
# while i < high:
#     print str(someNumber) + " * " + str(i + 1),
#     print " = " + str(someNumber * (i + 1))
#     i = i + 1

print "Which multiplication table would you like?"
someNumber = int(raw_input())
print "How high do you want to go?"
high = int(raw_input())
print "Here's your table:"
for i in range(high):
    print str(someNumber) + " * " + str(i + 1),  # 行末注释
    print " = " + str(someNumber * (i + 1))
