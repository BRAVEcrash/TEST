import datetime

my_date = datetime.datetime(2024,6,1,13,6,34)

sentence = '{:%B, %d, %Y}'.format(my_date)
print(sentence)
