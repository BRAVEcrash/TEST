a = int(input('Enter score: '))
if a <= 59:
    print('F')
elif a >= 60 and a <= 69:
    print('C')
elif a >= 70 and a <= 79:
    print('B')
elif a >= 80 and a <= 89:
    print('A')
elif a >= 90 and a <= 100:
    print('A+')
else:
    print('Invalid score')
