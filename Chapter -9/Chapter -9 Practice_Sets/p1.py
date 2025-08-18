"""1. Write a program to read the text from a given file 'poems.txt' and find out whether it
contains the word 'twin kle'."""
with open("poem.txt") as f:
    content = f.read()
    if "Titanic" in content:
        print("Titanic is in the poem file")
    else:
        print("Titanic is NOT in the poem file")
