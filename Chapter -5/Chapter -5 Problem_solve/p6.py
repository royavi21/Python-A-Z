# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique. 
fev_lang = {}

name = input("Enter friend name: ")
lang = input("Enter your fev language: ")
fev_lang.update({name: lang})

name = input("Enter friend name: ")
lang = input("Enter your fev language: ")
fev_lang.update({name: lang})

name = input("Enter friend name: ")
lang = input("Enter your fev language: ")
fev_lang.update({name: lang})

name = input("Enter friend name: ")
lang = input("Enter your fev language: ")
fev_lang.update({name: lang})

print(fev_lang)

'''
op:
Enter friend name: Avijit Roy
Enter your fev language: Python
Enter friend name: Rohan
Enter your fev language: Java
Enter friend name: Sikha
Enter your fev language: C++
Enter friend name: Purabi
Enter your fev language: Drt
{'Avijit Roy': 'Python', 'Rohan': 'Java', 'Sikha': 'C++', 'Purabi': 'Drt'}
'''