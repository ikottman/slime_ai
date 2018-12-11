from slime_mind.models.player_base import PlayerBase
from slime_mind.models.commands import Commands
import random

class Player(PlayerBase):
    # example player AI
    def __init__(self, id):
        super().__init__(id, "AI name here 1", 'custom_sprites/example_custom_basic.png', 'custom_sprites/example_custom_king.png')

    def command_slime(self, state, slime, turn):
        # Move randomly
        move_options = [Commands.LEFT,Commands.RIGHT,Commands.UP,Commands.DOWN]
        return random.choice(move_options)
