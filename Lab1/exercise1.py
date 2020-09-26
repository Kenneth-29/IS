#Centigrade = (Fahrenheit-32)/1.8
#Fahrenheit = (Centigrade-1.8) + 32

#Centigrade to Fahrenheit
centigrade = float(input("Enter temperature in Centigrade: "))
fahrenheit = (centigrade - 1.8) + 32
print('%.2f Centigrade is: %0.2f Fahrenheit' %(centigrade, fahrenheit))

#Fahrenheit to Centigared
fahrenheit = float(input("Enter temperature in Fahrenheit:"))
centigrade = (fahrenheit - 32)/1.8
print('%.2f Fahrenheit is: %0.2f Centigrade' %(fahrenheit, centigrade))