# Assignment 2
# Question 3
# Sowad Khan
# Date: April 24th, 2019
# Modifications:
# April 24th - Set up all variables and functions to be used
# April 25th - Created main body of the game, dice rolling and collecting the numbers entered
# April 25th - Fixed a small error where the numbers were not being converted into one number properly
# April 25th - Added scenarios where either player 1 or player 2 wins
# April 28th - Added game instructions, added scenario if both players/computer ties

# Created Beat That! dice game

# Notes:
# As I showed Ms. Harris before, my folder and files in GitHub was having some weird problems, where my dice class was
# not being found and I couldn't import it. This is why I had to make this program in a different folder and move this
# file into my Github folder to commit it. This is why my questions and files don't have regular commits, but my errors
# are listed in the modifications above for all questions, so tracetables refer to those dates of modifications and the
# code during those dates are shown in the code part of my tracetables.

# Music link: https://youtu.be/3ssL8vx7Xhg

# Importing the dice class and pygame
from DieClass import DieGame
import pygame

pygame.init()  # Initialize pygame

# Screen dimensions
width = 800
height = 700

# Colors to be used
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 203, 234)
GREEN = (12, 173, 1)
RED = (226, 6, 6)
LIGHT_GREEN = (0, 255, 0)

# Setting up fonts
font = pygame.font.SysFont("TimesNewRoman", 25)
big = pygame.font.SysFont("TimesNewRoman", 50)

# Load background music and play it infinitely
pygame.mixer.music.load("Dice Game.mp3")
pygame.mixer.music.play(-1)

# Creating the pygame screen
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Beat That!")
display.fill(GREEN)
pygame.display.flip()
clock = pygame.time.Clock()

running = True  # The game is running
display_instructions = True  # Instructions will be displayed
instructions = 1  # Start at sentence 1

while running and display_instructions:  # While these conditions are true
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Quit pygame if event type is quit
            running = False

        if event.type == pygame.KEYDOWN:  # Checking for user input on the keyboard
            if event.key == pygame.K_RETURN:  # Checking if the enter/return button has been pressed
                instructions += 1  # Instructions increase by one every time enter is pressed
                if instructions == 12:  # Instructions will go away once 12 is reached
                    display_instructions = False

    # The instructions will load a new sentence every time enter is clicked, until instructions reaches 12
    # Each sentence is displayed below eachother
    if instructions == 1:
        text = font.render("Instructions for Beat That! (Click Enter to continue)", True, WHITE)
        display.blit(text, (20, 50))
    if instructions == 2:
        text = font.render("In this game, you will require two players (if only one, play for the AI )", True, WHITE)
        display.blit(text, (20, 90))
    if instructions == 3:
        text = font.render("To roll the dice, click Enter and record your number by clicking the number", True, WHITE)
        display.blit(text, (20, 130))
    if instructions == 4:
        text = font.render("You will roll and record your numbers 3 times", True, WHITE)
        display.blit(text, (20, 170))
    if instructions == 5:
        text = font.render("The purpose of this game is to achieve the highest number possible", True, WHITE)
        display.blit(text, (20, 210))
    if instructions == 6:
        text = font.render("For example, if you roll 4,5,6, your number would be 654", True, WHITE)
        display.blit(text, (20, 250))
    if instructions == 7:
        text = font.render("Once your turn is done, click Enter and give your opponent their turn", True, WHITE)
        display.blit(text, (20, 290))
    if instructions == 8:
        text = font.render("The other player will follow the same instructions and try to score higher", True, WHITE)
        display.blit(text, (20, 330))
    if instructions == 9:
        text = font.render("If only 1 player, you will have to roll/record numbers for the other turn", True, WHITE)
        display.blit(text, (20, 370))
    if instructions == 10:
        text = font.render("Once both players/turns have been finished, the winner will be presented", True, WHITE)
        display.blit(text, (20, 410))
    if instructions == 11:
        text = font.render("Have fun and be honest! Please press Enter when you are ready", True, WHITE)
        display.blit(text, (20, 450))
    if instructions == 12:
        display.fill(GREEN)
        text = big.render("Press Enter to roll your dice", True, WHITE)
        word = big.render("Don't forget to enter your number too!", True, WHITE)
        display.blit(text, (130, 300))
        display.blit(word, (25, 400))
        pygame.display.flip()

    pygame.display.flip()
    clock.tick(60)  # 60 fps

