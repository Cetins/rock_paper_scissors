class Game:
    def __init__(self, players):
        self.players = players
        
    def gameplay(players):
        if players[0].choice == players[1].choice:
            return None
        if players[0].choice == "Paper" and players[1].choice == "Rock":
            return players[0].name
        if players[0].choice == "Rock" and players[1].choice == "Scissors":
            return players[0].name
        if players[0].choice == "Scissors" and players[1].choice == "Paper":
            return players[0].name
        else:
            return players[1].name
        



        
# Winning Rules as follows :

# Rock vs paper-> paper wins
# Rock vs scissor-> Rock wins
# paper vs scissor-> scissor wins.