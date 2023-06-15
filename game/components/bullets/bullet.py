import pygame
from pygame.sprite import Sprite
from game.utils.constants import BULLET_ENEMY, ENEMY_TYPE, SCREEN_HEIGHT

class Bullet(Sprite):
    SPEED = 20
    ENEMY_BULLET_IMG =  pygame.transform.scale(BULLET_ENEMY,(9,32))
    BULLETS = { ENEMY_TYPE:ENEMY_BULLET_IMG}

    def __init__(self, Spaceship):
        self.image = self.BULLETS[Spaceship.type]
        self.rect = self.image.get_rect()
        self.rect.center = Spaceship.rect.center
        self.owner = Spaceship.type

    def update(self, bullets):
        if self.owner == ENEMY_TYPE:
            self.rect.y += self.SPEED
            if self.rect.y > SCREEN_HEIGHT:
                bullets.remove(self)


    def draw (self,screen):
        screen.blit(self.image,(self.rect.x ,self.rect.y))