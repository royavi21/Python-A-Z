# 9. Write a program to find out whether a file is identical and matches the content of another file.
#Needed file1.txt and file2.txt for compare

with open("file1.txt") as f:
    content1 = f.read()
    # যদি this.txt এবং this_copy.txt কে পরস্পরের সাথে compare করি তাহলে Yes~equal রেজাল্ট পাব।
with open("file2.txt") as f:
    content2 = f.read()

if content1 == content2:
    print("Yes these files are equal")
else:
    print("No these files are not equal")
    