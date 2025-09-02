#Email: abkariyyah.ahmed31@myhunter.cuny.edu
#Name: Abkariyyah Ahmed
#Date: Feb 26, 2025
#This program outputs : shades of purple



import turtle		        #Import the turtle drawing package

turtle.colormode(255)		#Allows colors to be given as 0...255
riya = turtle.Turtle()		#Create a turtle
riya.shape("turtle")		#Make it turtle shaped
riya.backward(100)              #Move her backwards, to give more space to draw

#For 0,10,20,...,250
for i in range(0,255,10):
    riya.forward(10)		#Move forward
    riya.pensize(i)		#Set the drawing size to be i (larger each time)
    riya.color(i,0,i)		#Set the red channel to be i (brighter each time)

#RGB - Purple - (255,0,255)
