#Left Ventricle...or DIE!
#By MAS Software Inc.
#Python 2.7
import os
import random
import tkMessageBox
import time
import math

#Import the turtle module
import turtle
#Change the window size
turtle.setup(800, 600)
#Required on Mac to create turtle window
turtle.fd(0)
#Max animation speed
turtle.speed(0)
#Change the background color of the screen
turtle.bgcolor("black")
#Load the background image
turtle.bgpic("splash-screen.gif")
#Set the window title
turtle.title("Left Ventricle...or DIE!")
#Hide the turtle   
turtle.ht()
#Set the undo buffer to 1 (to save memory and speed things up)
turtle.setundobuffer(1)
#Speed up drawing (Draw every 6 frames)
turtle.tracer(0)

#Register shapes
turtle.register_shape("brain.gif")
turtle.register_shape("playbutton.gif")
turtle.register_shape("pausebutton.gif")
turtle.register_shape("soundbutton.gif")

class Sprite(turtle.Turtle):
	def __init__(self, spriteshape, color, startx, starty):
		turtle.Turtle.__init__(self, shape = spriteshape)
		self.speed(0)
		self.penup()
		self.color(color)
		self.fd(0)
		self.goto(startx, starty)
		self.speed = 0
		
	def is_collision(self, other):
		if (self.xcor() >= (other.xcor() - 20)) and \
			(self.xcor() <= (other.xcor() + 20)) and \
			(self.ycor() >= (other.ycor() - 20)) and \
			(self.ycor() <= (other.ycor() + 20)):
			return True
		else:
			return False
			
	def move(self):
		pass

class Player(Sprite):
	def __init__(self, spriteshape, color, startx, starty):
		Sprite.__init__(self, spriteshape, color, startx, starty)
		pass

		
	def move(self):		
		pass
					
class Game():
	def __init__(self):
		self.level = 1
		self.score = 0
		self.state = "splash"
		self.pen = turtle.Turtle()
		self.lives = 3
		
	def show_splash(self):
		turtle.bgpic("splash-screen.gif")
		turtle.update()
		time.sleep(1)
		turtle.bgpic("background1.gif")
		self.state = "setup"	
		
	def do_play(self, x,y):
		print ("PLAY BUTTON CLICKED!")

	def do_pause(self, x,y):
		print ("PAUSE BUTTON CLICKED!")

#Create game object
game = Game()
game.show_splash()

#Create the game objects
player = Player("triangle", "blue", 0, 0)
brain = Sprite("brain.gif", "white", 200, 150)
playbutton = Sprite("playbutton.gif", "pink", -350, 200)
pausebutton = Sprite("pausebutton.gif", "yellow", -350, 130)
soundbutton = Sprite("soundbutton.gif", "red" , -350, 60)
#Create

#Draw the game border


#Show the level and score


#Set up the game


	
#Keyboard Bindings
turtle.onkey(player.move, "Left")
turtle.onkey(player.move, "Right")
turtle.onkey(player.move, "Up")
turtle.onkey(player.move, "Down")
turtle.onkey(player.move, "space")
playbutton.onclick(game.do_play)
pausebutton.onclick(game.do_pause)
turtle.listen()

while True:
	turtle.update()

delay = raw_input("Press enter to finish. > ")
	