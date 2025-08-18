from os import linesep

f = open("file.txt")

# linesep = f.readlines()  #readlines is a list type. |<class 'list'>|
# print(linesep, type(linesep))     #সম্পূর্ণটা লিস্ট আকারে চাইলে readlines ব্যবহার করতে হয়।

# line1 = f.readline()  #readline is a str type. |<class 'str'>|
# print(line1, type(line1))
#
# line2 = f.readline()
# print(line2, type(line2))
#
# line4 = f.readline()
# print(line4, type(line4))

linesep1 = f.readline()
while (linesep1 != ""):          #while loop দিয়ে একবারে সব লাইন একেকটা করে দেখানো যায়।
    print(linesep1)
    linesep1 = f.readline()

f.close()