from Movement.PlayerMovementDirectionSetter.AbstractPlayerDirectionSetterCommand import AbstractPlayerDirectionSetterCommand
from Sprite.Player import Player

class LeftDirectionSetterCommand(AbstractPlayerDirectionSetterCommand):
    def __init__(self, player: Player):
        self.__player = player

    def __call__(self):
        self.__player.next_direction = "Left"