# Lists that will contain the numbers both users input from their dice roll
player1_numbers = []
player2_numbers = []

# Variables to count number of times enter is pressed
number_of_presses = 0
number_of_presses_2 = 0

dice = DieGame(display, width, height)  # Calling class DieGame


def text_display(statement, x, y, color):
    """Function that will display text"""
    text = big.render(statement, True, color)
    display.blit(text, (x, y))  # Display on screen
    pygame.display.update()  # Update screen


def dice_number(statement, press):
    """Will show the number the user enters after rolling their dice"""
    if press < 4:  # Only happens if enter is pressed less than 4 times
        text = font.render(statement, True, WHITE)
        rect = text.get_rect()
        rect.move_ip(600, 50)  # Moving the text box in the upper right corner
        display.blit(text, rect)  # Displaying the text box
        pygame.display.update()


def player_number(number_key, value, player):
    """Numbers user inputs will be appended to the list and sorted"""
    items = 3  # 3 numbers in the list
    number = pygame.key.get_pressed()
    if number[number_key]:  # Checks if the user entered a number
        if len(player) < items:  # If the length of the list is less than 3
            player.append(value)  # Number is appended to the list
            if len(player) == 3:
                player.sort(reverse=True)  # List is sorted from highest to lowest


def number_maker(player):
    """Function that will turn the numbers in each list into one number"""
    num = "".join(map(str, player))  # Makes each individual number a string, and joins them
    return int(num)  # Turns the string back into an integer


def dice_roll(press, player):
    """Function to allow dice to be rolled"""
    if press < 4:  # If user presses enter less than 4 times
        roll = pygame.key.get_pressed()
        if roll[pygame.K_RETURN]:  # Checks for enter/return input
            dice.random()  # Call random in the dice class
            effect = pygame.mixer.Sound("Dice.wav")  # Dice rolling sound effect is loaded and played
            effect.play(0)
            pygame.display.update()
    if press == 4:  # If user presses enter 4 times
        display.fill(GREEN)
        text_display("Your Biggest Number is: " + str(number_maker(player)), 100, 300, WHITE)  # Display number created


