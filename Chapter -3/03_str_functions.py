name = "Avijit"

print(len(name))              #en() Function gives the length of string (in variable)
print(name.endswith("jit"))   #variable.endswith() function returns a given str ether it's ture ot faalse

print(name.startswith("Obhi"))  #even its "case sensitive"


'''

1. Basic String Methods
        len(s): Returns the length of the string.
        s.lower(): Converts all characters to lowercase.
        s.upper(): Converts all characters to uppercase.
        s.title(): Capitalizes the first letter of each word.
        s.capitalize(): Capitalizes the first letter of the string.
        s.strip(): Removes leading and trailing whitespace.
        s.lstrip(): Removes leading whitespace.
        s.rstrip(): Removes trailing whitespace.
2. Searching and Replacing
        s.find(sub): Returns the index of the first occurrence of sub, or -1 if not found.
        s.index(sub): Returns the index of the first occurrence of sub, raises an error if not found.
        s.replace(old, new): Replaces occurrences of old with new.
        s.count(sub): Returns the number of occurrences of sub in the string.
        s.startswith(prefix): Checks if the string starts with prefix.
        s.endswith(suffix): Checks if the string ends with suffix.
3. Splitting and Joining
        s.split(delim): Splits the string into a list based on delim (default is whitespace).
        s.rsplit(delim, maxsplit): Splits from the right side.
        ' '.join(list): Joins elements of list into a string, separated by ' '.
4. String Formatting
        s.format(value): Formats the string using placeholders {}.
        f"Hello, {name}!": f-string for string interpolation.
        s.zfill(width): Pads the string with zeros to match width.
5. Character Classification
        s.isalpha(): Returns True if all characters are letters.
        s.isdigit(): Returns True if all characters are digits.
        s.isalnum(): Returns True if all characters are letters or digits.
        s.isspace(): Returns True if all characters are whitespace.
        s.islower(): Returns True if all characters are lowercase.
        s.isupper(): Returns True if all characters are uppercase.
        
'''