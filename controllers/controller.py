import random
from flask import render_template, request

from app import app

from models.game import Game
from models.player import Player

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/two_players')
def two_players():
    return render_template("two_players.html")        

@app.route('/winner', methods=['POST'])
def game_play():
    player1 = Player("Player1", request.form["choice1"])
    player2 = Player("Player2", request.form["choice2"])
    players = [player1, player2]
    winner = Game.gameplay(players)
        
    return render_template("winner.html", winner=winner)

@app.route('/player_vs_ai')
def player_vs_ai():
    return render_template("player_vs_ai.html")

@app.route('/winner2', methods=['POST'])
def ai_vs_homan():
    choices = ["Rock", "Paper", "Scissors"]
    homan = Player("Homan", request.form["homan_choice"])
    sushi = Player("Sushi 2.0", random.choice(choices))
    players = [homan, sushi]
    winner = Game.gameplay(players)
    return render_template("winner2.html", winner=winner)