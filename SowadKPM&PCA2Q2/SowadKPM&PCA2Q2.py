# Assignment 2
# Question 2
# Sowad Khan
# Date: April 9th, 2019
# Modifications:
# April 11th - Added in checking for letters in the word, fixed spacing error between placeholders
# April 11th - Fixed IndexError, where letters being guessed were out of range : Lines 146-147 added to fix error
# April 12th - Created win and lose functions and error counting rules
# April 13th - Added in sound effects/music

# Create a hangman game
# Notes:
# Error sound affect link: https://youtu.be/V0DGjXE_BQQ
# Win music link: https://youtu.be/8-Vpw0xD9JU
# Trump head picture link: https://www.google.com/search?q=trump+head&safe=strict&rlz=1C1CHBD
# _enCA836CA836&source=lnms&tbm=isch&sa=X&ved=0ahUKEwimzp7sj-XhAhWldN8KHSPfAE8Q_AUIDigB&biw=1209&bih=665#imgrc=Uym3OaPivOb6FM:

# Importing modules that will be used
import pygame
import random

# initialising pygame and mixer
pygame.init()
pygame.mixer.init()

hardware = []  # Creating empty list for words

# Opening text file with words and putting them in the list
with open("ComputerHardware.txt", "r") as file:
    lines = file.readlines()  # Reads all lines in the text file
    for parts in lines:
        hardware.append(parts.replace('\n', ''))  # Puts each word in the file into the empty list

# Choosing a random word for the user to guess
choose_parts = random.choice(hardware)

# Creating all background images used during the game
base = "Hangman1.png"
error1 = "Hangman2.png"
error2 = "Hangman3.png"
error3 = "Hangman4.png"
error4 = "Hangman5.png"
error5 = "Hangman6.png"
error6 = "Hangman7.png"

# Setting up colors to be used
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Setting up font types to be used
normal = pygame.font.SysFont("TimesNewRoman", 85)
count = pygame.font.SysFont("TimesNewRoman", 25)
win_or_lose = pygame.font.SysFont("TimesNewRoman", 140)

# Setting up screen properties
screen_size = (768, 614)
pygame.display.set_caption("Let's play some hangman!")
screen = pygame.display.set_mode(screen_size)

# Starting an error count and empty string for the word to be put in
error_count = 0
word = ""

# Index numbers to be used later
index1 = 0
index2 = 0

clock = pygame.time.Clock()  # Creating a clock for fps


def background_image(display):
    """Function that will display each background image chosen"""
    image = pygame.image.load(display)
    screen.blit(image, (0, 0))
    pygame.display.flip()  # Puts the image on the screen


def text_display(word):
    """This will set up a box for the words to be displayed in"""
    text_surface = normal.render(word, True, BLACK, WHITE)
    errors = count.render("Errors: " + str(error_count), True, BLACK)  # Counting number of errors by the user
    rect = text_surface.get_rect()
    rect.center = (370, 2.5*screen_size[1]/3)  # Placing a box in the bottom of the screen
    screen.blit(text_surface, rect)
    screen.blit(errors, (550, 100))
    pygame.display.update()  # Updating everything to the screen


def lose_screen():
    """Screen that will display if user loses"""
    lost = win_or_lose.render("YOU LOST!", True, RED, WHITE)
    the_word = count.render("The word was: " + str(choose_parts), True, GREEN)  # Shows the word being guessed
    block = lost.get_rect()
    block.center = (380, 2.5*screen_size[1]/3)
    # Puts everything created on the screen
    screen.blit(lost, block)
    screen.blit(the_word, (475, 200))
    pygame.display.update()  # Updates the screen with the new things


def win_screen():
    """Screen that will display if the user wins"""
    win = win_or_lose.render("YOU WIN!", True, GREEN)  # Rendering font
    block = win.get_rect()  # Putting the font into a surface box
    block.center = (380, screen_size[1]/2)  # Position the box in the middle of the screen
    screen.blit(win, block)  # Displaying the text on screen
    pygame.mixer.music.load("Win_song.mp3")  # Loading music
    pygame.mixer.music.play(0)  # Playing the music only once
    pygame.display.update()  # Updating the screen


def word_placeholders():
    """Hyphens used as placeholders for the letters in the word being guessed"""
    global word
    for i in range(len(choose_parts)):  # Places hyphens for every letter in the length of the word
        word += "_"
        word += " "  # Adds spaces between the hyphens
    text_display(word)  # Calling the text_display function


# Calling the other two functions created
background_image(base)
word_placeholders()

running = True  # While the game is running, the following actions will be done
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Stops running if the program quits
            running = False

        if event.type == pygame.KEYDOWN:  # Checks for a user keyboard input
            typed_key = pygame.key.name(event.key)
            if typed_key in choose_parts:  # Checks if the inputted key is in the word being guessed

                # Runs through the entire word
                for index1 in range(len(choose_parts)):
                    if typed_key == choose_parts[index1]:
                        word = list(word)  # Puts the word in a list so indexes can be compared and switched
                        # The hyphen is replaced with the guessed letter
                        word[index2] = choose_parts[index1]
                        word = "".join(word)  # The typed word is replaced with the empty string created before

                    index1 += 1  # Goes through all indexes in the word
                    index2 += 2  # Skips over the spaces between hyphens
                    text_display(word)
                # Resets the indexes back to the original position for more letters to be guessed
                index1 = 0
                index2 = 0

                if word.replace(" ", "") == choose_parts:  # If all letters hae been guessed in the word
                    win_screen()  # Call the win screen function
                    pygame.time.delay(10000)  # Delays 10 seconds before the game quits
                    pygame.quit()

            # Checks if the inputted key is not in the word
            else:
                if typed_key not in choose_parts:
                    error_count += 1  # Adds 1 to error for each letter guessed wrong

                if error_count == 1:
                    # Displays background images based on number of errors, same operation done for each error (1-6)
                    background_image(error1)
                    text_display(word)
                    # Loads a sound effect to be played once
                    pygame.mixer.music.load("Error.mp3")
                    pygame.mixer.music.play(0)

                if error_count == 2:
                    background_image(error2)
                    text_display(word)
                    pygame.mixer.music.load("Error.mp3")
                    pygame.mixer.music.play(0)

                if error_count == 3:
                    background_image(error3)
                    text_display(word)
                    pygame.mixer.music.load("Error.mp3")
                    pygame.mixer.music.play(0)

                if error_count == 4:
                    background_image(error4)
                    text_display(word)
                    pygame.mixer.music.load("Error.mp3")
                    pygame.mixer.music.play(0)

                if error_count == 5:
                    background_image(error5)
                    text_display(word)
                    pygame.mixer.music.load("Error.mp3")
                    pygame.mixer.music.play(0)

                if error_count == 6:
                    background_image(error6)
                    text_display(word)
                    lose_screen()  # Displays the losing screen
                    pygame.mixer.music.load("Error.mp3")
                    pygame.mixer.music.play(0)
                    pygame.time.delay(4000)  # Delays 4 seconds before the game quits
                    pygame.quit()
    clock.tick(60)

pygame.quit()  # Quits the game
