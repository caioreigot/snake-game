import pygame, random, sys
from time import sleep
from pygame import *

def playGame():

    font = pygame.font.Font('freesansbold.ttf', 18)
    score = 0

    def wait():
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN and event.key == K_r:
                    playGame()

    def on_grid_random():
        x = random.randint(0,590)
        y = random.randint(0,590)
        return (x//10 * 10, y//10 * 10)

    def collision(c1, c2):
        return (c1[0] == c2[0]) and (c1[1] == c2[1])

    def gameOver():
        screen.fill((0,0,0))
        # mensagem de game over
        gameOverFont = pygame.font.Font('freesansbold.ttf', 72)
        gameOverSurf = gameOverFont.render('Game Over', True, whitecolour)
        gameOverRect = gameOverSurf.get_rect()
        gameOverRect.midtop = (290, 240)
        screen.blit(gameOverSurf, gameOverRect)
        # mensagem score
        scorefont = pygame.font.Font('freesansbold.ttf', 32)
        score_font = scorefont.render('Score: %s' % (score), True, (255, 0 , 0))
        score_rect = score_font.get_rect()
        score_rect.midtop = (285, 365)
        screen.blit(score_font, score_rect)
        # mensagem restarting
        restart_font = font.render('Press button "R" to restart', True, whitecolour)
        restart_rect = score_font.get_rect()
        restart_rect.midtop = (240, 315)
        screen.blit(restart_font, restart_rect)
        pygame.display.flip()
        # tempo de espera de 3 segundos antes de reiniciar o jogo
        wait()

    whitecolour = pygame.Color(255,255,255)

    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    screen = pygame.display.set_mode((600,600))
    pygame.display.set_caption('Snake')

    clock = pygame.time.Clock()

    snake = [(260, 220), (270, 220), (280, 220)]
    my_direction = LEFT
    snake_skin = pygame.Surface((10,10))
    snake_skin.fill((255, 255, 255))

    apple_pos = on_grid_random()
    apple = pygame.Surface((10,10))
    apple.fill((255,0,0))

    while True:
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if event.type == KEYDOWN:
                if event.key == K_UP:
                    my_direction = UP
                if event.key == K_DOWN:
                    my_direction = DOWN
                if event.key == K_LEFT:
                    my_direction = LEFT
                if event.key == K_RIGHT:
                    my_direction = RIGHT

        # comendo a maça e aumentando o tamanho da cobra
        if collision(snake[0], apple_pos):
            apple_pos = on_grid_random()
            snake.append((0,0))
            score += 1

        # colisão com as bordas
        if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake [0][1] < 0:
            gameOver() 

        # colisão com ela mesma
        for i in range(1, len(snake) - 1):
            if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
                gameOver()

        for i in range(len(snake) - 1, 0, -1):
            snake[i] = (snake[i-1][0], snake[i-1][1])

        if my_direction == UP:
            snake[0] = (snake[0][0], snake[0][1] - 10)
        
        if my_direction == DOWN:
            snake[0] = (snake[0][0], snake[0][1] + 10)

        if my_direction == RIGHT:
            snake[0] = (snake[0][0] + 10, snake[0][1])

        if my_direction == LEFT:
            snake[0] = (snake[0][0] - 10, snake[0][1])

        screen.fill((0,0,0))
        screen.blit(apple, apple_pos)

        # se quiser desenhar linhas no jogo, descomente o código abaixo
        # for x in range(0, 600, 10):
        #     pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 600))
        # for y in range(0, 600, 10):
        #     pygame.draw.line(screen, (40, 40, 40), (0, y), (600, y))

        score_font = font.render('Score: %s' % (score), True, whitecolour)
        score_rect = score_font.get_rect()
        score_rect.topleft = (600 - 90, 10)
        screen.blit(score_font, score_rect)

        for pos in snake:
            screen.blit(snake_skin,pos)

        pygame.display.update()

pygame.init()

playGame()