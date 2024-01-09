from Movement.PacmanMovementCommands.AbstractPacmanMovementCommand import AbstractPacmanMovementCommand

class UpCommand(AbstractPacmanMovementCommand):
    def __init__(self, speed):
        self.__speed = speed
    
    def __call__(self, pacman, map, tile_size, ghosts):
        y = int(pacman.y // tile_size)
        x = int(pacman.x // tile_size)
        
        if (pacman.y) % tile_size > 11:
                pacman.y = pacman.y - self.__speed

        elif map[y-1][x] == 0 or map[y-1][x] == 9 or map[y-1][x] == 8 or map[y-1][x] == 10:
                pacman.y = pacman.y - self.__speed

        if map[y][x] == 9 and (pacman.y + 20) % tile_size == 0:
            pacman.score = pacman.score + 10
            map[y][x] = 0
        
        if map[y][x] == 10 and (pacman.y + 20) % tile_size == 0:
            pacman.score = pacman.score + 1000
            map[y][x] = 0

        elif map[y][x] == 8 and (pacman.y + 7) % tile_size == 0:
            pacman.score = pacman.score + 50

            for ghost in ghosts:
                if ghost.state == "Predator":
                    ghost.enter_prey_mode()
                    
            pacman.enter_predator_mode()
            map[y][x] = 0