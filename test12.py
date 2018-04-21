# coding=utf-8
'''
File: test12.py
Project: test
File Created: Saturday, 21st April 2018 7:39:23 pm
Author: <<dpj>> (<<idle0423@126.com>>)
'''

# friends = []
# friends.append("David")
# print friends

# friends.append("Mary")
# print friends

# letters = ["a", "b", "c", "d", "e"]
# print letters[0]
# letterschild = letters[1:4]
# print letterschild

# print letters[:2]
# print letters[2:]
# print letters[:]

# letters[2] = "z"
# print letters

# letters[2] = "c"
# print letters

# letters.append("n")
# print letters

# letters.append("g")
# print letters

# letters.extend(["p", "q", "r"])
# print letters

# letters.insert(2, "z")
# print letters

# letters = ["a", "b", "c", "d", "e"]
# print letters.remove("c")
# print letters

# letters = ["a", "b", "c", "d", "e"]
# del letters[3]
# print letters

# letters = ["a", "b", "c", "d", "e"]
# print letters.pop()
# print letters

# letters = ["a", "b", "c", "d", "e"]
# print letters.pop(1)
# print letters

# letters = ["a", "b", "c", "d", "e"]
# print "a" in letters
# print "z" in letters
# if "z" in letters:
#     letters.remove("z")
# print letters

# letters = ["a", "b", "c", "d", "e"]
# if "f" in letters:
#     print letters.index("f")

# letters = ["a", "b", "c", "d", "e"]
# print "item\tindex"
# for letter in letters:
#     print letter + "\t" + str(letters.index(letter))

# letters = ["d", "a", "e", "c", "b"]
# print letters
# print letters.sort()
# print letters

# letters = ["d", "a", "e", "c", "b"]
# letters.sort()
# print letters
# print letters.reverse()
# print letters

# letters = ["d", "a", "e", "c", "b"]
# letters.sort(reverse=True)
# print letters

# original = [5, 2, 3, 1, 4]
# newer = sorted(original)
# print newer
# print original

# my_tuple = ("red", "green", "blue")
# print my_tuple

# jobMarks = [55, 63, 77, 81]
# tomMarks = [65, 61, 67, 72]
# bethMarks = [97, 95, 92, 88]

# classMarks = [jobMarks, tomMarks, bethMarks]
# print classMarks

# for studentMarks in classMarks:
#     print studentMarks

# print classMarks[0]
# print classMarks[0][0]

# print "Math\tScience\tReading\tShaun"
# for student in classMarks:
#     for score in student:
#         print str(score) + "\t",
#     print

# phoneNumbers = {}
# phoneNumbers["Jonh"] = "555-1234"
# print phoneNumbers

phoneNumbers = {"John": "555-1234"}
print phoneNumbers

phoneNumbers["Mary"] = "555-6789"
phoneNumbers["Bob"] = "444-4321"
phoneNumbers["Jenny"] = "867-5309"
print phoneNumbers

# print phoneNumbers["Mary"]
# print phoneNumbers.keys()
# print phoneNumbers.values()

# for key in sorted(phoneNumbers.keys()):
#     print key, phoneNumbers[key]

# print "aaa"

# 首先取得排序之后的值的列表，然后针对列表中的每个值，循环遍历字典中的所有键，直到找到与该值关联的键，打印出该键以及对应的值
for value in sorted(phoneNumbers.values()):
    for key in phoneNumbers.keys():
        if phoneNumbers[key] == value:
            print key, phoneNumbers[key]
            print key, value

# del phoneNumbers["John"]
# print phoneNumbers

# phoneNumbers.clear()
# print phoneNumbers

print "Bob1" in phoneNumbers
