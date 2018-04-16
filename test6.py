# coding=utf-8
'''
File: test6.py
Project: test
File Created: Monday, 16th April 2018 3:50:13 pm
Author: <<dpj>> (<<idle0423@126.com>>)
'''
import easygui
import random
# user_response = easygui.msgbox("hello")
# print user_response
# flavor = easygui.buttonbox("你最喜欢哪种口味的冰激凌？",
#                            choices=["香草", "巧克力", "草莓"])
# easygui.msgbox("你选择的口味是：" + flavor)

# flavor = easygui.choicebox("你最喜欢哪种口味的冰激凌？",
#                            choices=["香草", "巧克力", "草莓"])
# easygui.msgbox(u"你选择的口味是：" + flavor)

# flavor = easygui.enterbox("你最喜欢哪种口味的冰激凌？")
# easygui.msgbox(u"你输入的口味是：" + flavor)

# flavor = easygui.enterbox("你最喜欢哪种口味的冰激凌？",
#                           default="香草")
# easygui.msgbox(u"你输入的口味是：" + flavor)

# num = easygui.enterbox("请输入一个数字：")
# print type(num)
# print type(int(num))
# easygui.msgbox(u"你输入的数字是：" + num)

secret = random.randint(1, 9)
guess = 0
tries = 0
easygui.msgbox("""妞妞，妈妈有一个秘密数字，你来猜猜看吧。
这个数字在1~9之间,你有6次机会猜一猜。""")
while guess != secret and tries < 6:
    guess = easygui.integerbox("你猜的数字是多少？")
    if not guess:
        break
    if guess < secret:
        easygui.msgbox(str(guess) + " 太小了，再猜！")
    elif guess > secret:
        easygui.msgbox(str(guess) + " 太大了，再猜！")
    tries = tries + 1
if guess == secret:
    easygui.msgbox("太棒了，你猜对了！你用了" + str(tries) + "次就猜对了！")
else:
    easygui.msgbox("没有机会再猜了，下次再玩儿吧。我的秘密数字是" + str(secret))
