import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.pensize(3)

x = 0
y = -100
t.penup()
t.goto(x,y)
t.pendown()

t.circle(100) #반지름이 100인원을 원을 그린다.
#거북이가 바라보는 방향의 원을 원점으로 한다.

t.penup()
t.goto(x-60.62, y+65)
t.pendown()
t.setheading(-60)
t.circle(70, 120)

t.pensize(3) #두께 지정하기
# Рисование глаз
t.penup()
t.goto(-35, 35)  # Перемещение влево и вверх
t.pendown()
t.dot(25)  # Рисование точки

t.penup()
t.goto(35, 35)  # Перемещение вправо
t.pendown()
t.dot(25)  # Рисование точки
