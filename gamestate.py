import pygame
import random

class GameState:
    def __init__(self, max_misses):
        self.score = 0
        self.misses = 0
        self.max_misses = max_misses
        self.is_game_over = False
    
    def increase_score(self):
        self.score += 1
    
    def record_miss(self):
        self.misses += 1
        if self.misses >= self.max_misses:
            self.is_game_over = True
    
    def reset(self):
        self.score = 0
        self.misses = 0
        self.is_game_over = False
    
    def get_score_text(self):
        return f"Score: {self.score}"
    
    def get_misses_text(self):
        return f"Misses: {'X' * self.misses}"