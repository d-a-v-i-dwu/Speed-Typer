import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))

# Set the title of the game window
pygame.display.set_caption('2D Sidescroller')

# Create the player's character
player = pygame.Rect(300, 550, 60, 60)

# Create a variable to control the player's movement
move_right = False
move_left = False

# Create a background image
bg = pygame.image.load('background.png')

# Create a function to draw the game on the screen
def draw_game():
  # Clear the screen
  screen.blit(bg, (0,0))

  # Draw the player on the screen
  pygame.draw.rect(screen, (255,0,0), player)

  # Update the display
  pygame.display.update()

# Create the main game loop
while True:
  # Check for events
  for event in pygame.event.get():
    # Quit the game if the player closes the window
    if event.type == pygame.QUIT:
      pygame.quit()

    # Set the movement variables based on the player's input
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        move_right = True
      if event.key == pygame.K_LEFT:
        move_left = True

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_RIGHT:
        move_right = False
      if event.key == pygame.K_LEFT:
        move_left = False

  # Move the player
  if move_right:
    player.x += 5
  if move_left:
    player.x -= 5

  # Draw the game on the screen
  draw_game()