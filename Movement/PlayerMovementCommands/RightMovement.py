from Movement.PlayerMovementCommands.AbstractPlayerMovementCommand import AbstractPlayerMovementCommand
from Sprite.Player import Player

class RightCommand(AbstractPlayerMovementCommand):
    def __init__(self, speed: int|float):
        self.__speed = speed
    
    def __call__(self, player: Player, map: list, tile_size: int, ghosts: list):
        y = int(player.y // tile_size)
        x = int(player.x // tile_size)

        if player.x % tile_size < 11:
            player.x = player.x + self.__speed 

        elif map[y][x+1] == 0 or map[y][x+1] == 9 or map[y][x+1] == 8 or map[y][x+1] == 10:
            player.x = player.x + self.__speed
        

        if map[y][x] == 9 and (player.x - 20) % tile_size == 0:
            player.score = player.score + 10
            map[y][x] = 0

        if map[y][x] == 10 and (player.x - 7) % tile_size == 0:
            player.score = player.score + 1000
            map[y][x] = 0

        elif map[y][x] == 8 and (player.x+ - 7) % tile_size == 0:
            player.score = player.score + 50
            
            for ghost in ghosts:
                if ghost.state == "Predator":
                    ghost.enter_prey_mode()
                    
            player.enter_predator_mode()
            map[y][x] = 0