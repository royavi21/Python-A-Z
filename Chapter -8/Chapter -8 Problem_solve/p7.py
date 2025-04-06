# Write a python function to remove a given word from a list and strip it at the same time.

def rem(l, word):
    n = []
    for item in l:
        n.append(item.strip(word))

    # l.remove("an")
    return n

l = ["Avijit", "Rohan", "Sikha", "Sohan", "an"]
print(rem(l, "an"))