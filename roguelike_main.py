import pygame
import sys
import random
import time


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
    global blocked_doors
    global room_shape
    global up_down
    global left_right
    room_shape = random.randint(1, 2)
    genorate_blocked_doors()
    door_check()
    tall = random.randint(200, 400)
    long = random.randint(200, 400)
    pos_tall = (500 - tall) / 2
    pos_long = (500 - long) / 2
    up_down = random.randint(100, tall - 50)
    left_right = random.randint(100, long - 100)


def display_random_square():
    global room_shape
    global long
    global pos_long
    global pos_tall
    global tall
    global up_down
    global left_right
    if room_shape == 1:
        walls(long, 20, pos_long, pos_tall)
        walls(long + 20, 20, pos_long, pos_tall + tall)
        walls(20, tall, pos_long, pos_tall)
        walls(20, tall, pos_long + long, pos_tall)
    if room_shape == 2:
        walls(long + 20, 20, pos_long, pos_tall + tall)
        walls(20, tall, pos_long, pos_tall)
        walls(long - left_right, 20, pos_long, pos_tall)
        walls(20, tall - up_down, pos_long + long - left_right, pos_tall)
        walls(left_right + 20, 20, long - left_right +
              pos_long, tall - up_down + pos_tall)
        walls(20, up_down, long + pos_long, tall - up_down + pos_tall)


def doors():
    global tall
    global long
    global pos_tall
    global pos_long
    global new_room
    global player_size
    global pos
    global curent_room
    global visted_rooms
    global blocked_doors
    global left_right
    global up_down
    if room_shape == 1:
        display_doors(pos_long + long / 2, pos_tall + 20, 20, 10, 0)
    if room_shape == 2:
        display_doors(
            pos_long + (long - left_right) / 2, pos_tall + 20, 20, 10, 0)
    if room_shape == 1:
        display_doors(pos_long + long - 10, pos_tall + tall / 2, 10, 20, 1)
    if room_shape == 2:
        display_doors(pos_long + long - 10, tall - up_down +
                      pos_tall + up_down / 2, 10, 20, 1)
    display_doors(pos_long + long / 2, pos_tall + tall - 10, 20, 10, 2)
    display_doors(pos_long + 20, pos_tall + tall / 2, 10, 20, 3)


def dev_tools():
    global dev_mode
    global direct
    global loop
    global new_room
    global visted_rooms
    global curent_room
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
        if keys[pygame.K_v]:
            print(visted_rooms)
        if keys[pygame.K_c]:
            print(curent_room)


def def_vars():
    global pos
    global direct
    global player_size
    global first
    global dev_mode
    global loop
    global new_room
    global visted_rooms
    global curent_room
    curent_room = [0, 0]
    visted_rooms = {}
    new_room = False
    loop = True
    dev_mode = False
    first = True
    direct = [True, True, True, True]
    pos = [250, 250]
    player_size = [10, 10]


def first_is_true():
    global first
    first = True


def exit_button():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def frame_cap(sleep):
    time.sleep(sleep)


def set_up_visted_rooms():
    global blocked_doors
    global room_shape
    global long
    global pos_long
    global pos_tall
    global tall
    global up_down
    global left_right
    visted_rooms[(0, 0)] = {
        'room_shape_1': room_shape,
        'long': long,
        'pos_long': pos_long,
        'pos_tall': pos_tall,
        'tall': tall,
        'up_down': up_down,
        'left_right': left_right,
        'blocked_doors': blocked_doors
    }


def respawn(new_square):
    global movement_change
    global pos
    global room_shape
    if new_square:
        random_square()
    if movement_change == (0, -1) and room_shape == 1:
        pos = [pos_long + long / 2, pos_tall + 40]
    if movement_change == (0, -1) and room_shape == 2:
        pos = [pos_long + (long - left_right) / 2, pos_tall + 40]
    if movement_change == (-1, 0) and room_shape == 1:
        pos = [pos_long + long - 10 - 20, pos_tall + tall / 2]
    if movement_change == (-1, 0) and room_shape == 2:
        pos = [pos_long + long - 10 - 20, tall -
               up_down + pos_tall + up_down / 2]
    if movement_change == (0, 1):
        pos = [pos_long + long / 2, pos_tall + tall - 10 - 20]
    if movement_change == (1, 0):
        pos = [pos_long + 40, pos_tall + tall / 2]


