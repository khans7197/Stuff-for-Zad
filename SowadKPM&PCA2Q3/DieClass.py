# This is a die class created by ICS3U-02 2018-19
# Teacher Ms. Harris
# This is a whole class one day (exploded into 4 days assignment) - formative
# Shell added by Ms. Harris (Teacher) April 7/10
# Modifications:
# Apr. 8/19 - Number 9 Added by Ziv, Sowad, and Victor
# Apr. 15/19 - Number 3 Added by Karan, Ciara, and Thomas
# 2019/04/16 - Ziv - fixed up implementation
# added 7-9 Sri, Simha, Karan

# Create class
import pygame
import random

class DieGame:

       # Initiallize class
    def __init__(self, screen, width, height):
        # finish this
        self.screen = screen
        self.width = width
        self.height = height
        self.one_image = pygame.image.load("dieClass/one.png")
        self.two_image = pygame.image.load("dieClass/two.png")
        self.three_image = pygame.image.load("dieClass/three.png")
        self.four_image = pygame.image.load("dieClass/four.png")
        self.five_image = pygame.image.load("dieClass/five.png")
        self.six_image = pygame.image.load("dieClass/six.png")
        self.seven_image = pygame.image.load("dieClass/seven.png")
        self.eight_image = pygame.image.load("dieClass/eight.png")
        self.nine_image = pygame.image.load("dieClass/nine.png")

        self.one_image = pygame.transform.scale(self.one_image, [512, 512])
        self.two_image = pygame.transform.scale(self.two_image, [512, 512])
        self.three_image = pygame.transform.scale(self.three_image, [512, 512])
        self.four_image = pygame.transform.scale(self.four_image, [512, 512])
        self.five_image = pygame.transform.scale(self.five_image, [512, 512])
        self.six_image = pygame.transform.scale(self.six_image, [512, 512])
        self.seven_image = pygame.transform.scale(self.seven_image, [512, 512])
        self.eight_image = pygame.transform.scale(self.eight_image, [512, 512])
        self.nine_image = pygame.transform.scale(self.nine_image, [512, 512])

        

    def random(self):
        choice = random.choice(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])
        if choice == "one":
            self.one()
        if choice == "two":
            self.two()
        if choice == "three":
            self.three()
        if choice == "four":
            self.four()
        if choice == "five":
            self.five()
        if choice == "six":
            self.six()
        if choice == "seven":
            self.seven()
        if choice == "eight":
            self.eight()
        if choice == "nine":
            self.nine()
            
    # get values and draw the one
    def one(self):
        self.screen.blit(self.one_image, (self.width/2-256,self.height/2-256))
    # get values and draw the two
    def two(self):
        self.screen.blit(self.two_image, (self.width/2-256,self.height/2-256))
        
    # get values and draw the three
    def three(self):
        self.screen.blit(self.three_image, (self.width/2-256,self.height/2-256))

   # get values and draw the four
    def four(self):
        self.screen.blit(self.four_image, (self.width/2-256,self.height/2-256))

   # get values and draw the five
    def five(self):
        self.screen.blit(self.five_image,(self.width/2-256,self.height/2-256))
        
   # get values and draw the six
    def six(self):
        self.screen.blit(self.six_image, (self.width/2-256,self.height/2-256))
        
   # get values and draw the seven
    def seven(self):
        self.screen.blit(self.seven_image, (self.width/2-256,self.height/2-256))
        
   # get values and draw the eight
    def eight(self):
        self.screen.blit(self.eight_image, (self.width/2-256,self.height/2-256))
        
   # get values and draw the nine
    def nine(self):
        self.screen.blit(self.nine_image, (self.width/2-256,self.height/2-256))
