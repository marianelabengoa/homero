import pygame

class Dona:
    def __init__(self, size, coordenate, path_imagen):
        self.size=size
        self.coordenate=coordenate
        self.imagen=pygame.transform.scale(pygame.image.load(path_imagen).convert_alpha(), size)
        self.rect=self.imagen.get_rect()
        self.rect.topleft=coordenate
        self.active=True

    def update(self):
        self.rect.y+=5