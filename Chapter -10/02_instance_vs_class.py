class Employee:
    language = "Python" #This is a class attribute
    salary=20000


avi= Employee()
avi.name = "Avijit Roy" #This is an instance/object attribute
avi.language = "JavaScript" #প্রথমে ইন্সটান্স / অবজেক্ট এ চেক করবে, না থাকলে ক্লাস চেক করবে।
print(avi.name, avi.language, avi.salary)

# op: Avijit Ryo JavaScript 20000