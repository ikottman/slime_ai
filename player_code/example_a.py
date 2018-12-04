from slime_mind.models.player_base import PlayerBase
from slime_mind.models.commands import Commands
import random

class Player(PlayerBase):
    # example player AI
    def __init__(self, id):
        super().__init__(id, "AI name here a")

    def command_slime(self, state, slime, turn):
        # bite randomly
        move_options = [Commands.BITELEFT,Commands.BITERIGHT,Commands.BITEUP,Commands.BITEDOWN]
        return random.choice(move_options)
