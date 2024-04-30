import pygame
from newton import Player
from apple import Apple
from gamestate import GameState


# Constants for screen dimensions and maximum misses
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
MAX_MISSES = 3

def main():

    # Initialize Pygame
    pygame.init()

    # Set up the screen dimensions
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()

    # Create the player instance
    myPlayer = Player(position=(80, 600))

    # Create an initial apple
    myApple = Apple()

    # Initialize the font
    font = pygame.font.Font(None, 36)

    # Initialize the gamestate
    game_state = GameState(MAX_MISSES)

    # Main game loop
    running = True
    while running and not game_state.is_game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill('black')
        
        # Render score and misses using GameState
        score_text = font.render(game_state.get_score_text(), True, (255, 255, 255))
        misses_text = font.render(game_state.get_misses_text(), True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        screen.blit(misses_text, (10, 40))
        
        myPlayer.draw(screen)
        screen.blit(myApple.image, myApple.pos)
        
        myApple.appleFall()
        
        if myApple.pos[1] > SCREEN_HEIGHT:
            game_state.record_miss()
            myApple = Apple()  # Create a new apple
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            myPlayer.moveLeft(8)
        if keys[pygame.K_d]:
            myPlayer.moveRight(8)
        
        # Check for collision between player and apple
        if myPlayer.get_rect().colliderect(myApple.get_rect()):
            game_state.increase_score()  # Increase score
            myApple = Apple()  # Create a new apple
        
        pygame.display.flip()
        clock.tick(60)  # 60 frames per second

    pygame.quit()

    # Run the game
if __name__ == "__main__":
    main()