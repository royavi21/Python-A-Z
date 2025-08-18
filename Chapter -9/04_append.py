str = " Hola Moo"

f = open("myfile.txt", "a")
f.write(str)
f.close() # যত বার run হবে ততবার myfile.txt  এ str এর value - add হতেই থাকবে।