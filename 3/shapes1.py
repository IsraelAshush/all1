import pygame


MOVING_IMAGE = 'ball.png'
PINK = (255,174,201)
HORIZONTAL_VELOCITY = 3
VERTICAL_VELOCITY = 5
class Ball(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Ball, self).__init__()
        self.image = pygame.image.load(MOVING_IMAGE).convert()
        self.image.set_colorkey(PINK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self._vx = HORIZONTAL_VELOCITY
        self._vy = VERTICAL_VELOCITY

    def update_v(self, x, y):
        self._vx = x
        self._vy = y

    def update_loc(self):
        self.rect.x += self._vx
        self.rect.y += self._vy

    def get_pos(self):
        return self.rect.x, self.rect.y

    def get_v(self):
        return self._vx, self._vy


