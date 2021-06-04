import pygame

IMAGE = 'example.jpg'
IMAGE_BALL = 'ball.jpg'
FILE_SOUND = 'music.mp3'
WINDOWS_WIDTH = 700
WINDOWS_HEIGHT = 500
CENTER_PICTURE = (WINDOWS_WIDTH/2, WINDOWS_HEIGHT/2)
LEFT = 1
RIGHT = 3
RADIUS = 30
WHITE = (255,255,255)

pygame.init()
pygame.mixer.music.load(FILE_SOUND)


clock = pygame.time.Clock()
size = (WINDOWS_WIDTH, WINDOWS_HEIGHT)
screen = pygame.display.set_mode(size)
image = pygame.image.load(IMAGE)
image_ball = pygame.image.load(IMAGE_BALL)
screen.blit(image,(0,0))
pygame.display.set_caption("GAME")
[ball_x, ball_y] = CENTER_PICTURE
screen.blit(image_ball,[ball_x, ball_y])
pygame.display.flip()
direct_x = 3 #direction of ball 1 is right -1 is left
direct_y = 3 #direction of ball 1 is down  -1 is up

mouse_pos_list = []
finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
            pygame.mixer.music.play()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            mouse_pos_list.append(pygame.mouse.get_pos())
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direct_x = 3
            elif event.key == pygame.K_LEFT:
                direct_x = -3
            elif event.key == pygame.K_UP:
                direct_y = -3
            elif event.key == pygame.K_DOWN:
                direct_y = 3
            elif event.key == pygame.K_SPACE:
                mouse_pos_list.clear()
                direct_x = 3
                direct_y = 3
                [ball_x, ball_y] = CENTER_PICTURE

    if ball_y + image_ball.get_height() >= WINDOWS_HEIGHT:
            direct_y = -3
    elif ball_y <= 0:
            direct_y = 3
    if ball_x + image_ball.get_height() >= WINDOWS_WIDTH:
            direct_x = -3
    elif ball_x <= 0:
            direct_x = 3
    ball_x += direct_x
    ball_y += direct_y
    screen.blit(image, (0, 0))
    screen.blit(image_ball, [ball_x, ball_y])
    for sprite in mouse_pos_list:
        screen.blit(image_ball, sprite)
    pygame.display.flip()
    clock.tick(60)