running = True  # While game is running
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # If user presses enter
                number_of_presses += 1  # Keep adding 1 to presses
                display.fill(GREEN)
                text_display("Roll The Dice!", 275, 20, WHITE)  # Call text display function
                dice_number("Dice Number: ", number_of_presses)  # Call dice number function
                dice_roll(number_of_presses, player1_numbers)  # Call dice roll functions
                pygame.display.update()  # Update the screen

            # Whatever number the user gets and inputs, the same actions will happen as indicated for number 1
            if event.key == pygame.K_1:  # If users enters 1
                # Put that number into the list created, shows it in the upper right corner
                player_number(pygame.K_1, 1, player1_numbers)
                dice_number("Dice Number: 1", number_of_presses)
            if event.key == pygame.K_2:
                player_number(pygame.K_2, 2, player1_numbers)
                dice_number("Dice Number: 2", number_of_presses)
            if event.key == pygame.K_3:
                player_number(pygame.K_3, 3, player1_numbers)
                dice_number("Dice Number: 3", number_of_presses)
            if event.key == pygame.K_4:
                player_number(pygame.K_4, 4, player1_numbers)
                dice_number("Dice Number: 4", number_of_presses)
            if event.key == pygame.K_5:
                player_number(pygame.K_5, 5, player1_numbers)
                dice_number("Dice Number: 5", number_of_presses)
            if event.key == pygame.K_6:
                player_number(pygame.K_6, 6, player1_numbers)
                dice_number("Dice Number: 6", number_of_presses)
            if event.key == pygame.K_7:
                player_number(pygame.K_7, 7, player1_numbers)
                dice_number("Dice Number: 7", number_of_presses)
            if event.key == pygame.K_8:
                player_number(pygame.K_8, 8, player1_numbers)
                dice_number("Dice Number: 8", number_of_presses)
            if event.key == pygame.K_9:
                player_number(pygame.K_9, 9, player1_numbers)
                dice_number("Dice Number: 9", number_of_presses)

            if number_of_presses == 5:  # If player 1 pressed enter 5 times
                # Call text display functions to indicate their turn is over
                text_display("Great! Now it's the other players turn", 25, 300, WHITE)
                text_display("Play for the AI if you are the only player", 5, 375, WHITE)
                text_display("Press Enter to continue", 175, 450, WHITE)

            if number_of_presses > 5:  # If player 1 pressed enter more than 5 times
                if event.key == pygame.K_RETURN:
                    number_of_presses_2 += 1  # Increment player 2 presses by 1
                    display.fill(GREEN)  # Fill the screen with green
                    text_display("Roll The Dice!", 275, 20, WHITE)  # Call text display functions
                    dice_number("Dice Number: ", number_of_presses_2)  # Call dice number function
                    dice_roll(number_of_presses_2, player2_numbers)  # Call dice roll function
                    pygame.display.update()

                # The same method is done for player 2, their numbers are put into a different list
                if event.key == pygame.K_1:
                    player_number(pygame.K_1, 1, player2_numbers)
                    dice_number("Dice Number: 1", number_of_presses_2)
                if event.key == pygame.K_2:
                    player_number(pygame.K_2, 2, player2_numbers)
                    dice_number("Dice Number: 2", number_of_presses_2)
                if event.key == pygame.K_3:
                    player_number(pygame.K_3, 3, player2_numbers)
                    dice_number("Dice Number: 3", number_of_presses_2)
                if event.key == pygame.K_4:
                    player_number(pygame.K_4, 4, player2_numbers)
                    dice_number("Dice Number: 4", number_of_presses_2)
                if event.key == pygame.K_5:
                    player_number(pygame.K_5, 5, player2_numbers)
                    dice_number("Dice Number: 5", number_of_presses_2)
                if event.key == pygame.K_6:
                    player_number(pygame.K_6, 6, player2_numbers)
                    dice_number("Dice Number: 6", number_of_presses_2)
                if event.key == pygame.K_7:
                    player_number(pygame.K_7, 7, player2_numbers)
                    dice_number("Dice Number: 7", number_of_presses_2)
                if event.key == pygame.K_8:
                    player_number(pygame.K_8, 8, player2_numbers)
                    dice_number("Dice Number: 8", number_of_presses_2)
                if event.key == pygame.K_9:
                    player_number(pygame.K_9, 9, player2_numbers)
                    dice_number("Dice Number: 9", number_of_presses_2)

                if number_of_presses_2 >= 5:  # If the second player presses enter more than 5 times
                    if number_maker(player1_numbers) > number_maker(player2_numbers):  # Check if player 1 won
                        # Display both players numebrs and indicate the winner
                        text_display("Player 1: " + str(number_maker(player1_numbers)), 75, 100, LIGHT_GREEN)
                        text_display("Player 2: " + str(number_maker(player2_numbers)), 480, 100, RED)
                        text_display("PLAYER 1 HAS WON BY " + str(number_maker(player1_numbers) - number_maker(
                            player2_numbers)), 100, 300, WHITE)
                        text_display("Player 1 has Beat That!", 175, 400, BLUE)
                        pygame.time.delay(5000)  # Delay the game for 5 seconds
                        pygame.quit()  # Quit pygame

                    elif number_maker(player2_numbers) > number_maker(player1_numbers):  # Check if player 2 won
                        # Display both players numbers on screen and indicate the winner
                        text_display("Player 1: " + str(number_maker(player1_numbers)), 75, 100, RED)
                        text_display("Player 2: " + str(number_maker(player2_numbers)), 480, 100, LIGHT_GREEN)
                        text_display("PLAYER 2 HAS WON BY " + str(number_maker(player2_numbers) - number_maker(
                            player1_numbers)), 100, 300, WHITE)
                        text_display("Player 2 has Beat That!", 175, 400, BLUE)
                        pygame.time.delay(5000)  # Delay game for 5 seconds
                        pygame.quit()  # Quit pygame

                    else:  # If both players/AI get the same number, they tie
                        text_display("Player 1: " + str(number_maker(player1_numbers)), 75, 100, RED)
                        text_display("Player 2: " + str(number_maker(player2_numbers)), 480, 100, LIGHT_GREEN)
                        text_display("WE HAVE A TIE!", 200, 300, BLUE)
                        pygame.time.delay(5000)
                        pygame.quit()

    clock.tick(60)  # 60 fps

pygame.quit()  # Quit pygame
