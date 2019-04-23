# Assignment 2
# Question 1
# Sowad Khan
# Date: April 6th, 2019
# Modifications:
# April 7th: Added in user input for values
# April 10th: Instead of user inputs for length and times, changed it to only input for an angle (a shape)
# April 10th: Given user choice of shape to draw, set default as a square

# Create a recursive function using turtle

# importing turtle and random modules
import turtle
import random

colors = ["blue", "green", "red", "purple", "orange", "pink", "yellow"]  # A list of colors used

# Asks user for the shape of spiral they would like to draw
print("If anything other than the below is entered, the default option will draw a star spiral ")
angle = str(input("Please pick a spiral shape to draw (Options: triangle, square, pentagon, hexagon, octagon, star): "))

# Setting up the turtle screen
screen = turtle.Screen()
screen.bgcolor("grey")
screen.title("A Recursive Spiral!")

# Setting up turtle properties
t = turtle.Turtle()
t.ht()
t.speed(0)

if angle == "triangle":  # Checks if the user entered triangle
    angle = 120  # Convert their input to 120

elif angle == "square":  # Checks if the user entered square
    angle = 90  # Convert their input to 90

elif angle == "pentagon":  # Checks if the user entered pentagon
    angle = 75  # Convert their input to 75

elif angle == "hexagon":  # Checks if the user entered hexagon
    angle = 60  # Convert their input to 60

elif angle == "octagon":  # Checks if the user entered octagon
    angle = 45  # Convert their input to 45

elif angle == "star":  # Checks if the user entered star
    angle = 150  # Convert their input to 150

# If the user enters something other than the shapes mentioned above, a square will be drawn by default
else:
    angle = 150


def recursive_spiral(length, angle, times, pen_size):
    """A function that will create a recursive spiral"""
    if times > 0:  # Runs the code until recursion stops, base case
        for i in range(length):
            t.pencolor(random.choice(colors))  # Chooses a color randomly from the list
        if pen_size == 5:  # Once the pen size is 5, it resets back to 0 and starts adding 1 to it again
            pen_size = 0
        t.forward(length)  # Move forward
        t.left(angle)  # Turn left by the angle
        t.pensize(pen_size)  # Choose the pensize

        # Recursive call to add 3 to length each time, subtract 1 from times, and add 1 to the pen size
        recursive_spiral(length + 3, angle, times - 1, pen_size + 1)


recursive_spiral(10, angle, 50, 0)  # Calls the function with required values

screen.exitonclick()  # Closes turtle window on click (Only when the recursion ends)
