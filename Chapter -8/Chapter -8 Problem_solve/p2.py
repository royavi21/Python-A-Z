# Write a python program using function to convert Celsius to Fahrenheit.
'''
f = float(input("Enter the temperature in Farenheit: "))
c = 5 * (f-32) /9
# print(c)
print(f"The temperature in Celsius is: {c:.2f}") #for 2 digit after . in the o/p

'''

'''def celsius_to_fahrenheit():
    f = float(input("Enter the temperature in Fahrenheit: "))
    c = 5 * (f - 32) / 9
    print(f"The temperature in Celsius is: {c:.2f}")

# Call the function
celsius_to_fahrenheit()'''



def f_to_c():
    return 5*(f-32)/9
f=float(input("Enter the temperature in Fahrenheit: "))
print(f"The temperature in Celsius is: {f_to_c():.2f}")
