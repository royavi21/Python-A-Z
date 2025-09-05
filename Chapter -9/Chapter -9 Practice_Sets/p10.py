# 10. Write a program to wipe out the content of a file using python.

with open("fr_wipe_data_p10.txt", "w") as f:
    f.write(" ") # .write(" ") এ ফাকা স্ট্রিং রাখলেই সিলেক্টেড ফাইল ওয়াইপাউট হয়ে যাবে। 