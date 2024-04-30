import pygame
import random
APPLES = ['redApple', 'greenApple']

class Apple:
    
    def __init__(self):
        self.pos = (random.randint(50,1200),50)
        self.image = None
        self.loadApple()
        
    def loadApple(self):
        self.image = pygame.image.load(f'images/{random.choice(APPLES)}.png', 'png')
        self.image = pygame.transform.scale(self.image, (38, 50))
        
    def get_rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.image.get_width(), self.image.get_height())
    
    def appleFall(self):
        self.pos = (self.pos[0], self.pos[1] + 5)