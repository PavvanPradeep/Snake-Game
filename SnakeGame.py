import pygame
import random
import time
from pygame import mixer

pygame.init()

# color

yellow = pygame.Color(255, 255, 0)

# background
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake Game')
icon = pygame.image.load('snake.png')
pygame.display.set_icon(icon)
image = pygame.image.load('background6.jpg')
apple = pygame.image.load('apple.png')
eye = pygame.image.load('snakeye4.jpg')

# music/sound
mixer.init()
eat_sound = pygame.mixer.Sound("sound.mp3")


def game():
    mixer.init()
    eat_sound = pygame.mixer.Sound("sound.mp3")

    def sound():
        pygame.mixer.Sound.play(eat_sound)

    # fps
    fps = pygame.time.Clock()

    # score
    score = 0

    # snake

    speed = 10
    snake_head_pos = [400, 480]
    snake_body_pos_init = [[400, 480], [400, 470], [400, 460], [400, 450], ]

    def draw_snake():
        for i in snake_body_pos_init:
            pygame.draw.rect(screen, yellow, pygame.Rect(i[0], i[1], 10, 10))

    # fruit
    def draw_fruit():
        screen.blit(apple, pygame.Rect(fruit_position[0], fruit_position[1], 20, 20))

    fruit_position = [random.randint(1, (800 // 10)) * 10, random.randint(1, (600 // 10)) * 10]

    fruit_spawn = True

    default_direction = 'UP'
    direction_change = default_direction

    # movement functions

    def move_up():
        snake_head_pos[1] -= 10

    def move_down():
        snake_head_pos[1] += 10

    def move_left():
        snake_head_pos[0] -= 10

    def move_right():
        snake_head_pos[0] += 10

    def display_score():
        font = pygame.font.SysFont('arial', 35)
        s = font.render(f"Score: {score}", True, (200, 200, 200))
        screen.blit(s, (600, 10))

    def game_over():
        # self.render_background()
        font = pygame.font.SysFont('arial', 35)
        line1 = font.render(f"Game Over! Your score is {score}", True, (255, 255, 255))
        screen.blit(line1, (200, 200))
        line2 = font.render(f"To play again press UP. To exit press ESC", True, (225, 225, 225))
        screen.blit(line2, (130, 300))
        pygame.display.flip()
        for i in pygame.event.get():
            if i.key == pygame.K_UP:
                game()

    # game loop

    main_code_running = True
    while main_code_running:

        screen.blit(eye, (0, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_code_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_code_running = False
                if event.key == pygame.K_UP:
                    running = True

                    while running:
                        # pygame.mixer.Sound.play(background_sound)
                        for i in pygame.event.get():
                            if i.type == pygame.QUIT:
                                running = False
                            if i.type == pygame.KEYDOWN:
                                if i.key == pygame.K_ESCAPE:
                                    running = False
                                if i.key == pygame.K_UP:
                                    direction_change = 'UP'
                                if i.key == pygame.K_DOWN:
                                    direction_change = 'DOWN'
                                if i.key == pygame.K_LEFT:
                                    direction_change = 'LEFT'
                                if i.key == pygame.K_RIGHT:
                                    direction_change = 'RIGHT'

                        if direction_change == 'UP' and default_direction != 'DOWN':
                            default_direction = 'UP'
                        if direction_change == 'DOWN' and default_direction != 'UP':
                            default_direction = 'DOWN'
                        if direction_change == 'LEFT' and default_direction != 'RIGHT':
                            default_direction = 'LEFT'
                        if direction_change == 'RIGHT' and default_direction != 'LEFT':
                            default_direction = 'RIGHT'

                        if default_direction == 'UP':
                            move_up()
                        if default_direction == 'DOWN':
                            move_down()
                        if default_direction == 'LEFT':
                            move_left()
                        if default_direction == 'RIGHT':
                            move_right()

                        snake_body_pos_init.insert(0, list(snake_head_pos))
                        if snake_head_pos[0] == fruit_position[0] and snake_head_pos[1] == fruit_position[1] or \
                                snake_head_pos[0] == \
                                fruit_position[1] and snake_head_pos[1] == (fruit_position[1]) + 1 or snake_head_pos[
                            0] == \
                                fruit_position[
                                    0] and snake_head_pos[1] == (fruit_position[1]) - 1 or snake_head_pos[0] == \
                                fruit_position[1] and \
                                snake_head_pos[1] == (fruit_position[1]) - 1:
                            score += 10
                            pygame.mixer.Sound.play(eat_sound)
                            fruit_spawn = False
                            if speed < 40:
                                speed = speed + 3
                            if speed == 40:
                                pass
                        else:
                            snake_body_pos_init.pop()

                        if not fruit_spawn:
                            fruit_position = [random.randint(1, (800 // 10)) * 10, random.randint(1, (600 // 10)) * 10]

                        fruit_spawn = True

                        screen.fill((0, 0, 0))
                        # blit function draws on screen
                        screen.blit(image, (0, 0))
                        draw_snake()
                        draw_fruit()

                        display_score()
                        if snake_head_pos[0] < 0 or snake_head_pos[0] > 800 - 10:
                            game_over()
                        if snake_head_pos[1] < 0 or snake_head_pos[1] > 600 - 10:
                            game_over()

                        pygame.display.update()
                        fps.tick(speed)


game()
