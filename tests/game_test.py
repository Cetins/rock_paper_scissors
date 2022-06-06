import unittest

from models.game import Game
from models.player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("John", "Scissors")
        self.player2 = Player("Jarrod", "Paper")
        self.player3 = Player("Morag", "Rock")
        self.player4 = Player("Alexandra", "Paper")
        self.players = (self.player1, self.player2)
        self.players2 = (self.player3, self.player4)
        self.gameplay = Game.gameplay
    
    def test_draw(self):
        self.player1.choice = "Paper"
        self.assertEqual(None, self.gameplay(self.players))
        
    def test_paper_vs_rock(self):
        self.player1.choice = "Paper"
        self.player2.choice = "Rock"
        self.player3.choice = "Rock"
        self.player4.choice = "Paper"
        self.assertEqual(f"{self.player1.name} has won Paper beats Rock", self.gameplay(self.players))
        self.assertEqual(f"{self.player4.name} has won Paper beats Rock", self.gameplay(self.players2))
        
    def test_rock_vs_scissors(self):
        self.player1.choice = "Rock"
        self.player2.choice = "Scissors"
        self.player3.choice = "Scissors"
        self.player4.choice = "Rock"
        self.assertEqual(f"{self.player1.name} has won Rock beats Scissors", self.gameplay(self.players))
        self.assertEqual(f"{self.player4.name} has won Rock beats Scissors", self.gameplay(self.players2))
        
    def test_scissors_vs_paper(self):
        self.player1.choice = "Scissors"
        self.player2.choice = "Paper"
        self.player3.choice = "Paper"
        self.player4.choice = "Scissors"
        self.assertEqual(f"{self.player1.name} has won Scissors beats Paper", self.gameplay(self.players))
        self.assertEqual(f"{self.player4.name} has won Scissors beats Paper", self.gameplay(self.players2))