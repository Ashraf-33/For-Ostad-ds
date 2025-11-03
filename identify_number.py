
unclear_number = int(input('Enter any kind of number you want (Only int allowed): '))

if unclear_number < 0: 
    print('Firstly this number is negative')
    if abs(unclear_number) % 2 == 0:
        print('And it is Even')
    else:
        print('And it is Odd')

elif unclear_number > 0:
    print('Firstly this number is positive')
    if unclear_number % 2 == 0:
        print('And it is Even')
    else:
        print('And it is Odd')

else:
    print('It is the number Zero')
