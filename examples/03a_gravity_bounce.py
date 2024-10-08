"""
Gravity bounce with x motion

If we add X velocity, from side to side, the player will bounce around the
screen. We will need to add a check to see if the player hits the left or right
side of the screen.

"""
import pygame
from dataclasses import dataclass

@dataclass
class Settings:
    """Class for keeping track of game settings and constants."""
    screen_width: int = 500
    screen_height: int = 500
    white: tuple = (255, 255, 255)
    black: tuple = (0, 0, 0)
    red: tuple = (255, 0, 0)
    player_size: int = 20
    gravity: int = 1
    jump_velocity: int = 30

# Initialize Pygame
pygame.init()

# Create an instance of Settings
settings = Settings()

# Initialize screen
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

# Define player
player = pygame.Rect(100, settings.screen_height - settings.player_size, settings.player_size, settings.player_size)
player_y_velocity = 0
player_x_velocity = 10

is_jumping = False

# Main game loop
running = True
clock = pygame.time.Clock()

while running:

    # Handle events, such as quitting the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Continuously jump. If the player is not jumping, may it jump
    if is_jumping is False:
        # Jumping means that the player is going up. The top of the 
        # screen is y=0, and the bottom is y=settings.screen_height. So, to go up,
        # we need to have a negative y velocity
        player_y_velocity = -settings.jump_velocity
        is_jumping = True

    # If the player hits one side of the screen or the other, bounce the player
    if player.left <= 0 or player.right >= settings.screen_width:
        player_x_velocity = -player_x_velocity

    # If the player hits the top of the screen, bounce the player
    if player.top <= 0:
        player_y_velocity = -player_y_velocity

    # Update player position. Gravity is always pulling the player down,
    # which is the positive y direction, so we add settings.gravity to the y velocity
    # to make the player go up more slowly. Eventually, the player will have
    # a positive y velocity, and gravity will pull the player down.
    player_y_velocity += settings.gravity
    player.y += player_y_velocity
    player.x += player_x_velocity

    # If the player hits the ground, stop the player from falling.
    # The player's position is measured from the top left corner, so the
    # bottom of the player is player.y + settings.player_size. If the bottom of the
    # player is greater than the height of the screen, the player is on the
    # ground. So, set the player's y position to the bottom of the screen
    # and stop the player from falling
    if player.bottom >= settings.screen_height:
        player.bottom = settings.screen_height
        player_y_velocity = 0
        is_jumping = False

    # Draw everything
    screen.fill(settings.white)
    pygame.draw.rect(screen, settings.black, player)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
