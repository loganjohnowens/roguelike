import pygame
import sys
import random


def screen():
    global canvas
    pygame.init()
    canvas = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("roguelike")


def walls(wide, high, x, y):
    global pos
    global player_size
    global direct
    global first
    pygame.draw.rect(canvas, (210, 180, 140),
                     pygame.Rect(x, y, wide, high))
    if first:
        direct = [True, True, True, True]
    rect1 = pygame.Rect(x, y, wide, high)
    rect2 = pygame.Rect(pos[0], pos[1] - 1, player_size[0], player_size[1])
    if rect1.colliderect(rect2):
        direct[0] = False
    rect2 = pygame.Rect(pos[0] + 1, pos[1], player_size[0], player_size[1])
    if rect1.colliderect(rect2):
        direct[1] = False
    rect2 = pygame.Rect(pos[0], pos[1] + 1, player_size[0], player_size[1])
    if rect1.colliderect(rect2):
        direct[2] = False
    rect2 = pygame.Rect(pos[0] - 1, pos[1], player_size[0], player_size[1])
    if rect1.colliderect(rect2):
        direct[3] = False
    first = False


def player():
    global pos
    global player_size
    pygame.draw.rect(canvas, (0, 180, 255),
                     pygame.Rect(pos[0], pos[1], player_size[0], player_size[1]))


def player_move():
    global direct
    global pos
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] and direct[1]:
        pos[0] += 1
    if keys[pygame.K_a] and direct[3]:
        pos[0] -= 1
    if keys[pygame.K_s] and direct[2]:
        pos[1] += 1
    if keys[pygame.K_w] and direct[0]:
        pos[1] -= 1


def update_screen():
    pygame.display.flip()


def restet_screen():
    black = (0, 0, 0)
    canvas.fill(black)


def random_square():
    global tall
    global long
    global pos_tall
    global pos_long
    tall = random.randint(200, 300)
    long = random.randint(200, 300)
    pos_tall = (500 - tall) / 2
    pos_long = (500 - long) / 2


def display_random_square():
    walls(long, 20, pos_long, pos_tall)
    walls(long + 20, 20, pos_long, pos_tall + tall)
    walls(20, tall, pos_long, pos_tall)
    walls(20, tall, pos_long + long, pos_tall)


def doors():
    global tall
    global long
    global pos_tall
    global pos_long
    global new_room
    global player_size
    global pos
    rect2 = pygame.Rect(pos[0], pos[1], player_size[0], player_size[1])
    pygame.draw.rect(canvas, (255, 50, 0),
                     pygame.Rect(pos_long + long / 2, pos_tall + 20, 20, 10))
    rect1 = pygame.Rect(pos_long + long / 2, pos_tall + 20, 20, 10)
    if rect1.colliderect(rect2):
        new_room = True
    pygame.draw.rect(canvas, (255, 50, 0),
                     pygame.Rect(pos_long + long / 2, pos_tall + tall - 10, 20, 10))
    rect1 = pygame.Rect(pos_long + long / 2, pos_tall + tall - 10, 20, 10)
    if rect1.colliderect(rect2):
        new_room = True
    pygame.draw.rect(canvas, (255, 50, 0),
                     pygame.Rect(pos_long + 20, pos_tall + tall / 2, 10, 20))
    rect1 = pygame.Rect(pos_long + 20, pos_tall + tall / 2, 10, 20)
    if rect1.colliderect(rect2):
        new_room = True
    pygame.draw.rect(canvas, (255, 50, 0),
                     pygame.Rect(pos_long + long - 10, pos_tall + tall / 2, 10, 20))
    rect1 = pygame.Rect(pos_long + long - 10, pos_tall + tall / 2, 10, 20)
    if rect1.colliderect(rect2):
        new_room = True
    if new_room is True:
        random_square()
        pos = [250, 250]
        new_room = False


def dev_tools():
    global dev_mode
    global direct
    global loop
    global new_room
    keys = pygame.key.get_pressed()
    if keys[pygame.K_l]:
        dev_mode = True
    if dev_mode:
        if keys[pygame.K_LSHIFT]:
            direct = [True, True, True, True]
        if keys[pygame.K_k]:
            loop = False
        if keys[pygame.K_r]:
            new_room = True


def main():
    screen()
    global pos
    global direct
    global player_size
    global first
    global dev_mode
    global loop
    global new_room
    new_room = False
    loop = True
    dev_mode = False
    first = True
    direct = [True, True, True, True]
    pos = [250, 250]
    player_size = [10, 10]
    random_square()
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        restet_screen()
        player_move()
        player()
        display_random_square()
        dev_tools()
        doors()
        update_screen()
        first = True


main()
