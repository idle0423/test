# coding=utf-8
'''
File: test6.py
Project: test
File Created: Monday, 16th April 2018 3:50:13 pm
Author: <<dpj>> (<<idle0423@126.com>>)
'''
import easygui
# import random
# user_response = easygui.msgbox("hello")
# print user_response
flavor = easygui.buttonbox("你最喜欢哪种口味的冰激凌？",
                           choices=["香草", "巧克力", "草莓"])
easygui.msgbox("你选择的口味是：" + flavor)

flavor = easygui.choicebox("你最喜欢哪种口味的冰激凌？",
                           choices=["香草", "巧克力", "草莓"])
easygui.msgbox(u"你选择的口味是：" + flavor)

flavor = easygui.enterbox("你最喜欢哪种口味的冰激凌？")
easygui.msgbox(u"你输入的口味是：" + flavor)

flavor = easygui.enterbox("你最喜欢哪种口味的冰激凌？",
                          default="香草")
easygui.msgbox(u"你输入的口味是：" + flavor)

# num = easygui.enterbox("请输入一个数字：")
# print type(num)
# print type(int(num))
# easygui.msgbox(u"你输入的数字是：" + num)

# secret = random.randint(1, 50)
# guess = 0
# tries = 0
# easygui.msgbox("""妞妞，妈妈有一个秘密数字，你来猜猜看吧。
# 这个数字在1~50之间,你有7次机会猜一猜。""")
# while guess != secret and tries < 7:
#     guess = easygui.integerbox("你猜的数字是多少？")
#     if not guess:
#         break
#     if guess < secret:
#         easygui.msgbox(str(guess) + " 太小了，再猜！")
#     elif guess > secret:
#         easygui.msgbox(str(guess) + " 太大了，再猜！")
#     tries = tries + 1
# if guess == secret:
#     easygui.msgbox("太棒了，你猜对了！你用了" + str(tries) + "次就猜对了！")
# else:
#     easygui.msgbox("没有机会再猜了，下次再玩儿吧。我的秘密数字是" + str(secret))

# msg1 = easygui.msgbox("hello,dpj!")
# print msg1

# msg2 = easygui.enterbox(msg="enter some string:",
#                         title="string input", default="string")
# easygui.msgbox("you input:" + msg2)

# msg3 = easygui.enterbox(msg="enter some integer:",
#                         title="integer input", default="6")
# easygui.msgbox("you input:" + msg3)
# print type(msg3)
# print type(int(msg3))

# msg4 = easygui.enterbox(msg="enter some float:",
#                         title="float input", default="6.9")
# easygui.msgbox("you input:" + msg4)
# print type(msg4)
# print type(float(msg4))

# msg1 = easygui.enterbox("""This program converts Fahrenheit to Celsius.
#                         Type in a tempreature in Fahrenheit:""")
# Fahrenheit = float(msg1)
# Celsius = (Fahrenheit - 32) * 5.0 / 9
# msg2 = easygui.msgbox("That is " + str(Celsius) + " degrees celius")

# name = easygui.enterbox("please enter your name:")
# room = easygui.enterbox("enter your room number:")
# street = easygui.enterbox("enter your street:")
# city = easygui.enterbox("enter your city:")
# state = easygui.enterbox("enter your state:")
# area = easygui.enterbox("enter your area:")
# code = easygui.enterbox("enter your code:")
# whole_addr = name + "\n" + street + "\n" + city + " ," + state + "\n" + code
# msg = easygui.msgbox(whole_addr)
