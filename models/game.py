class Game:
    def __init__(self, players):
        self.players = players
        
    def gameplay(players):
        if players[0].choice == players[1].choice:
            return None
        
        if players[0].choice == "Paper" and players[1].choice == "Rock":
            return f"{players[0].name} has won Paper beats Rock"
        
        if players[0].choice == "Rock" and players[1].choice == "Scissors":
            return f"{players[0].name} has won Rock beats Scissors"
        
        if players[0].choice == "Scissors" and players[1].choice == "Paper":
            return f"{players[0].name} has won Scissors beats Paper"
        
        if players[1].choice == "Paper" and players[0].choice == "Rock":
            return f"{players[1].name} has won Paper beats Rock"
        
        if players[1].choice == "Rock" and players[0].choice == "Scissors":
            return f"{players[1].name} has won Rock beats Scissors"
        
        if players[1].choice == "Scissors" and players[0].choice == "Paper":
            return f"{players[1].name} has won Scissors beats Paper"



        
# Winning Rules as follows :

# Rock vs paper-> paper wins
# Rock vs scissor-> Rock wins
# paper vs scissor-> scissor wins.