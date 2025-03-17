# If languages of two friends are same; what will happen to the program in problem 6

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

#Value can be same. 

'''
Enter friend name: Avijit
Enter your fev language: Python
Enter friend name: Alex
Enter your fev language: Dart
Enter friend name: Martin
Enter your fev language: Python
Enter friend name: Sikha
Enter your fev language: C++
{'Avijit': 'Python', 'Alex': 'Dart', 'Martin': 'Python', 'Sikha': 'C++'}

'''