import pygame

IMAGE = 'example.jpg'
IMAGE_BALL = 'ball.jpg'
WINDOWS_WIDTH = 700
WINDOWS_HEIGHT = 500
LEFT = 1
RIGHT = 2

pygame.init()
#pygame.mouse.set_visible(False)

clock = pygame.time.Clock()
size = (WINDOWS_WIDTH, WINDOWS_HEIGHT)
screen = pygame.display.set_mode(size)
image = pygame.image.load(IMAGE)
image_ball = pygame.image.load(IMAGE_BALL)
screen.blit(image,(0,0))
pygame.display.set_caption("GAME")
pygame.display.flip()

mouse_pos_list = []
finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            mouse_pos_list.append(pygame.mouse.get_pos())
            mouse_point = pygame.mouse.get_pos()
            screen.blit(image_ball,mouse_point)
    pygame.display.flip()
    clock.tick(60)

#pygame.quit()