temprature = [32.4 , 23.2, 35.5, 43.7, 22.3]

total = 0

for temp in temprature:
    total += temp
    
avg = total/len(temprature)
print(f"Avarage temparature is: {avg:.2f}") #this use loop which takes more time than numpy



