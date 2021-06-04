import pygame
import math

#constant vars
IMAGE = 'example.jpg'
WINDOWS_WIDTH = 700
WINDOWS_HEIGHT = 500
CENTER_PICTURE = (WINDOWS_WIDTH/2, WINDOWS_HEIGHT/2)
RADIUS = 30
WHITE = (255,255,255)


#draw screen init and ball
pygame.init()
size = (WINDOWS_WIDTH, WINDOWS_HEIGHT)
screen = pygame.display.set_mode(size)
#screen.fill(WHITE)
#pygame.display.flip()
img = pygame.image.load(IMAGE)
screen.blit(img, (0,0))
pygame.display.set_caption("Game")
pygame.draw.circle(screen, WHITE, CENTER_PICTURE, RADIUS, )
pygame.display.flip()
#
#the ball moves
clock = pygame.time.Clock()
[ball_x, ball_y] = CENTER_PICTURE
finish = False
direct_x = 3 #direction of ball 1 is right -1 is left
direct_y = 3 #direction of ball 1 is down  -1 is up
max_len_line = 0
index_len_line = 1
list_net = []
flash_rate_left = 200
flash_rate_right = 200
for i in range(1,101,1):
    list_net.append(i)
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
    screen.blit(img, (0, 0))
    if ball_y >= WINDOWS_HEIGHT:
        direct_y = -3
        flag = True
    elif ball_y <= 0:
        direct_y = 3
        flag = True
    if ball_x >= WINDOWS_WIDTH:
        direct_x =-3
        list_net.remove(index_len_line)
        flash_rate_right += 0
    elif ball_x <= 0:
        direct_x = 3
        list_net.remove(index_len_line)
        flash_rate_left += 0

    ball_x += direct_x
    ball_y += direct_y
    max_len_line = 0
    index_len_line = 1
    #
    #draw the net
    for line in list_net:
        x = math.cos(math.radians(3.6 * line)) * RADIUS
        y = math.sin(math.radians(3.6 * line)) * RADIUS
        pygame.draw.line(screen, WHITE, [ball_x + x, ball_y + y], [CENTER_PICTURE[0] + x*5, CENTER_PICTURE[1] + y*5], 1)

        len_line = math.sqrt(((ball_x + x) - (CENTER_PICTURE[0] + x*5))**2 + (((ball_y + y) - (CENTER_PICTURE[1] + y*5))**2))
        if max_len_line < len_line:
            max_len_line = len_line
            index_len_line = line
    pygame.draw.circle(screen, WHITE, [ball_x, ball_y], RADIUS, )
    pygame.display.flip()
    if direct_x > 1:
        clock.tick(flash_rate_right)
    elif direct_x < -1:
        clock.tick(flash_rate_left)

pygame.quit()



"""
def main():
    print ('0')



if __name__ == '__main__':
    main()

"""