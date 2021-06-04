import pygame
import math

IMAGE = 'example.jpg'
WINDOWS_WIDTH = 700
WINDOWS_HEIGHT = 500
CENTER_PICTURE = (WINDOWS_WIDTH/2, WINDOWS_HEIGHT/2)
WHITE = (255,255,255)

pygame.init()
size = (WINDOWS_WIDTH, WINDOWS_HEIGHT)
screen = pygame.display.set_mode(size)
#screen.fill(WHITE)
#pygame.display.flip()
img = pygame.image.load(IMAGE)

screen.blit(img, (0,0))
pygame.display.set_caption("Game")
#pygame.draw.line(screen, WHITE, CENTER_PICTURE, [90, 90], 5)  [CENTER_PICTURE[0] + math.cos(3.6*x)*150, CENTER_PICTURE[1] + math.cos(3.6*x)*150] [10*x, 10*x]
for line in range(1,100,1):
    x =math.cos(math.radians(3.6*line))*150
    y =math.sin(math.radians(3.6*line))*150
    pygame.draw.line(screen, WHITE, CENTER_PICTURE,[CENTER_PICTURE[0] + x, CENTER_PICTURE[1] + y],1)
pygame.display.flip()
pygame.image.save(screen, r"C:\Networks\Pyhton3.8\classBegin\3\test.jpg")

finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
pygame.quit()

"""
def main():
    print ('0')



if __name__ == '__main__':
    main()

"""