def door_check():
    global blocked_doors
    check = 0
    while True:
        for i in blocked_doors:
            if i > 7:
                check += 1
        if check == 4:
            blocked_doors[0] = random.randint(0, 10)
            blocked_doors[1] = random.randint(0, 10)
            blocked_doors[2] = random.randint(0, 10)
            blocked_doors[3] = random.randint(0, 10)
        else:
            break


def display_doors(x_long, y_long, x, y, directoin_of_door):
    global curent_room
    global new_room
    global blocked_doors
    global room_shape
    global long
    global pos_long
    global pos_tall
    global tall
    global up_down
    global left_right
    global movement_change
    used_rooms = False
    how_to_change_cords = {
        0: (0, 1),
        1: (1, 0),
        2: (0, -1),
        3: (-1, 0)
    }
    rect2 = pygame.Rect(pos[0], pos[1], player_size[0], player_size[1])
    if blocked_doors[directoin_of_door] < 8 and blocked_doors[directoin_of_door] < 8:
        pygame.draw.rect(canvas, (255, 50, 0),
                         pygame.Rect(x_long, y_long, x, y))
    rect1 = pygame.Rect(x_long, y_long, x, y)

    if rect1.colliderect(rect2) and blocked_doors[directoin_of_door] < 8:
        new_room = True
        if directoin_of_door in how_to_change_cords:
            movement_change = how_to_change_cords[directoin_of_door]
            curent_room = (
                curent_room[0] + movement_change[0], curent_room[1] + movement_change[1])
            if curent_room in visted_rooms:
                room_shape = visted_rooms[curent_room]['room_shape_1']
                long = visted_rooms[curent_room]['long']
                pos_long = visted_rooms[curent_room]['pos_long']
                pos_tall = visted_rooms[curent_room]['pos_tall']
                tall = visted_rooms[curent_room]['tall']
                up_down = visted_rooms[curent_room]['up_down']
                left_right = visted_rooms[curent_room]['left_right']
                blocked_doors = visted_rooms[curent_room]['blocked_doors']
                respawn(False)
                used_rooms = True
            else:
                if new_room is True and used_rooms is not True:
                    respawn(True)
                visted_rooms[(curent_room)] = {
                    'room_shape_1': room_shape,
                    'long': long,
                    'pos_long': pos_long,
                    'pos_tall': pos_tall,
                    'tall': tall,
                    'up_down': up_down,
                    'left_right': left_right,
                    'blocked_doors': blocked_doors
                }
    new_room = False


def genorate_blocked_doors():
    global visted_rooms
    global blocked_doors
    blocked_doors = [0, 0, 0, 0]
    how_to_change_cords = {
        0: (0, 1),
        1: (1, 0),
        2: (0, -1),
        3: (-1, 0)
    }
    round_number = 0
    almost_blocked_doors = [False, False, False, False]
    for checking_room in (how_to_change_cords[0], how_to_change_cords[1], how_to_change_cords[2], how_to_change_cords[3]):
        if (curent_room[0] + checking_room[0], curent_room[1] + checking_room[1]) in visted_rooms:
            almost_blocked_doors[round_number] = visted_rooms[
                curent_room[0] + checking_room[0], curent_room[1] + checking_room[1]]['blocked_doors']
        round_number += 1

    if almost_blocked_doors[0] is not True:
        blocked_doors[0] = random.randint(0, 10)
    if almost_blocked_doors[0] is not False:
        blocked_doors[0] = almost_blocked_doors[0][2]

    if almost_blocked_doors[1] is not True:
        blocked_doors[1] = random.randint(0, 10)
    if almost_blocked_doors[1] is not False:
        blocked_doors[1] = almost_blocked_doors[1][3]

    if almost_blocked_doors[2] is not True:
        blocked_doors[2] = random.randint(0, 10)
    if almost_blocked_doors[2] is not False:
        blocked_doors[2] = almost_blocked_doors[2][0]

    if almost_blocked_doors[3] is not True:
        blocked_doors[3] = random.randint(0, 10)
    if almost_blocked_doors[3] is not False:
        blocked_doors[3] = almost_blocked_doors[3][1]


def set_to_square():
    global room_shape
    room_shape = 1


def main():
    screen()
    def_vars()
    random_square()
    set_up_visted_rooms()
    set_to_square()
    while loop:
        exit_button()
        restet_screen()
        player_move()
        player()
        display_random_square()
        dev_tools()
        doors()
        update_screen()
        first_is_true()
        frame_cap(.005)


main()
