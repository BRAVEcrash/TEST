'''from random import randint, choice

print(randint(1,10))
print(randint(1,10))
x=0
while x==0:
	try:
		a,b,c,d = map(int,input().split())
		print(a*b*c*d)
	except ValueError:
		print('Error! write numbers only')
class Soda:
    def __init__(self, ingredient = None):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient =None
    def show_my_drink(self):
        if self.ingredient:
            print(f' Газировка и {self.ingredient}')
        else:
            print('Обчная газировка')

drink1= Soda()
drink2= Soda('Мaлина')
drink3= Soda(5)
drink1.show_my_drink()
drink2.show_my_drink()
drink3.show_my_drink()'''
class TriangleChecker:
    def __init__(self, sides):
        self.sides =sides
    def is_triangle(self):
        if self.ingredient:
            print(f' Газировка и {self.ingredient}')
        else:
            print('Обчная газировка')

drink1= Soda()
drink2= Soda('Мaлина')
drink3= Soda(5)
drink1.show_my_drink()
drink2.show_my_drink()
drink3.show_my_drink()