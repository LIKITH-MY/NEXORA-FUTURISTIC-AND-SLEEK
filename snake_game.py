# Snake game logic
import pygame
import threading
import random

def run_snake_game():

    def game():

        WIDTH = 400
        HEIGHT = 400
        BLOCK = 20

        pygame.init()

        screen = pygame.display.set_mode(
            (WIDTH, HEIGHT)
        )

        pygame.display.set_caption(
            "Nexora Snake Game"
        )

        clock = pygame.time.Clock()

        snake = [[100, 100]]

        food = [
            random.randrange(0, WIDTH, BLOCK),
            random.randrange(0, HEIGHT, BLOCK)
        ]

        direction = "RIGHT"

        running = True

        while running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

            screen.fill((0, 0, 0))

            pygame.draw.rect(
                screen,
                (255, 0, 0),
                (*food, BLOCK, BLOCK)
            )

            for part in snake:

                pygame.draw.rect(
                    screen,
                    (0, 255, 0),
                    (*part, BLOCK, BLOCK)
                )

            pygame.display.update()

            clock.tick(10)

        pygame.quit()

    threading.Thread(
        target=game,
        daemon=True
    ).start()
