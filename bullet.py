import pygame.image
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Manages bullets fired by the ship"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load bullet and set position
        self.image = pygame.image.load(self.settings.bullet_image_path)
        self.rect = self.image.get_rect()
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        # Update the decimal position of the bullet
        self.y -= self.settings.bullet_speed
        # Update the rect position of the bullet
        self.rect.y = round(self.y)

    def blitme(self):
        """Draw the bullet at its current location"""
        self.screen.blit(self.image, self.rect)
