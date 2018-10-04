import pygame


# base enemy class, inherits from the pygame Sprite class
class Enemy(pygame.sprite.Sprite):

    # constructor, takes a tuple with a position and optionally an image path and speed list
    def __init__(self, pos, image="images/enemy.png", speed=[0, 3]):
        # call the Sprite class constructor
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = speed

    # move the enemy
    def update(self, *args):
        self.rect.move_ip(self.speed)
        # remove the enemy if it goes off screen
        if self.rect.y > pygame.display.Info().current_h:
            self.kill()

# create the FiringEnemy class here
