# coding=utf-8
'''
File: test13.py
Project: test
File Created: Sunday, 22nd April 2018 9:54:12 am
Author: <<dpj>> (<<idle0423@126.com>>)
'''


# def printMyAddress(myName, houseNum):
#     print myName
#     print houseNum
#     print "Ottawa, ontario, Canada"
#     print "K2M 2E9"
#     print


# printMyAddress("Carter Sande", "45")
# printMyAddress("Jack Black", "64")
# printMyAddress("Tom Green", "22")
# printMyAddress("Todd White", "36")

# print printMyAddress("Carter Sande", "45")
# print printMyAddress("Jack Black", "64")
# print printMyAddress("Tom Green", "22")
# print printMyAddress("Todd White", "36")

# def calculateTax(price, tax_rate):
#     total = price + (price * tax_rate)
#     global my_price
#     my_price = 10000
#     print "my_price (inside function) = ", my_price
#     return total


# my_price = float(raw_input("Enter a price: "))

# totalPrice = calculateTax(my_price, 0.06)
# print "price = ", my_price, "Total price = ", totalPrice
# print "my_price (outside function) = ", my_price

# 第2题
# def printInfo(infolist):
#     for info in infolist:
#         print info,


# infolist = ["carter", "adress", "street1", "city", "province", "450000",
#             "china"]

# printInfo(infolist)

# 第3题
# def calculateTax(price, tax_rate):
#     total = price + (price * tax_rate)
#     global my_price
#     my_price = 10000
#     print "my_price (inside function) = ", my_price
#     return total


# my_price = float(raw_input("Enter a price: "))

# totalPrice = calculateTax(my_price, 0.06)
# print "price = ", my_price, "Total price = ", totalPrice
# print "my_price (outside function) = ", my_price

# 第4题
def totalMoney(fivenum, threenum, onenum):
    total = 5 * fivenum + 3 * threenum + 1 * onenum
    return total


fivenum = int(raw_input("Enter five num: "))
threenum = int(raw_input("Enter three num: "))
onenum = int(raw_input("Enter one num: "))

print totalMoney(fivenum, threenum, onenum)
