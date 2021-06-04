import pygame
import random
from shapes1 import Ball

LEFT = 1
RIGHT = 3
REFRESH_RATE = 60
WINDOWS_WIDTH = 700
WINDOWS_HEIGHT = 500
IMAGE = 'example.jpg'
NUMBER_OF_BALL = 10
MAX_VELOCITY = 5
DISTANCE_X = 50
DISTANCE_Y = 25

clock = pygame.time.Clock()
size = (WINDOWS_WIDTH, WINDOWS_HEIGHT)
screen = pygame.display.set_mode(size)
image = pygame.image.load(IMAGE)
screen.blit(image,(0,0))

balls_list = pygame.sprite.Group()
balls_list_new = pygame.sprite.Group()
#balls_list_new.empty()
for i in range(NUMBER_OF_BALL):
    ball = Ball(i*DISTANCE_X,i*DISTANCE_Y)
    vx = random.randint(-MAX_VELOCITY, MAX_VELOCITY)
    vy = random.randint(-MAX_VELOCITY, MAX_VELOCITY)
    ball.update_v(vx, vy)
    balls_list.add(ball)




finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        # add a ball each time user clicks mouse
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            x,y = pygame.mouse.get_pos()
            ball = Ball(x,y)
            ball.rect.x -= ball.image.get_height()/2
            ball.rect.y -= ball.image.get_width()/2
            #אופציה שניה למימוש#ball = Ball(x - ball.image.get_height()/2 ,y - ball.image.get_width()/2)
            vx = random.randint(-MAX_VELOCITY,MAX_VELOCITY)
            vy = random.randint(-MAX_VELOCITY, MAX_VELOCITY)
            ball.update_v(vx, vy)
            balls_list.add(ball)

    #update screen with balls
    for ball in balls_list:
        ball.update_loc()
        x,y = ball.get_pos()
        vx,vy = ball.get_v()
        if (x + ball._vx > WINDOWS_WIDTH) or (x + ball._vx < 0):
            vx *= -1
        if (y + ball._vy > WINDOWS_HEIGHT) or (y + ball._vy < 0):
            vy *= -1
        ball.update_v(vx, vy)

    balls_list_new.empty()
    #for ball in balls_list:
     #   balls_hit_list = pygame.sprite.spritecollide(ball, balls_list, False)
     #   if len(balls_hit_list) == 1:
     #       balls_list_new.add(ball)
    ##balls_list.empty()
    #for ball in balls_list_new:
    #    balls_list.add(ball)
    #if len(balls_list) == 0:
     #   finish = True
    screen.blit(image, (0, 0))
    balls_list.draw(screen)
    pygame.display.flip()
    clock.tick(REFRESH_RATE)

pygame.quit()

