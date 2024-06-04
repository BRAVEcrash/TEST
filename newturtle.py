import turtle
import random  #초기화
turtle.speed(0)
turtle.bgcolor('black')  #색상리스트
colors=['red','orange','yellow','green','blue','purple','white']  #화려한모양그리기함수
defdraw_shape(size):
	for_inrange(6):
		turtle.color(random.choice(colors))
		turtle.forward(size)
turtle.left(60)  #화려한그림그리기함수
defdraw_art():
	for_inrange(36):
	draw_shape(100)
	turtle.right(10)
draw_art()
turtle.mainloop()