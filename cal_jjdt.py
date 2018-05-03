# coding=utf-8
'''
File: cal_jjdt.py
Project: test
File Created: Thursday, 3rd May 2018 1:40:52 pm
Author: <<dpj>> (<<idle0423@126.com>>)
'''
print u"M:预期收益"
print u"每月定投金额"
print u"年收益率"
print u"定投期数（公式中为n次方）"

a = float(input(u"计划月定投金额：".encode("gbk")))
n = float(input(u"计划投资年限：".encode("gbk")))
x = float(input(u"预期年收益率：".encode("gbk")))

m = x / 100
M = 12 * a * (1 + m) * (-1 + (1 + m) ** n) / m
H = M - 12 * a * n
Y = H / (12 * a * n)

print u"投资年限到期本金收益和：" + str(M)
print u"投资年限到期总收益：" + str(H)
print u"资产增加率：" + format(Y, ".5%")

# 买入费率
buy_rate = 0.0015

# 第一次投入本金
principal1 = float(input(u"第一次投入本金：".encode("gbk")))
# 第一次买入时的净值
buy_net_value1 = float(input(u"第一次买入净值：".encode("gbk")))
# 第一次买入份额
quotient1 = principal1 * (1 - buy_rate) / buy_net_value1

# 第二次投入本金
principal2 = float(input(u"第二次投入本金：".encode("gbk")))
# 第二次买入时的净值
buy_net_value2 = float(input(u"第二次买入净值：".encode("gbk")))
# 第二次买入份额
quotient2 = principal2 * (1 - buy_rate) / buy_net_value2

# 总投入本金
total_principal = principal1 + principal2
# 总买入份额
total_quotient = quotient1 + quotient2
# 当前市值
market_value = buy_net_value2 * total_quotient
# 持仓成本价
cost_price = total_principal / total_quotient
# 当前收益率
rate = (market_value - total_principal) / total_principal * 100

print u"总本金" + str(total_principal)
print u"买入总份额：" + str(total_quotient)
print u"平均收益率：" + str(rate) + " %"
print u"平均持仓成本价：" + str(cost_price)
