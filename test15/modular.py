# coding=utf-8
'''
File: modular.py
Project: test15
File Created: Monday, 23rd April 2018 3:58:50 pm
Author: <<dpj>> (<<idle0423@126.com>>)
'''
# # 第2题
# from my_module import c_to_f
# import time
# import random

# celsius = float(raw_input("Enter a temperature in Celsius: "))
# fahrenheit = c_to_f(celsius)
# print "That's ", fahrenheit, " degrees Fahrenheit"

# print "How",
# time.sleep(2)
# print "are",
# time.sleep(2)
# print "you",
# time.sleep(2)
# print "today?"

# print random.randint(0, 100)
# print random.random() * 10

# 第3题
# import random

# numlist = []
# for i in range(5):
#     numlist.append(random.randint(1, 20))

# for i in numlist:
#     print i,

# 第4题
import random
import time

for i in range(10):
    print random.random()
    time.sleep(3)
