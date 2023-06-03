import pygame
import random

# Initialize Pygame
pygame.init()

# Set the width and height of the game window
window_width = 400
window_height = 600
window = pygame.display.set_mode((window_width, window_height))

# Set the title of the game window
pygame.display.set_caption("Flappy Bird")

# Load the background image
background_img = pygame.image.load("background.png").convert()

# Load the bird image
bird_img = pygame.image.load("bird.png").convert_alpha()
bird_rect = bird_img.get_rect()
bird_rect.x = 50
bird_rect.y = int(window_height / 2)

# Load the pipe images
pipe_img = pygame.image.load("pipe.png").convert_alpha()

# Set the gravity
gravity = 0.5

# Set the velocity
bird_velocity = 0

# Create a list to store the pipes
pipes = []
pipe_gap = 150
pipe_frequency = 1500
last_pipe_time = pygame.time.get_ticks()

# Set the game over flag
game_over = False

# Set the clock to control the frame rate
clock = pygame.time.Clock()

# Function to display the score
def display_score(score):
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    window.blit(score_text, (10, 10))

# Function to display the game over message
def display_game_over():
    font = pygame.font.Font(None, 72)
    game_over_text = font.render("Game Over", True, (255, 0, 0))
    window.blit(game_over_text, (window_width / 2 - game_over_text.get_width() / 2, window_height / 2 - game_over_text.get_height() / 2))

# Game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = -10

    # Update the bird's position
    bird_velocity += gravity
    bird_rect.y += bird_velocity

    # Update the pipes
    if pygame.time.get_ticks() - last_pipe_time > pipe_frequency:
        pipe_height = random.randint(100, 400)
        pipe_rect_bottom = pipe_img.get_rect()
        pipe_rect_bottom.x = window_width
        pipe_rect_bottom.y = pipe_height + pipe_gap
        pipe_rect_top = pipe_img.get_rect()
        pipe_rect_top.x = window_width
        pipe_rect_top.y = pipe_height - pipe_rect_top.height
        pipes.append((pipe_rect_bottom, pipe_rect_top))
        last_pipe_time = pygame.time.get_ticks()

    for pipe in pipes:
        pipe[0].x -= 5
        pipe[1].x -= 5
        if pipe[0].x + pipe[0].width < 0:
            pipes.remove(pipe)

    # Check for collision
    for pipe in pipes:
        if bird_rect.colliderect(pipe[0]) or bird_rect.colliderect(pipe[1]):
            game_over = True

    # Check for bird out of screen
    if bird_rect.y < 0 or bird_rect.y + bird_rect.height > window_height:
        game_over = True

    # Draw the background
    window.blit(background_img, (0, 0))

    # Draw the bird
    window.blit(bird_img, bird_rect)

    # Draw the pipes
    for pipe in pipes:
        window.blit(pipe_img, pipe[0])
        window.blit(pygame.transform.flip(pipe_img, False, True), pipe[1])

    # Display the score
    display_score(len(pipes))

    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)

# Game over
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Display the game over message
    display_game_over()

    # Update the display
    pygame.display.update()
