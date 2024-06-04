w = 0
while w == 0:
    try:
        a = int(input('N1:'))
        b = int(input('N2: '))
        print(a + b)
    except ValueError:
        print('write number')
    finally:
        print('Done')