import pygame
import random
import sys

pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color Quest Game")

# Fonts and colors
font = pygame.font.SysFont("arial", 48)
small_font = pygame.font.SysFont("arial", 30)

COLORS = {
    "RED": (255, 0, 0),
    "GREEN": (0, 255, 0),
    "BLUE": (0, 0, 255),
    "YELLOW": (255, 255, 0),
    "CYAN": (0, 255, 255),
    "MAGENTA": (255, 0, 255),
}

color_keys = {
    pygame.K_r: "RED",
    pygame.K_g: "GREEN",
    pygame.K_b: "BLUE",
    pygame.K_y: "YELLOW",
    pygame.K_c: "CYAN",
    pygame.K_m: "MAGENTA",
}

score = 0
time_left = 30  # seconds
clock = pygame.time.Clock()

# Pick first word and actual color
def new_round():
    word = random.choice(list(COLORS.keys()))
    color = random.choice(list(COLORS.keys()))
    return word, color

word, color = new_round()
start_ticks = pygame.time.get_ticks()

# Game loop
while True:
    screen.fill((30, 30, 30))

    # Timer
    seconds_passed = (pygame.time.get_ticks() - start_ticks) / 1000
    remaining = max(0, time_left - int(seconds_passed))

    # End screen
    if remaining == 0:
        end_text = font.render(f"Time's Up! Score: {score}", True, (255, 255, 255))
        screen.blit(end_text, (100, 170))
        pygame.display.update()
        pygame.time.delay(3000)
        pygame.quit()
        sys.exit()

    # Display word with mismatched color
    text = font.render(word, True, COLORS[color])
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 120))

    score_text = small_font.render(f"Score: {score}", True, (255, 255, 255))
    time_text = small_font.render(f"Time: {remaining}", True, (255, 255, 255))
    screen.blit(score_text, (20, 20))
    screen.blit(time_text, (480, 20))

    # Instructions
    inst = small_font.render("Press key of TEXT COLOR (R,G,B,Y,C,M)", True, (200, 200, 200))
    screen.blit(inst, (60, 300))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key in color_keys:
                if color_keys[event.key] == color:
                    score += 1
                word, color = new_round()

    pygame.display.update()
    clock.tick(60)
