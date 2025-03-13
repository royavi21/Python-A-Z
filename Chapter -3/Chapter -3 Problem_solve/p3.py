# Write a program to detect double space in a string.

name = "Avijit  is a CSE Student"
print(name.find("  "))
#This program returns 6, because I use first double space after 6 carecters. 

name = "Avijit is a CSE Student"
print(name.find("  "))
# Output -1 means there is no double space in the string. 


name = "Avijit is a CSE Student"
print(name.find("CSE"))
#CSE 12 number index e, tai o/p 12 asbe eitar.  