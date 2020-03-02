# Unit 1, Assignment 1
# Question 4
# Sowad Khan
# Date: March 1st, 2019
# Modifications: March 2nd - Added a colour list to randomly pick a color for the ball
#                March 5th - Added a background image and set constant screen size
# Picture citation(MLA):“Pixabay'de Ücretsiz Görüntüler - Arka Plan, Dağlar, Dağ, Peyzaj.” Sea ​​Bottom Photocomposition
# · Free Image on Pixabay, pixabay.com/tr/photos/arka-plan-dağlar-dağ-peyzaj-doğa-2455710/.

# This program will simulate a ball bouncing around a screen


# Imports the turtle and random modules
import turtle
import random


def screen_formatting():  # Function for all screen formatting
    scr = turtle.Screen()  # Sets up the screen
    scr.bgpic("Turtle Background.gif")  # Changes background to a picture (Picture citation above)
    scr.title("Bouncy Ball!")  # Gives the screen a title
    scr.setup(600, 600)  # Sets up constant screen size


screen_formatting()  # Calls the function


def spawn_ball_one():  # Function for all ball animations/movement
    ball = turtle.Turtle()
    colors = ["red", "blue", "yellow", "orange", "purple", "green", "pink", "brown", "white"]

    # Ball is given multiple properties
    ball.shape("circle")
    ball.color(random.choice(colors))  # Chooses a random color from the color list
    ball.shapesize(2)
    ball.ht()  # Hides the turtle
    ball.penup()  # Turtle doesnt draw when being moved up

    # Gives the ball random coordinates to spawn at within the screen size
    x = random.randrange(-300, 300)
    y = random.randrange(-285, 285)
    ball.goto(x, y)  # Ball goes to the random coordinates specified above
    ball.st()  # Ball appears on the screen

    # Sets variables to change balls direction
    y_direction_change = -10
    x_direction_change = 4

    # This loop allows the ball to keep bouncing around the screen forever
    while True:
        # Adds the change variables above to the balls current location on the screen
        ball.sety(ball.ycor() + y_direction_change)
        ball.setx(ball.xcor() + x_direction_change)

        # This allows the ball to bounce once at the bottom and top
        if ball.ycor() < -285:  # When ball hits the edge of the screen - y direction
            y_direction_change *= -1  # Reverses direction once hitting a wall
        elif ball.ycor() > 285:
            y_direction_change *= -1

        # Checks if the ball hit both screen walls, allows to bounce off
        if ball.xcor() > 285:  # When ball hits the edge of the screen - x direction
            x_direction_change *= -1  # Reverses direction once hitting a wall
        elif ball.xcor() < -285:
            x_direction_change *= -1


spawn_ball_one()  # Calls the function
scr.exitonclick()  # Closes screen when user clicks
