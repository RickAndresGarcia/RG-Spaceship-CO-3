from game.components.enemies.secondenemy import SecondEnemy
from game.components.enemies.enemy import Enemy


class EnemyManager:
    def __init__(self):
        self.enemies: list[Enemy] = []
        self.secondenemies: list[SecondEnemy] = []

    def update(self, game):
        if not self.enemies and not self.secondenemies:
            self.enemies.append(Enemy())
            self.secondenemies.append(SecondEnemy())
            
        for enemy in self.enemies:
            enemy.update(self.enemies, game)

        for senemy in self.secondenemies:
            senemy.update(self.secondenemies, game)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
            
        for senemy in self.secondenemies:
            senemy.draw(screen)