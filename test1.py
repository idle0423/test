# -*- coding: utf-8 -*-
import random

secret = random.randint(1, 60)
guess = 0
tries = 0
print u"妞妞，妈妈有一个秘密数字，你来猜猜看吧。"
print u"这个数字在1~60之间,你有7次机会猜一猜"
while guess != secret and tries < 7:
    guess = input(u"请输入你猜的数字: ".encode("gbk"))
    if guess < secret:
        print u"比它大哦，再猜"
    elif guess > secret:
        print u"比它小哦，再猜"

    tries = tries + 1

if guess == secret:
    print u"太棒了，你猜对了！"
    print u"你用了%d次就猜对了!" % tries
else:
    print u"没有机会再猜了，下次再玩儿吧"
    print u"我的秘密数字是：%d" % secret
