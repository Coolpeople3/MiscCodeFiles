import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the display in fullscreen mode
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # Fullscreen mode
pygame.display.set_caption("Dark Screen Mode")

# Create a surface filled with black color to simulate a dark screen
dark_surface = pygame.Surface((screen.get_width(), screen.get_height()))
dark_surface.fill((0, 0, 0))  # Fill with black

# Main loop
running = True
while running:
    for event in pygame.event.get():
        # If the user presses the spacebar, the screen returns to normal
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            running = False  # Exit the loop and return to normal screen

        # If the user presses the close button, we ignore it
        if event.type == pygame.QUIT:
            continue  # Do nothing if the user tries to quit via the close button

    # Blit the dark surface over the entire screen
    screen.blit(dark_surface, (0, 0))
    pygame.display.update()  # Update the screen to show the dark surface

# Quit pygame and close the window
pygame.quit()
sys.exit()
