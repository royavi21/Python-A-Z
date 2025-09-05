#5. Repeat program 4 for a list of such words to be censored.
from pywin.scintilla.keycodes import make_key_name

#make a list of words
words = ["Donkey","BIG", "Roy", "small"]

with open("donkey.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))


with open("donkey.txt", "w") as f:
    f.write(content)