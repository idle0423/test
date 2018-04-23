# coding=utf-8
'''
File: test14.py
Project: test
File Created: Monday, 23rd April 2018 9:15:38 am
Author: <<dpj>> (<<idle0423@126.com>>)
'''


# class Ball:

#     def bounce(self):
#         if self.direction == "down":
#             self.direction = "up"


# myBall = Ball()
# myBall.direction = "down"
# myBall.color = "red"
# myBall.size = "small"

# print "I just created a ball."
# print "My ball is", myBall.size
# print "My ball is", myBall.color
# print "My ball's direction is", myBall.direction
# print "Now I'm going to bounce the ball"
# print
# myBall.bounce()
# print "Now the ball's direction is", myBall.direction

# class Ball:

#     def __init__(self, color, size, direction):
#         self.color = color
#         self.size = size
#         self.direction = direction

#     def bounce(self):
#         if self.direction == "down":
#             self.direction = "up"


# myBall = Ball("red", "small", "down")
# print "I just created a ball."

# print "My ball is", myBall.size
# print "My ball is", myBall.color
# print "My ball's direction is", myBall.direction
# print "Now I'm going to bounce the ball"
# print
# myBall.bounce()
# print "Now the ball's direction is", myBall.direction

# class Ball:

#     def __init__(self, color, size, direction):
#         self.color = color
#         self.size = size
#         self.direction = direction

#     def __str__(self):
#         msg = "Hi, I'm a " + self.size + " " + self.color + "ball!"
#         return msg


# myBall = Ball("red", "small", "down")
# print myBall

# class HotDog:

#     def __init__(self):
#         self.cooked_level = 0
#         self.cooked_string = "Raw"
#         self.condiments = []

#     def __str__(self):
#         msg = "hot dog"
#         if len(self.condiments) > 0:
#             msg = msg + " with "
#         for i in self.condiments:
#             msg = msg + i + ", "
#         msg = msg.strip(", ")
#         msg = self.cooked_string + " " + msg + "."
#         return msg

#     def cook(self, time):
#         self.cooked_level = self.cooked_level + time
#         if self.cooked_level > 8:
#             self.cooked_string = "Charcoal"
#         elif self.cooked_level > 5:
#             self.cooked_string = "Well-done"
#         elif self.cooked_level > 3:
#             self.cooked_string = "Medium"
#         else:
#             self.cooked_string = "Raw"

#     def addCondiment(self, condiment):
#         self.condiments.append(condiment)


# myDog = HotDog()
# print myDog
# print "Cooking hot dog for 4 minutes..."
# myDog.cook(4)
# print myDog
# print "Cooking hot dog for 3 more minutes..."
# myDog.cook(3)
# print myDog
# print "What happens if I cook it for 10 more minutes?"
# myDog.cook(10)
# print myDog
# print "Now, I'm goting to add some stuff on my hot dog"
# myDog.addCondiment("ketchup")
# myDog.addCondiment("mustard")
# print myDog

# class Triangle:

#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def getArea(self):
#         area = self.width * self.height / 2.0
#         return area


# class Square:

#     def __init__(self, size):
#         self.size = size

#     def getArea(self):
#         area = self.size * self.size
#         return area


# myTriangle = Triangle(4, 5)
# mySquare = Square(7)

# print myTriangle.getArea()
# print mySquare.getArea()

# 第1题
class BankAccount:

    def __init__(self, name, account):
        self.name = name
        self.account = account
        self.balance = 0.0

    def printbalance(self):
        print "My balancet is: " + str(self.balance)

    def inbank(self, money):
        self.balance = self.balance + money

    def outbank(self, money):
        self.balance = self.balance - money


myBank = BankAccount("carter", "car")
myBank.printbalance()
myBank.inbank(1000)
myBank.printbalance()
myBank.outbank(500)
myBank.printbalance()


# 第2题
class InterestAccount(BankAccount):

    def __init__(self, name, account, rate):
        BankAccount.__init__(self, name, account)
        self.rate = rate

    def addInterest(self):
        interset = self.balance * self.rate
        return interset


myCount = InterestAccount("carter", "car", 0.06)
myCount.printbalance()
myCount.inbank(3000)
myCount.printbalance()
myCount.inbank(myCount.addInterest())
myCount.printbalance()
