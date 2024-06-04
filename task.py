itemPrice=int(input("물건값을입력하시오:"))
note=int(input("1000원지폐개수:"))
coin500=int(input("500원동전개수:"))
coin100=int(input("100원동전개수:"))

change=note*1000+coin500*500+coin100*100-itemPrice

#거스름돈(500원동전개수)을계산한다.
a=nCoin500=change//500
change=change%500

#거스름돈(100원동전개수)을계산한다.
b=nCoin100=change//100
change=change%100

#거스름돈(10원동전개수)을계산한다.
c=nCoin10=change//10
change=change%10

#거스름돈(1원동전개수)을계산한다.
d=nCoin1=change

print("500원=",nCoin500,"100원=",nCoin100,"10원=",nCoin10,"1원=",nCoin1,'\n''returnPrice=',a+b+c+d)
