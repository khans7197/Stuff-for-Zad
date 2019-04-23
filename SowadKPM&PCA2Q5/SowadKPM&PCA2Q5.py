# Assignment 2
# Question 5
# Sowad Khan
# Date: April 14th, 2019
# Modifications:
# April 16th - Fixed error where bullets were one big straight line, added in king moving functions
# April 17th - Checking for collisions with bullets and the pawns
# April 18th - Added movement for enemy pawns, checking for collision between king and pawns, created game over screens
# April 19th - Added background music and sound effects for the game
# April 20th - Added instructions for the game
# April 22nd - Fixed error where scoreboard wasn't very clear, put a background behind it

# Create a game with pygame sprites
# Notes:
# King image link: https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwi_zubZlt3hAhUimuAKHWVnAGsQjRx6BAgBEAU&
# url=https%3A%2F%2Fwww.chesskid.com%2Farticle%2Fview%2Fpandolfinis-puzzler-26
# ---the-king-takes-a-walk&psig=AOvVaw0B9BxSKXXXNiNeJlZQe6VJ&ust=1555798363587790

# Pawn image link: https://media.chesskidfiles.com/images/user/tiny_mce/BoundingOwl/pawn%20dreaming%20white.png
# Background image link: https://i.pinimg.com/originals/37/71/60/37716068933bae2f9b11ff90bc91b015.png
# Shooting sound effect link: https://youtu.be/FuvmTL1nPDs
# Game background music link: https://youtu.be/_m47nceKkx4
# Win sound effect link: https://youtu.be/barWV7RWkq0
# Death sound effect link: https://youtu.be/YnREVb33zx0

# Importing pygame and random modules
import pygame
import random

# Setting up images to be used
background = "board.png"
enemy = "pawn.png"
hero = "king.png"

# Setting up colors that will be used
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (139, 69, 19)

score = 0  # Starting the score at 0 for the player

pygame.init()  # Initializing pygame
pygame.mixer.init()

