from Tiles.TileAbstractClass import AbstractTile
import pygame

class LeftDownPerpendicularTile(AbstractTile):
    def draw(self, win, i: int, j: int, color: tuple, size: int):
        pygame.draw.line(win, color, (j*size, i*size + int(size/2)), (j*size + int(size/2), i*size + int(size/2)), 3)
        pygame.draw.line(win, color, (j*size + int(size/2) , i*size + int(size/2)), (j*size + int(size/2), i*size + size), 3)