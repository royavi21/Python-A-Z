"""4. A file contains a word Donkey multiple times. You need to write a program that
replaces this word with ##### by updating the same file."""

word = "Donkey"

with open("donkey.txt", "r") as f:
    content = f.read()

contentNew = content.replace("Donkey", "#####")

with open("donkey.txt", "w") as f:
    f.write(contentNew)