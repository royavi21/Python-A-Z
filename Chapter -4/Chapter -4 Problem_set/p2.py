# 2. Write a program to accept marks om 6 students and display them in a sorted manner.

markes = []

m1 = int(input("Enter mark here: "))
markes.append(m1)
m2 = int(input("Enter mark here: "))
markes.append(m2)
m3 = int(input("Enter mark here: "))
markes.append(m3)
m4 = int(input("Enter mark here: "))
markes.append(m4)
m5 = int(input("Enter mark here: "))
markes.append(m5)
m6 = int(input("Enter mark here: "))
markes.append(m6)
m7 = int(input("Enter mark here: "))
markes.append(m7)

markes.sort()
print(markes)