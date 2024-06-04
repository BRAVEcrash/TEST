try:
    with open('text.txt', 'r') as f:
        print(f.read())
except FileNotFoundError:
    print('No such file or directory')