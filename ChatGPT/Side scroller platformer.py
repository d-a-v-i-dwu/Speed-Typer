import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the width and height of the screen
size = [700, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("2D Platformer")

# Loop until the user clicks the close button
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Set the speed at which the screen scrolls
scroll_speed = 10

# Initialize the player's position
player_position = [50, 50]

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # Move the player
    player_position[0] += scroll_speed

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)

    # --- Drawing code should go here
    # Draw the player
    pygame.draw.rect(screen, BLACK, [player_position[0], player_position[1], 50, 50])