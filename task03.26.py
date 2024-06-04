def multipleNumber(num):
    answer = num% 2
    return answer
#------------main---------------------------
userNumber= int(input('배수를 입력하세요:'))
print('입력한 배수는:', userNumber)
for x in range(20):
    result = multipleNumber(x, userNumber)
    if result == 0:
        print(x, '는 ',)
        sum = sum+x