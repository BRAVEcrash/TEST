def solution(itemPrice, note, coin500, coin100):  #  이 부분은 지우지 마세요.
    #itemPrice=int(input("물건값을입력하시오:"))
    #note=int(input("1000원지폐개수:"))
    #coin500=int(input("500원동전개수:"))
    #coin100=int(input("100원동전개수:"))

    change=note*1000+coin500*500+coin100*100-itemPrice

    nCoin1000=change//1000
    change=change%1000

    nCoin500=change//500
    change=change%500

    nCoin100=change//100
    change=change%100

    nCoin10=change//10
    change=change%10

    nCoin1=change

    return nCoin1000 + nCoin500 + nCoin100 + nCoin10 + nCoin1


