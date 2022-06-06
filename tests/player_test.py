from typing_extensions import Self
import unittest

from models.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("John", "Scissors")
        self.player2 = Player("Jarrod", "Paper")
        
    def test_player_has_name(self):
        self.assertEqual("John", self.player1.name)
        
    def test_player_has_choice(self):
        self.assertEqual("Paper", self.player2.choice)