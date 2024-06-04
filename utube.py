data = input('Your text:')
file = open('indata/text.txt', 'w')
file.write(data + '\n')
file.close()
