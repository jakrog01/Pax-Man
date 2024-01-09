from Movement.GhostsStrategies.AbstractGhostStrategy import AbstractGhostStrategy

class ClairvoyantNormalStrategy(AbstractGhostStrategy):
    def choose_direction(self, clairvoyant, pacman, tile_size, map, *args):

        clairvoyant_x = int(clairvoyant.x // tile_size)
        clairvoyant_y = int(clairvoyant.y // tile_size)

        destination_x = int(pacman.x // tile_size)
        destination_y = int(pacman.y // tile_size)

        if pacman.direction == "Up":
            destination_y -= 4
        elif pacman.direction == "Down":
            destination_y += 4
        elif pacman.direction == "Right":
            destination_x += 4
        elif pacman.direction == "Left":
            destination_x -= 4

        distance = 1000000
        new_direction = "None"

        if clairvoyant.direction != "Left":
            if map[clairvoyant_y][clairvoyant_x+1] == 9 or map[clairvoyant_y][clairvoyant_x+1] == 0 or map[clairvoyant_y][clairvoyant_x+1] == 8:
                new_distance = ((clairvoyant_x+1) - destination_x)**2 + (clairvoyant_y - destination_y)**2
                if new_distance < distance:
                    new_direction = "Right"
                    distance = new_distance
        
        if clairvoyant.direction != "Right":
            if map[clairvoyant_y][clairvoyant_x-1] == 9 or map[clairvoyant_y][clairvoyant_x-1] == 0 or map[clairvoyant_y][clairvoyant_x-1] == 8:
                new_distance = ((clairvoyant_x-1) - destination_x)**2 + (clairvoyant_y - destination_y)**2
                if new_distance < distance:
                    new_direction = "Left"
                    distance = new_distance
        
        if clairvoyant.direction != "Up":
            if map[clairvoyant_y+1][clairvoyant_x] == 9 or map[clairvoyant_y+1][clairvoyant_x] == 0 or map[clairvoyant_y+1][clairvoyant_x] == 8:
                new_distance = (clairvoyant_x - destination_x)**2 + ((clairvoyant_y+1) - destination_y)**2
                if new_distance < distance:
                    new_direction = "Down"
                    distance = new_distance
        
        if clairvoyant.direction != "Down":
            if map[clairvoyant_y-1][clairvoyant_x] == 9 or map[clairvoyant_y-1][clairvoyant_x] == 0 or map[clairvoyant_y-1][clairvoyant_x] == 7 or map[clairvoyant_y-1][clairvoyant_x] == 8:
                new_distance = (clairvoyant_x - destination_x)**2 + ((clairvoyant_y-1) - destination_y)**2
                if new_distance < distance:
                    new_direction = "Up"
                    distance = new_distance

        if new_direction == "None":
            clairvoyant.inverse_direction()
        else:
            clairvoyant.direction = new_direction
        
            