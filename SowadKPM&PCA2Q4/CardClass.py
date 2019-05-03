import pygame
# importing pygame

pygame.font.init()
font = pygame.font.SysFont(None, 50)
# init font


class card(pygame.sprite.Sprite):
    def __init__(self, suit, number, background=(0, 0, 0), width=150, height=200):
        super().__init__()
        suit = suit.lower()
        self.symbolscale = int(height / 2)
        self.width = width
        self.height = height

        if number == 11:
            number = "J"
        elif number == 12:
            number = "Q"
        elif number == 13:
            number = "K"
        elif number == 14:
            number = "A"
        number = str(number)

        self.image = pygame.Surface([self.width, self.height], pygame.SRCALPHA)
        # make sprite surface
        self.blankcard = pygame.draw.rect(self.image, (255, 255, 255), [0, 0, self.width, self.height])
        # draw sprite background
        self.border = pygame.draw.rect(self.image, background, [0, 0, self.width, self.height], 10)
        if suit == "clubs":
            self.suit = pygame.image.load("cardClass/Clubs.png")
            self.suit = pygame.transform.scale(self.suit, (self.symbolscale, self.symbolscale))
            number = font.render(number, True, (0, 0, 0), (255, 255, 255))
        if suit == "spades":
            self.suit = pygame.image.load("cardClass/Spades.png")
            self.suit = pygame.transform.scale(self.suit, (self.symbolscale, self.symbolscale))
            number = font.render(number, True, (0, 0, 0), (255, 255, 255))
        if suit == "hearts":
            self.suit = pygame.image.load("cardClass/Hearts.png")
            self.suit = pygame.transform.scale(self.suit, (self.symbolscale, self.symbolscale))
            number = font.render(number, True, (255, 0, 0), (255, 255, 255))
        if suit == "diamonds":
            self.suit = pygame.image.load("cardClass/Diamonds.png")
            self.suit = pygame.transform.scale(self.suit, (self.symbolscale, self.symbolscale))
            number = font.render(number, True, (255, 0, 0), (255, 255, 255))
        self.image.blit(self.suit, (25, 50))
        self.image.blit(number, (10, 10))

        self.rect = self.image.get_rect()
        self.angle = 0
        self.orige = self.image.copy()
        self.size = 1.0

    def move(self, posx, posy):
        self.rect.x = posx - self.width / 2
        self.rect.y = posy - self.height / 2

    def rotate(self, angle):
        self.angle -= angle
        rotImage = pygame.transform.rotozoom(self.orige, self.angle, 1.0)
        rotRect = rotImage.get_rect(center=self.rect.center)
        self.image = rotImage
        self.rect = rotRect

    def scale(self, size):
        self.size = size / 100
        sclImage = pygame.transform.rotozoom(self.orige, 0, self.size)
        sclRect = sclImage.get_rect(center=self.rect.center)
        self.image = sclImage
        self.rect = sclRect
