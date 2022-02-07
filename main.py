import pygame
import random
from pygame import mixer

# Pygame init
pygame.font.init()
pygame.init()
main_font = pygame.font.SysFont("comicsans", 25)

# window screen
width = 800
height = 600

WIN = pygame.display.set_mode((width, height))

# Program window info

pygame.display.set_caption("Simon Game")
pygame.display.set_icon(pygame.image.load('GameFiles/icon.png'))

# Loading buttons and sounds

BUTTONS = [
    pygame.image.load('GameFiles/blue.png').convert_alpha(),
    pygame.image.load('GameFiles/green.png').convert_alpha(),
    pygame.image.load('GameFiles/red.png').convert_alpha(),
    pygame.image.load('GameFiles/yellow.png').convert_alpha()
]

BUTTONS_LIT = [
    pygame.image.load('GameFiles/blue1.png'),
    pygame.image.load('GameFiles/green1.png'),
    pygame.image.load('GameFiles/red1.png'),
    pygame.image.load('GameFiles/yellow1.png')
]

SOUNDS = [
    mixer.Sound('GameSounds/blue.mp3'),
    mixer.Sound('GameSounds/green.mp3'),
    mixer.Sound('GameSounds/red.mp3'),
    mixer.Sound('GameSounds/yellow.mp3'),
    mixer.Sound('GameSounds/wrong.mp3')
]

POS = [
    (width / 2 - BUTTONS[0].get_width() - 5, height / 2 - BUTTONS[0].get_height() + 15),
    (width / 2 + 5, height / 2 - BUTTONS[1].get_height() + 15),
    (width / 2 - BUTTONS[3].get_width() - 5, height / 2 + 25),
    (width / 2 + 5, height / 2 + 25)
]
# Function to lit buttons


def onclick(clicked1):
    WIN.blit(BUTTONS_LIT[clicked1], POS[clicked1])
    SOUNDS[clicked1].play()
    pygame.display.update()
    pygame.time.delay(200)


def redraw():
    WIN.fill((25, 25, 25))
    start = main_font.render("Press <ANY_KEY> to start the game", 1, (255, 0, 0))
    level = main_font.render(f"Level: {len(genclick)}", 1, (255, 0, 0))
    WIN.blit(start, (width / 2 - start.get_width() / 2, 0))
    WIN.blit(level, (width / 2 - level.get_width() / 2, 40))
    WIN.blit(BUTTONS[0], POS[0])
    WIN.blit(BUTTONS[1], POS[1])
    WIN.blit(BUTTONS[2], POS[2])
    WIN.blit(BUTTONS[3], POS[3])
    pygame.display.update()


genclick = []
clicked = []


def game():
    redraw()
    pygame.time.delay(500)
    gen = random.randint(1, 4)
    if gen == 1:
        onclick(0)
        genclick.append(0)
    if gen == 2:
        onclick(1)
        genclick.append(1)
    if gen == 3:
        onclick(2)
        genclick.append(2)
    if gen == 4:
        onclick(3)
        genclick.append(3)


def check_game():
    if clicked[-1] == genclick[len(clicked) - 1]:
        if len(clicked) == len(genclick):
            game()
            clicked.clear()
    else:
        print("You failed")
        clicked.clear()
        genclick.clear()
        SOUNDS[4].play()


def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    clock.tick(FPS)
    mask = pygame.mask.from_surface(BUTTONS[0])
    mask1 = pygame.mask.from_surface(BUTTONS[1])
    while run:
        redraw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                clicked.clear()
                genclick.clear()
                game()

            if event.type == pygame.MOUSEBUTTONDOWN:
                try:
                    if mask.get_at((event.pos[0] - POS[0][0], event.pos[1] - POS[0][1])):
                        onclick(0)
                        clicked.append(0)
                        check_game()
                except IndexError:
                    pass

                try:
                    if mask1.get_at((event.pos[0] - POS[1][0], event.pos[1] - POS[1][1])):
                        onclick(1)
                        clicked.append(1)
                        check_game()
                except IndexError:
                    pass

                try:
                    if mask1.get_at((event.pos[0] - POS[2][0], event.pos[1] - POS[2][1])):
                        onclick(2)
                        clicked.append(2)
                        check_game()
                except IndexError:
                    pass

                try:
                    if mask1.get_at((event.pos[0] - POS[3][0], event.pos[1] - POS[3][1])):
                        onclick(3)
                        clicked.append(3)
                        check_game()
                except IndexError:
                    pass

main()
