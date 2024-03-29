from Sprite.GhostMakers.AbstractGhostMaker import AbstractGhostMaker
from Sprite.Ignoramus import Ignoramus
import pygame
import os

class IgnoramusMaker(AbstractGhostMaker):
    def __init__(self):
        self.__picture = pygame.transform.scale(pygame.image.load( os.path.join("Sprite", "Graphics", "Ignoramus.png")), (32,32))

    def make(self, args: list) -> Ignoramus:
        return Ignoramus(args[0],args[1], args[2],args[3], args[4], self.__picture)