import pygame
    
class Player:
    def __init__(self, position):
        self.position = position
        self.image = None
        self.loadPlayer()

    def loadPlayer(self):
        self.image = pygame.image.load('images/newton.png', 'r')
        self.image = pygame.transform.scale(self.image, (150, 125))

    def draw(self, screen):
        screen.blit(self.image, self.position)
        
    def moveLeft(self, distance):
        self.position = (self.position[0] - distance, self.position[1])

    def moveRight(self, distance):
        self.position = (self.position[0] + distance, self.position[1])
        
    def get_rect(self):
        return pygame.Rect(self.position[0], self.position[1], self.image.get_width(), self.image.get_height())