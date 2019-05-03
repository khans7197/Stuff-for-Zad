# Assignment 2
# Question 4
# Sowad Khan
# Date: April 29th, 2019
# Modifications:

# Created a card matching game

# Notes:
# Had trouble with this question, so only left what I had to start and submitted with the flowchart and IPO chart
# (talked to Ms. Harris about this)

from CardClass import *
import pygame

pygame.init()

# Setting up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 203, 234)
GREEN = (12, 173, 1)
RED = (226, 6, 6)

# Setting up fonts
font = pygame.font.SysFont("TimesNewRoman", 25)
big = pygame.font.SysFont("TimesNewRoman", 50)

# Setting up screen sizes and properties
screen_size = (1200, 800)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Card Game!")
screen.fill(GREEN)  # Fill screen with green
pygame.display.flip()
clock = pygame.time.Clock()

score = 0  # score variable starting at 0

card_lists = pygame.sprite.Group()  # Creating a sprite group for cards to be used


def card_placer(suit, number, xpos, ypos):
    """Will place cards at their appropriate positions on screen"""
    global types
    types = card(suit, number)  # Instance variable for the class
    types.move(xpos, ypos)  # Move the card to a specific position on screen
    card_lists.add(types)  # Add the cards to the sprite group created


# Calling the card placer function, creating each card for hearts and spades suits
card_placer("Hearts", 1, 425, 300)
card_placer("Hearts", 2, 250, 100)
card_placer("Hearts", 3, 950, 700)
card_placer("Hearts", 4, 775, 700)
card_placer("Hearts", 5, 250, 300)
card_placer("Hearts", 6, 950, 500)
card_placer("Hearts", 7, 775, 100)
card_placer("Hearts", 8, 250, 500)
card_placer("Hearts", 9, 75, 300)
card_placer("Hearts", 11, 600, 500)
card_placer("Hearts", 12, 775, 500)
card_placer("Hearts", 13, 1125, 300)
card_placer("Hearts", 14, 75, 700)
card_placer("Hearts", 10, 75, 100)

card_placer("Spades", 1, 775, 300)
card_placer("Spades", 2, 600, 100)
card_placer("Spades", 3, 950, 100)
card_placer("Spades", 4, 425, 500)
card_placer("Spades", 5, 75, 500)
card_placer("Spades", 6, 1125, 500)
card_placer("Spades", 7, 250, 700)
card_placer("Spades", 8, 600, 700)
card_placer("Spades", 9, 425, 100)
card_placer("Spades", 10, 950, 300)
card_placer("Spades", 11, 1125, 100)
card_placer("Spades", 12, 425, 700)
card_placer("Spades", 13, 600, 300)
card_placer("Spades", 13, 1125, 700)


# Updating sprite groups and drawing them on the screen
card_lists.update()
card_lists.draw(screen)

pygame.display.flip()  # Putting everything on the screen


running = True  # While game is running
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Quit pygame if game is not running
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:  # Check for mouse click
            pos = pygame.mouse.get_pos()  # Get the position of the mouse

            # Checking if the mouse clicked a card in the cards sprite group
            clicked_sprites = [cards for cards in card_lists if cards.rect.collidepoint(pos)]
            if clicked_sprites:
                print("Testing")

            # This is where I started having some trouble, I did not know how to highlight/make the card glow when it
            # was clicked. I tried drawing a rectangle without filling it around the card, but it wouldn't allow me
            # since the card is in a sprite group and not an individual rect object. I tried working around this, but
            # wasn't successful. Also, I did not know how to check if the card that was clicked was the same
            # number/type of the next card that would be clicked in order to match them.
            # If I were able to implement those two things, this program should've been able to function fine.

pygame.quit()

