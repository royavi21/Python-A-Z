"""4. A file contains a word “Donkey” multiple times. You need to write a program
which replace this word with ##### by updating the same file. """

from idlelib.run import MyHandler
from tkinter.font import names

word = "Donkey"

with open("donkey.txt", "r") as f:
    content = f.read()

contentNew = content.replace("Donkey", "######")
contentNew = content.replace("BIG", "######")

with open("donkey.txt", "w") as f:
    f.write(contentNew)