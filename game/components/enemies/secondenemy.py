import random
import pygame
from pygame.sprite import Sprite
from game.utils.constants import ENEMY_2, ENEMY_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH
from game.components.bullets.bullet import Bullet


class SecondEnemy(Sprite):
    X_POS_LIST = [50,100,150,200,250,300,350,400,450,500,550,500,650,700,750,800,850,900,950,1000,1050]
    Y_POS = 20
    SPEED_X = 5
    SPEED_Y = 3
    SPEED_UP = 5
    MOVEMENTS = ["left","right", "left up", "right up"]
    INDEX = 5

    def __init__(self):
        self.image = pygame.transform.scale(ENEMY_2,(50,50))
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS
        self.type = ENEMY_TYPE
        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y
        self.speed_up = self.SPEED_UP
        self.movement = self.MOVEMENTS
        self.moving_index = random.randint(0, len(self.MOVEMENTS) - 1)
        self.index = self.INDEX
        self.shooting_time = random.randint(10,15)

    def update(self, ships, game):

        self.rect.y += self.speed_y
        movement = self.movement[self.moving_index]
        self.shoot(game.bullet_manager)

        match movement:
            case "left":
                self.rect.x -= self.speed_x
            case "right":
                self.rect.x += self.speed_x
            case "left up":
                self.rect.y -= self.speed_up
                self.rect.x -= self.speed_x
            case "right up":
                self.rect.y -= self.speed_up
                self.rect.x += self.speed_x

        self.update_movement()
        if self.rect.y >= SCREEN_HEIGHT - 100:
            ships.remove(self)

    def update_movement (self):
        self.index +=1
        if self.rect.x <= 0:
            self.rect.x = SCREEN_WIDTH
        elif self.rect.x >= SCREEN_WIDTH:
            self.rect.x = 1  
        elif self.rect.y <= 0:
            self.rect.y += self.speed_y
        elif self.rect.y <= 0:
            self.rect.y += self.speed_y
        if self.index >10:
            self.moving_index = random.randint(0, len(self.MOVEMENTS) - 1)
            self.index = 0

        


    def draw(self, screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))

    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)
            self.shooting_time += random.randint(30,50)
