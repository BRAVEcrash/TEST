import turtle

# Создание экрана
screen = turtle.Screen()

# Создание черепахи
smiley = turtle.Turtle()

# Рисование лица
smiley.penup()
smiley.goto(0, -100)  # Перемещение вниз
smiley.pendown()
smiley.circle(100)  # Рисование круга

# Рисование глаз
smiley.penup()
smiley.goto(-35, 35)  # Перемещение влево и вверх
smiley.pendown()
smiley.dot(25)  # Рисование точки

smiley.penup()
smiley.goto(35, 35)  # Перемещение вправо
smiley.pendown()
smiley.dot(25)  # Рисование точки

# Рисование улыбки
smiley.penup()
smiley.goto(-60.62, -35)  # Перемещение вниз и влево
smiley.pendown()
smiley.setheading(-60)  # Поворот влево
smiley.circle(70, 120)  # Рисование дуги

# Завершение рисования
turtle.done()
