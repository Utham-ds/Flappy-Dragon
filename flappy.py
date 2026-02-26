import sys, subprocess

subprocess.check_call([sys.executable, "-m", "pip", "install", "-U", "pygame"])

import pygame
import random

# Game state
GAME_STATE_START = 0
GAME_STATE_PLAYING = 1
GAME_STATE_GAME_OVER = 2

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 500, 600
GROUND_HEIGHT = 75
FPS = 30
GRAVITY = 1.5
FLAP_STRENGTH = -10
PIPE_WIDTH = 50
PIPE_GAP = 150

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wing Flapper")

# Load assets
bird_image = pygame.image.load("assets/dragon.png")
background_image = pygame.image.load("assets/Background.jpg")
pipe_image = pygame.image.load("assets/Pipe.png")

# Scale assets
bird_image = pygame.transform.scale(bird_image, (50, 50))
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
pipe_image = pygame.transform.scale(pipe_image, (PIPE_WIDTH, HEIGHT - GROUND_HEIGHT))

# Create bird
bird_rect = bird_image.get_rect()
bird_rect.centerx = WIDTH // 4
bird_rect.centery = HEIGHT // 2
bird_y_speed = 0

# Create ground
ground_rect = pygame.Rect(0, HEIGHT - GROUND_HEIGHT, WIDTH, GROUND_HEIGHT)

# Create pipes
pipes = []
pipe_timer = pygame.time.get_ticks()

# Score
score = 0
font = pygame.font.Font(None, 36)

# Levels
levels = [
    {"pipe_speed": 5, "spawn_frequency": 2000, "score_threshold": 20},
    {"pipe_speed": 6, "spawn_frequency": 1800, "score_threshold": float("inf")},  # Infinite level
]

# Current level
current_level = 0

# Game state
game_state = GAME_STATE_START

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_state == GAME_STATE_PLAYING:
                bird_y_speed = FLAP_STRENGTH
            elif event.key == pygame.K_SPACE and game_state == GAME_STATE_START:
                game_state = GAME_STATE_PLAYING
            elif event.key == pygame.K_SPACE and game_state == GAME_STATE_GAME_OVER:
                game_state = GAME_STATE_START
                bird_rect.centerx = WIDTH // 4
                bird_rect.centery = HEIGHT // 2
                bird_y_speed = 0
                pipes = []
                score = 0
                current_level = 0  # Reset to the first level

    # Update bird
    bird_y_speed += GRAVITY
    bird_rect.centery += bird_y_speed

    # Check collision with ground
    if bird_rect.colliderect(ground_rect):
        game_state = GAME_STATE_GAME_OVER

    # Update pipes
    if pygame.time.get_ticks() - pipe_timer > levels[current_level]["spawn_frequency"]:
        pipe_height = random.randint(100, HEIGHT - GROUND_HEIGHT - PIPE_GAP - 100)
        top_pipe_rect = pipe_image.get_rect(midbottom=(WIDTH, pipe_height))
        bottom_pipe_rect = pipe_image.get_rect(midtop=(WIDTH, pipe_height + PIPE_GAP))
        pipes.append((top_pipe_rect, bottom_pipe_rect))
        pipe_timer = pygame.time.get_ticks()

    for top_pipe, bottom_pipe in pipes:
        top_pipe.centerx -= levels[current_level]["pipe_speed"]
        bottom_pipe.centerx -= levels[current_level]["pipe_speed"]

        # Check collision with pipes
        if bird_rect.colliderect(top_pipe) or bird_rect.colliderect(bottom_pipe):
            game_state = GAME_STATE_GAME_OVER

        # Remove off-screen pipes
        if top_pipe.right < 0:
            pipes.remove((top_pipe, bottom_pipe))
            score += 1

    # Draw everything
    screen.blit(background_image, (0, 0))
    for top_pipe, bottom_pipe in pipes:
        screen.blit(pipe_image, top_pipe)
        screen.blit(pipe_image, bottom_pipe)
    screen.blit(bird_image, bird_rect)
    pygame.draw.rect(screen, GREEN, ground_rect)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (20, 20))

    # Display level information
    level_text = font.render(f"Level {current_level + 1}", True, WHITE)
    screen.blit(level_text, (20, HEIGHT - 60))

    if game_state == GAME_STATE_START:
        start_text = font.render("Press SPACE to Start", True, WHITE)
        screen.blit(start_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
    elif game_state == GAME_STATE_GAME_OVER:
        game_over_text = font.render("Game Over. Press SPACE to Restart", True, WHITE)
        screen.blit(game_over_text, (WIDTH // 2 - 200, HEIGHT // 2 - 50))

    pygame.display.flip()

    # Check if it's time to switch to the next level
    if score >= levels[current_level]["score_threshold"]:
        current_level += 1
        if current_level < len(levels):
            bird_rect.centerx = WIDTH // 4  # Reset bird's position
            bird_rect.centery = HEIGHT // 2
            pipes = []  # Reset pipes
        else:
            game_state = GAME_STATE_GAME_OVER  # No more levels, end the game

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
