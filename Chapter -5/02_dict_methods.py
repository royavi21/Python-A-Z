marks = {
    "Avijit": 89,   # : এর বামের অংশকে keys বলে আর ডানের অংশকে values বলে। 
    "Rohan": 87,
    "Ritu":69
}

print(marks.items()) #Returns a list of (key,value)tuples.

print(marks.keys()) #Returns a list Containing dictionary's keys.

print(marks.values()) #Returns a list Containing dictionary's values.

marks.update({"Rohan": 77, "Sikha": 91}) 
# Updates the dictionary with supplied key-value pairs.
# আপডেট নুতুন ভ্যালুও অ্যাড করে। 
print(marks)


print(marks.get("Avijit")) # Returns the value of the specified ke s and value is returned Ex."Avijit" is returned here).
print(marks["Avijit"])
#এই ২ টাই সেম আউটপুট দিবে। তবে ২টাই জিনিস সেম না। 



print(marks.get("Avijit_2")) #print none
# print(marks["Avijit_2"]) # returns an error
#এখানে যে ২টা ভ্যালু নিলাম, তাতো নাই ই marks{} এ। তবে আউটপুটে marks.get("Avijit_2") দিবে none.
#পক্ষান্তরে marks["Avijit_2"] দিবে KeyError. 

'''
Some more python DICTIONARY methods...

.pop()
.clear()


'''