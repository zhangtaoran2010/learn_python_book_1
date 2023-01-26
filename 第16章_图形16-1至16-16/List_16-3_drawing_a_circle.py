import pygame,sys
pygame.init()
screen = pygame.display.set_mode([640,480])
# Add these three lines
screen.fill([255,255,255]) # Fills the window with a white background
pygame.draw.circle(screen,[255,0,0],[100,100],30,0) # Draw a circle
pygame.display.flip()  # Flips your monitor over.... just kidding!
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
