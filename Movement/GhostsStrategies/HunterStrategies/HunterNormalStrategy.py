from Movement.GhostsStrategies.AbstractGhostStrategy import AbstractGhostStrategy

from Sprite.AbstractGhost import AbstractGhost
from Sprite.Player import Player

class HunterNormalStrategy(AbstractGhostStrategy):
    def choose_direction(self, hunter: AbstractGhost, player: Player, tile_size: int, map: list, *args):
        hunter_x = int(hunter.x // tile_size)
        hunter_y = int(hunter.y // tile_size)

        destination_x = int(player.x // tile_size)
        destination_y = int(player.y // tile_size)

        distance = 1000000
        new_direction = "None"

        if hunter.direction != "Left":
            if map[hunter_y][hunter_x+1] == 9 or map[hunter_y][hunter_x+1] == 0 or map[hunter_y][hunter_x+1] == 8 or map[hunter_y][hunter_x+1] == 10:
                new_distance = ((hunter_x+1) - destination_x)**2 + (hunter_y - destination_y)**2
                if new_distance < distance:
                    new_direction = "Right"
                    distance = new_distance
        
        if hunter.direction != "Right":
            if map[hunter_y][hunter_x-1] == 9 or map[hunter_y][hunter_x-1] == 0  or map[hunter_y][hunter_x-1] == 8 or map[hunter_y][hunter_x-1] == 10:
                new_distance = ((hunter_x-1) - destination_x)**2 + (hunter_y - destination_y)**2
                if new_distance < distance:
                    new_direction = "Left"
                    distance = new_distance
        
        if hunter.direction != "Up":
            if map[hunter_y+1][hunter_x] == 9 or map[hunter_y+1][hunter_x] == 0 or map[hunter_y+1][hunter_x] == 8 or map[hunter_y+1][hunter_x] == 10:
                new_distance = (hunter_x - destination_x)**2 + ((hunter_y+1) - destination_y)**2
                if new_distance < distance:
                    new_direction = "Down"
                    distance = new_distance
        
        if hunter.direction != "Down":
            if map[hunter_y-1][hunter_x] == 9 or map[hunter_y-1][hunter_x] == 0 or map[hunter_y-1][hunter_x] == 7 or map[hunter_y-1][hunter_x] == 8 or map[hunter_y-1][hunter_x] == 10:
                new_distance = (hunter_x - destination_x)**2 + ((hunter_y-1) - destination_y)**2
                if new_distance < distance:
                    new_direction = "Up"
                    distance = new_distance

        if new_direction == "None":
           hunter.inverse_direction()
        else:
            hunter.direction = new_direction
        
            