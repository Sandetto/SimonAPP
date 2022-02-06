import pygame
import time
import random
from pygame import mixer

# Pygame font initialize
pygame.font.init()
# Required line
pygame.init()

# Creating screen
width = 1200
height = 1000
WIN = pygame.display.set_mode((width, height))

# BG image & music
BG = pygame.image.load('GameFiles/background.jpg')
#mixer.music.load('GameSounds/red.mp3')
#mixer.music.play(-1)

# title and icon
pygame.display.set_caption("Simon Game")
icon = pygame.image.load('GameFiles/icon.png')
pygame.display.set_icon(icon)

# Buttons
BLUE = pygame.image.load('GameFiles/blue.png')
BLUELIT = pygame.image.load('GameFiles/blue1.png')
GREEN = pygame.image.load('GameFiles/green.png')
GREENLIT = pygame.image.load('GameFiles/green1.png')
RED = pygame.image.load('GameFiles/red.png')
REDLIT = pygame.image.load('GameFiles/red1.png')
YELLOW = pygame.image.load('GameFiles/yellow.png')
YELLOWLIT = pygame.image.load('GameFiles/yellow1.png')


def redlit():
    redsound = mixer.Sound('GameSounds/red.mp3')
    redsound.play()
    WIN.blit(REDLIT, (width / 2 - RED.get_width() - 5, height / 2 - RED.get_height() + 15))
    pygame.display.update()


def bluelit():
    bluesound = mixer.Sound('GameSounds/blue.mp3')
    bluesound.play()
    WIN.blit(BLUELIT, (width / 2 + 5, height / 2 - BLUE.get_height() + 15))
    pygame.display.update()


def yellowlit():
    yellowsound = mixer.Sound('GameSounds/yellow.mp3')
    yellowsound.play()
    WIN.blit(YELLOWLIT, (width / 2 - YELLOW.get_width() - 5, height / 2 + 25))
    pygame.display.update()


def greenlit():
    greensound = mixer.Sound('GameSounds/green.mp3')
    greensound.play()
    WIN.blit(GREENLIT, (width / 2 + 5, height / 2 + 20 + 5))
    pygame.display.update()


def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    clock.tick(FPS)
    main_font = pygame.font.SysFont("comicsans", 25)
    answers = []
    clicks = []

    def redraw_window():
        WIN.fill((25, 25, 25))
        # Draw text
        start = main_font.render("Press <ANY_KEY> to start the game", 1, (255, 0, 0))
        level = main_font.render(f"Level: {len(answers)}", 1, (255, 0, 0))
        WIN.blit(start, (width / 2 - start.get_width() / 2, 0))
        WIN.blit(level, (width / 2 - level.get_width() / 2, 40))
        WIN.blit(RED, (width / 2 - RED.get_width() - 5, height / 2 - RED.get_height() + 20 - 5))
        WIN.blit(BLUE, (width / 2 + 5, height / 2 - BLUE.get_height() + 20 - 5))
        WIN.blit(YELLOW, (width / 2 - YELLOW.get_width() - 5, height / 2 + 20 + 5))
        WIN.blit(GREEN, (width / 2 + 5, height / 2 + 20 + 5))
        pygame.display.update()

    def start_game():
        generator = random.randint(1, 4)
        if generator == 1:
            redraw_window()
            redlit()
            pygame.display.update()
            answers.append(1)
            time.sleep(1)
        elif generator == 2:
            redraw_window()
            bluelit()
            pygame.display.update()
            answers.append(2)
            time.sleep(1)
        elif generator == 3:
            redraw_window()
            yellowlit()
            pygame.display.update()
            answers.append(3)
            time.sleep(1)
        elif generator == 4:
            redraw_window()
            greenlit()
            pygame.display.update()
            answers.append(4)
            time.sleep(1)

    def check():
        if clicks[-1] == answers[len(clicks) - 1]:
            if len(clicks) == len(answers):
                time.sleep(1)
                start_game()
                clicks.clear()
        else:
            print("You failed")
            clicks.clear()
            answers.clear()
            failsound = mixer.Sound('GameSounds/wrong.mp3')
            failsound.play()

    while run:
        try:
            clock.tick(FPS)
            redraw_window()
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    clicks.clear()
                    answers.clear()
                    start_game()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if width / 2 - RED.get_width() - 5 <= mouse[0] <= width / 2 - 5 and\
                            height / 2 - RED.get_height() + 20 - 5 <= mouse[1] <= height / 2 + 15:
                        redlit()
                        redraw_window()
                        clicks.append(1)
                        check()
                        redraw_window()
                    if width / 2 + 5 <= mouse[0] <= width / 2 + BLUE.get_width() + 5 and\
                            height / 2 - BLUE.get_height() + 15 <= mouse[1] <= height / 2 + 15:
                        bluelit()
                        redraw_window()
                        clicks.append(2)
                        check()
                        redraw_window()
                    if width / 2 - YELLOW.get_width() - 5 <= mouse[0] <= width / 2 - 5 and\
                            height / 2 + 25 <= mouse[1] <= height / 2 + YELLOW.get_height() + 25:
                        yellowlit()
                        redraw_window()
                        clicks.append(3)
                        check()
                        redraw_window()
                    if width / 2 + 5 <= mouse[0] <= width / 2 + GREEN.get_width() + 5 and\
                            height / 2 + 25 <= mouse[1] <= height / 2 + GREEN.get_height() + 25:
                        greenlit()
                        redraw_window()
                        clicks.append(4)
                        check()
                        redraw_window()
        except IndexError:
            continue

main()

