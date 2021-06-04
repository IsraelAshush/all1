

#WINDOWS_WIDTH = 511
#WINDOWS_HEIGHT = 511
#BLACK = (0,0,0)
#WHITE = (255,255,255)
#size = (WINDOWS_WIDTH,WINDOWS_HEIGHT)
#screen = pygame.display.set_mode(size)
#screen.fill(WHITE)
#for i in range (0,511 , 51):
#    pygame.draw.line(screen, BLACK, (i, 0), (i, WINDOWS_HEIGHT))
#for j in range (0,511 , 51):
#    pygame.draw.line(screen, BLACK, (0, j), (WINDOWS_WIDTH, j))
#pygame.image.save(screen, r"C:\Networks\Pyhton3.8\classBegin\4\Board.jpg")
import pygame
import Plane
import random

def out_of_window(x,y):
    if (x > 0 and x < WINDOWS_HEIGHT and y > 0 and y < WINDOWS_HEIGHT):
        return False
    return True

def check_colision(plane, players_list):
    list_colision = []
    for i in range(-1,2,1):
        for j in range (-1,2,1):
            if((i,j)==(0,0)):
                continue
            plane.update_pos(i*51, j*51)
            plane_colision_list = pygame.sprite.spritecollide(plane, players_list, False)
            if len(plane_colision_list) == 1:
                list_colision.append((i,j))
            plane.update_pos(-i*51, -j*51)
    if len(list_colision) == 0:
        return False, list_colision
    return True, list_colision

def go_rand(plane, players_list):
    x,y = plane.get_pos()
    plane_check = Plane.plane(x,y)
    colision, list_colision = check_colision(plane_check, players_list)
    if not colision:
        return True,0,0
    else:
        for i in range(-1, 2, 1):
            for j in range(-1, 2, 1):
                if((i,j) in list_colision):
                    continue
                if ((i, j) == (0,0)):
                    continue
                if (out_of_window(plane_check.get_pos()[0]+i*51, plane_check.get_pos()[1]+j*51)):
                    continue
                plane_check.update_pos(i * 51, j * 51)
                check, list_colision_new_position = check_colision(plane_check, players_list)
                if len(list_colision_new_position) == 1:
                    return False, i, j
                plane_check.update_pos(-i * 51, -j * 51)


        list_rand_pos = []
        for i in range(-1, 2, 1):
            for j in range(-1, 2, 1):
                if((i,j) != (0,0) and (i, j) not in list_colision and not (out_of_window(plane_check.get_pos()[0]+i*51, plane_check.get_pos()[1]+j*51))):
                    list_rand_pos.append((i,j))
        if (len(list_rand_pos)>0):
            x,y = random.choice(list_rand_pos)
            return False, x,y
        return True, i, j



WINDOWS_WIDTH = 511
WINDOWS_HEIGHT = 511
PLAYERS = 5
LOOP = 1000
FRAME_RATE = 60
size = (WINDOWS_WIDTH,WINDOWS_HEIGHT)
screen = pygame.display.set_mode(size)
board = pygame.image.load(r"C:\Networks\Pyhton3.8\classBegin\4\Board.jpg")
screen.blit(board,(0,0))
pygame.display.set_caption("AirGame")

clock = pygame.time.Clock()
players_list = pygame.sprite.Group()
start_position_check = []
for i in range(0, PLAYERS, 1):
    x_plane = 1 + random.randint(0,9)*51
    y_plane = 1 + random.randint(0,9)*51
    while (x_plane, y_plane) in start_position_check:
        x_plane = 1 + random.randint(0, 9) * 51
        y_plane = 1 + random.randint(0, 9) * 51
    if i < 3:
        plane = Plane.plane(x_plane, y_plane, r"C:\Networks\Pyhton3.8\classBegin\4\Player_" + str(i) + ".png")
    else:
        plane = Plane.plane(x_plane, y_plane)
    start_position_check.append((x_plane,y_plane))
    players_list.add(plane)
players_list.draw(screen)


pygame.display.flip()
finish = False
score = 0
loop = 0
while (not finish) and loop != LOOP:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
    for plane in players_list:
        go,x,y = go_rand(plane, players_list)
        if go:
            x = random.randint(-1,1)
            y = random.randint(-1,1)
            while ((x,y) == (0,0)) or out_of_window(plane.get_pos()[0]+x*51, plane.get_pos()[1]+y*51):
                x = random.randint(-1, 1)
                y = random.randint(-1, 1)
        else:
            score -= 1
        plane.update_move(x, y)
        plane.update_pos(x*51, y*51)
        screen.blit(board, (0, 0))
        players_list.draw(screen)
        pygame.display.flip()
        plane_colision_list = pygame.sprite.spritecollide(plane,players_list,False)
        if len(plane_colision_list) == 1:
            score += 1
        else:
            finish = True
            break

    loop += 1
    clock.tick(FRAME_RATE)

print (score)
