# coding=utf-8
'''
File: test5.py
Project: test
File Created: Sunday, 15th April 2018 5:12:28 pm
Author: <<杜沛静>> (<<dupeijing@dfsoft.com.cn>>)
'''

# print "Enter your name:"
# somebody = raw_input()
# print "Hi", somebody, ",how are you today?"

# print "Enter your name:",
# somebody = raw_input()
# print "Hi", somebody, ",how are you today?"

# print "My",
# print "name",
# print "is",
# print "Dave."

# somebody = raw_input("Enter your name :")
# print somebody

# somenum = raw_input("Enter your number:")
# print float(somenum)
# print type(somenum)
# print type(float(somenum))

# somenum = float(raw_input("Enter your num:"))
# print type(somenum)

# print "This program converts Fahrenheit to Celsius"
# print "Type in a tempreature in Fahrenheit: ",
# Fahrenheit = float(raw_input())
# Celsius = (Fahrenheit - 32) * 5.0 / 9
# print "That is",
# print Celsius,
# print "degrees celius"
# print "That is", Celsius, "degrees celius"

# number = input("Enter your number")
# print number
# print type(number)

# import urllib2
# file = urllib2.urlopen("http://manning.com/sande2/data/message.txt")
# message = file.read()
# print message

# xing = "du"
# ming = "jing"
# print xing, ming

# xing = raw_input("what is your xing:")
# ming = raw_input("what is your ming:")
# print "my name is :", xing, ming

# length = float(raw_input("Enter the length:"))
# wedith = float(raw_input("Enter th wedith:"))
# price = float(raw_input("The price is :"))
# print "the area is :", length * wedith, u"平凡米"
# print "the total price is :", length * wedith * price, u"元"

num1 = int(raw_input(u"有多少个5分币：".encode("gbk")))
num2 = int(raw_input(u"有多少个2分币：".encode("gbk")))
num3 = int(raw_input(u"有多少个1分币：".encode("gbk")))
print "the total is :", 5 * num1 + 2 * num2 + 1 * num3, u"分币"
