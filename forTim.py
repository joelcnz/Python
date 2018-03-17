import pygame
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

x = 300
y = 100

updown = 0.0
swingSize = 10
yoffSet = 0.0

def processAndDrawStuff():
    # Draw on the screen a line from (0,0) to (100,100)
    # 5 pixels wide.
    yoffSet = math.sin(updown) * swingSize
    pygame.draw.line(screen, GREEN, [x, y + yoffSet], [x + 100, y + 100 + yoffSet], 5)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # Draw on the screen a line from (0,0) to (100,100)
    # 5 pixels wide.
    
    yoffSet = math.sin(updown) * swingSize
    processAndDrawStuff()
    #pygame.draw.line(screen, GREEN, [x, y + yoffSet], [x + 100, y + 100 + yoffSet], 5)
    # --- Drawing code should go here
    #x += 2
    if (x + 100 > 700):
        x = 0
    updown += 0.2
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
