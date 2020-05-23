import turtle
from turtle import Turtle,Screen
import random
from tkinter import *
from tkinter import messagebox

width = 800
height = 600

turtles = 8
colors = ['red','blue','green','purple','yellow','orange','black','cyan']

class Turtle():
	def __init__(self,color,pos):
		self.color = color
		self.pos = pos
		self.turt = turtle.Turtle()
		self.turt.penup()
		self.turt.setpos(pos)
		self.turt.shape('turtle')
		self.turt.color(color)
		self.turt.shapesize(2)
		self.turt.setheading(90)
	
	def race(self):
		r = random.randint(1,20)
		self.pos = (self.pos[0],self.pos[1]+r)
		self.turt.pendown()
		self.turt.forward(r)

	def reset(self):
		self.turt.clear()
		self.turt.penup()
		self.pos = (self.pos[0],-250)
		self.turt.setpos(self.pos)

def saveresult(score):
	with open("result.txt",'w') as file:
	 	for key,value in score.items():
	 		file.write(key+" = "+str(value)+"\n")

def main(lap):
	global root1
	root1.destroy()
	turtle.setup(width, height)
	turt=[]
	x=-350
	winner = None
	score ={}
	try:	
		laps = int(lap)
	except:
		laps =1	
	count = 0
	reset_count = 0
	for i in range(turtles):
		score[colors[i]] =0
	for i in range(turtles):
		turt.append(Turtle(colors[i],(x,-250)))
		x+=100
	while count<laps:
		for t in turt:	
			if t.pos[1] >=250:
				reset_count+=1
				t.reset()
				if reset_count == 1:
					count+=1
					score[t.color]+=1
				if reset_count%8==0:
					reset_count=0	
			t.race()

	saveresult(score)
	turtle.mainloop()	

def main_menu():
	global root1
	root.destroy()
	root1 = Tk()
	root1.geometry('%dx%d+%d+%d' % (w, h, x, y))
	label = Label(root1,text = "Enter numbers of laps?").pack()
	input = Entry(root1)
	input.pack()
	Button(root1, text="Race", command=lambda:main(input.get())).pack()
	root1.mainloop()
	# pass


root = Tk()
w = 150  # width for the window size
h = 80  # height for the window size
ws = root.winfo_screenwidth()  # width of the screen
hs = root.winfo_screenheight()  # height of the screen
x = (ws/2) - (w/2)  # calculate x and y coordinates for the Tk window
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
launch = messagebox.askquestion("launcher","Play game?")
if launch == "yes":
    main_menu()
else:
	root.destroy()
root.mainloop()
