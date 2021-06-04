import pygame
import math

#constant vars
IMAGE = 'example.jpg'
WINDOWS_WIDTH = 700
WINDOWS_HEIGHT = 500
CENTER_PICTURE = (WINDOWS_WIDTH/2, WINDOWS_HEIGHT/2)
RADIUS = 30
WHITE = (255,255,255)
REFRESH_RATE = 300


pygame.init()
size = (WINDOWS_WIDTH, WINDOWS_HEIGHT)
screen = pygame.display.set_mode(size)
#screen.fill(WHITE)
#pygame.display.flip()
img = pygame.image.load(IMAGE)
screen.blit(img, (0,0))
pygame.display.set_caption("Game")
#pygame.draw.line(screen, WHITE, CENTER_PICTURE, [90, 90], 5)  [CENTER_PICTURE[0] + math.cos(3.6*x)*150, CENTER_PICTURE[1] + math.cos(3.6*x)*150] [10*x, 10*x]
pygame.draw.circle(screen, WHITE, CENTER_PICTURE, RADIUS, )
pygame.display.flip()

clock = pygame.time.Clock()
[ball_x, ball_y] = CENTER_PICTURE


finish = False
direct_x = 1
direct_y = 1
refrash = 0
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
            #refrash += 1
    screen.blit(img, (0, 0))
    if ball_y == WINDOWS_HEIGHT:
        direct_y = -1
    elif ball_y == 0:
        direct_y = 1
    if ball_x == WINDOWS_WIDTH:
        direct_x =-1
    elif ball_x == 0:
        direct_x = 1
    ball_x += direct_x
    ball_y += direct_y

    for line in range(1, 101, 1):
        x = math.cos(math.radians(3.6 * line)) * RADIUS
        y = math.sin(math.radians(3.6 * line)) * RADIUS
        pygame.draw.line(screen, WHITE, [ball_x + x, ball_y + y], [CENTER_PICTURE[0] + x*5, CENTER_PICTURE[1] + y*5], 1)

    pygame.draw.circle(screen, WHITE, [ball_x, ball_y], RADIUS, )
    pygame.display.flip()
    clock.tick(REFRESH_RATE + refrash )

pygame.quit()



"""
def main():
    print ('0')



if __name__ == '__main__':
    main()

"""