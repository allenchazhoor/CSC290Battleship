import pygame, crayons

size = (1000, 1000)
fill_color = (0, 0, 0) # RGB black

pygame.init()

pygame.font.init()

print(crayons.yellow('Initialized PyGame'));

arial = pygame.font.SysFont("Arial", 30)

text = arial.render("Welcome to DreadNought", False, (255, 255, 255))

screen = pygame.display.set_mode(size)

running = True

def keyboard(key):

    if key == pygame.K_x:
        global running
        running = False

print(crayons.yellow('Entering main game loop'))

while running: # Main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # User has requested that the game exit
            running = False # Exits the loop, therefore the game
        elif event.type == pygame.KEYDOWN:
            keyboard(event.key) # Handle keyboard
        
        if not running:
            break

    screen.fill( fill_color ) # Clear screen

    screen.blit(text, (100, 100)) # Render text

    pygame.display.flip() # Render

# Exit