# Setting up screen properties and fonts
screen_size = (700, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Shoot the pawns!")
font = pygame.font.SysFont("TimesNewRoman", 25)
win_or_lose = pygame.font.SysFont("TimesNewRoman", 60)

# Background music that will play for the entire game infinitely
pygame.mixer.music.load("Game_music.mp3")
pygame.mixer.music.play(-1)

# Loading the background image and displaying it on the screen
image = pygame.image.load(background)
screen.blit(image, (0, 0))
pygame.display.flip()

clock = pygame.time.Clock()  # Setting up a pygame clock for fps

running = True  # While the game is running
display_instructions = True  # Instructions will display unless instructed otherwise
instructions = 1  # Starting instructions at sentence 1

# The following actions will be done while the game and instructions are running
while running and display_instructions:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:  # Checking for user input on the keyboard
            if event.key == pygame.K_RETURN:  # Checking if the enter/return button has been pressed
                instructions += 1  # Instructions increase by one every time enter is pressed
                if instructions == 7:  # Instructions will go away once 7 is reached
                    display_instructions = False

    # Every time instructions increases, new rules are written and displayed below by pressing enter (1-6)
    if instructions == 1:
        text = font.render("Instructions (Press Enter to continue):", True, WHITE)
        screen.blit(text, (150, 100))

    if instructions == 2:
        text = font.render("In this game, you are a king and trying to shoot all the pawns", True, WHITE)
        screen.blit(text, (65, 150))

    if instructions == 3:
        text = font.render("Use the left and right keys to move, spacebar to shoot", True, WHITE)
        screen.blit(text, (100, 200))

    if instructions == 4:
        text = font.render("There are 30 pawns, if you get hit by one, you lose", True, WHITE)
        screen.blit(text, (100, 250))

    if instructions == 5:
        text = font.render("If you shoot all the pawns before they get you, you win", True, WHITE)
        screen.blit(text, (80, 300))

    if instructions == 6:
        text = font.render("Good luck! If you are ready to play, press Enter", True, WHITE)
        screen.blit(text, (120, 350))

    # The game will run once the instructions are finished
    if instructions == 7:
        image = pygame.image.load(background)
        screen.blit(image, (0, 0))
        pygame.display.flip()

    clock.tick(60)  # 60 fps
    pygame.display.flip()


class Pawn(pygame.sprite.Sprite):
    """This class will contain the enemy's"""

    # Initializing the class
    def __init__(self):
        super().__init__()

        # Loading the pawn image and putting it inside a rectangle to allow movement
        self.image = pygame.Surface([700, 600])
        self.image = pygame.image.load(enemy)
        self.rect = self.image.get_rect()
        self.y_speed = 1  # Setting up the pawns movement speed

    def update(self):
        """Making the pawns move up the screen"""
        self.rect.y -= self.y_speed  # Pawns move up the screen at the speed specified


class King(pygame.sprite.Sprite):
    """This class will contain the player"""

    # Initializing the class
    def __init__(self):
        super().__init__()

        # Loading the king image and putting it inside a rectangle to allow movement
        self.image = pygame.Surface([700, 600])
        self.image = pygame.image.load('king.png')
        self.rect = self.image.get_rect()

    def move_right(self):
        """Function to move the player right"""
        self.rect.x += 5  # Moves to the right by 5

        # If the player reaches the edge of the screen, they can't go further
        if self.rect.x >= 580:
            self.rect.x = 580

    def move_left(self):
        """Function to move the player left"""
        self.rect.x -= 5  # Moves to the left by 5

        # If the player reaches the edge of the screen, they can't go further
        if self.rect.x <= -50:
            self.rect.x = -50

    def update(self):
        """Updating the kings position on screen"""
        keys = pygame.key.get_pressed()  # Checks for an input by the user
        if keys[pygame.K_RIGHT]:
            king.move_right()  # Moves right if the user presses the right key

        if keys[pygame.K_LEFT]:
            king.move_left()  # Moves left if the user presses the left key

    def shoot(self):
        """Allows the player to shoot"""
        shots = Shooting(self.rect.centerx, self.rect.bottom)
        # Adding the shots to sprite lists created
        all_sprites_list.add(shots)
        shooting_list.add(shots)


class Shooting(pygame.sprite.Sprite):
    """This class will contain the bullets and shooting"""

    # Initializing the class
    def __init__(self, x, y):
        super().__init__()

        # Creating black squares for the bullets
        self.image = pygame.Surface([10, 10])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()

        # Keeping the bullets with the king and setting the firing speed
        self.rect.top = y
        self.rect.centerx = x
        self.speedy = 8

    def update(self):
        """Updates the shots from the player"""
        self.rect.y += self.speedy
        # If the bullet doesn't hit a pawn, it is removed from the screen
        if self.rect.bottom > 600:
            self.kill()


def scoreboard():
    """Contains the scoreboard for the player"""
    box = font.render("Kills: " + str(score), True, WHITE)  # Rendering font for the scoreboard
    screen.fill(BROWN, rect=box.get_rect(topright=(635, 20)))  # Filling the background of the scoreboard with brown
    screen.blit(box, (550, 20))  # Putting the scoreboard in the top right corner of the screen
    pygame.display.update()  # Updating the screen


def sound_effects(sound):
    """Sets up/initializes sound effects"""
    global effect  # Making effect global so it can be used outside this function
    effect = pygame.mixer.Sound(sound)  # Loading sound files
    effect.play(0)  # Playing sound files


def game_over(statement, color):
    """Function that contains graphics for when the game is over"""
    # Setting up fonts and creating rectangles to put them inside
    lose = win_or_lose.render(statement, True, color)
    leave = font.render("Please press Q to quit the game", True, WHITE)
    text = lose.get_rect()
    box = leave.get_rect()

    # Positioning the statements accordingly and displaying them on the screen
    text.center = (350, screen_size[1] / 2)
    box.center = (350, screen_size[1] / 1.5)
    screen.blit(lose, text)
    screen.blit(leave, box)
    King.kill(king)  # The king is removed from the screen
    pygame.display.update()

    # If the user presses "Q", pygame quits
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        pygame.quit()


# Creating sprite lists for all the classes created
all_sprites_list = pygame.sprite.Group()
pawn_list = pygame.sprite.Group()
shooting_list = pygame.sprite.Group()

# Creating instance variables for pawn and king
king = King()
pawn = Pawn()
all_sprites_list.add(king)  # Adding the king to the all sprites list


for i in range(30):
    # Creates 30 pawns randomly on the screen
    pawn = Pawn()  # Instance variable
    pawn.rect.x = random.randrange(625)
    pawn.rect.y = random.randrange(550, 1000)  # Some pawns appear bellow the screen so the user has time

    # Adding the pawns to created sprite lists
    pawn_list.add(pawn)
    all_sprites_list.add(pawn)

running = True  # While the game is running, the following actions will be done
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Stops running if the program quits
            running = False

        if event.type == pygame.KEYDOWN:  # Checks if the user enters a key on the keyboard
            if event.key == pygame.K_SPACE:  # Checks for the spacebar key
                king.shoot()  # Calling the shoot function inside the king class
                sound_effects("Shooting.wav")  # Calling the sound effect function

    # Checking for a collision between bullets and a pawn
    kills = pygame.sprite.groupcollide(pawn_list, shooting_list, True, True)

    # Every time a pawn is hit, score increases and the pawn is removed from the screen
    for kill in kills:
        pawn = Pawn()  # Instance variable
        score += 1
        all_sprites_list.remove(pawn)  # Removes the killed pawn from the sprites groups
        pawn_list.remove(pawn)
        pawn.kill()  # Removes the pawn from the screen

    death = pygame.sprite.spritecollide(king, pawn_list, False)  # Checks for a collision between the king and a pawn
    if death:  # If the king is hit, the player has lost
        game_over("YOU GOT KILLED!", RED)  # Game over function called for a loss
        sound_effects("Death.wav")  # Sound effects function called
        pygame.mixer.music.stop()  # Background music stops playing

    if score == 30:  # If the player killed all the pawns (30), they have won
        game_over("YOU BEAT THE PAWNS!", GREEN)  # Game over function called for a win
        sound_effects("Win.wav")  # Sound effects function called

    scoreboard()  # Calling the scoreboard function to display it on screen

    pygame.display.flip()  # Updating the screen and displaying everything
    all_sprites_list.clear(screen, image)  # Clearing all sprites from the screen

    all_sprites_list.update()  # Updating the all sprites list
    all_sprites_list.draw(screen)  # Drawing all sprites created on the screen

    clock.tick(60)  # Setting 60 frames per second

pygame.quit()  # Quits pygame
