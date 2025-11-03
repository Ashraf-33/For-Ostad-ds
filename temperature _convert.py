# celsius as c variable which will take an input from user
c = float(input('Enter the temperature in degree celsius: '))
# make two variable Fahrenheit as f and Kelvin as k
# the relation between f and c is " F = 9/5 (C) + 32"
f = ((9/5)*c)+32
# the relation between c and k is "K = C + 273"
k = c+273
print('The temperature in Fahrenheit: ', round(f,2),'F')
print('The temperatue in Kelvin: ', round(k,2),'K')