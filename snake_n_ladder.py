import random
import sys

#setup number of players
no_of_players = 0
while not int(no_of_players) in range(1,5):
    no_of_players = int(input("Enter number of players (1 - 4) : "))

#setup number of dice
no_of_dice = 0
while not int(no_of_dice) in range(1,3):
    no_of_dice = int(input("Enter number of dice (1 - 2) : "))

#setup snakes and ladders in one set
snakes_n_ladders = {
    4: 14,
    9: 31,
    17: 7,
    20: 38,
    28: 84,
    40: 59,
    51: 67,
    54: 34,
    62: 19,
    63: 81,
    64: 60,
    71: 91,
    87: 24,
    93: 73,
    95: 75,
    99: 78
}
#roll again if player gets 6 on any one die
RollAgain = True

#output player movements 
def turn(player_name, square):
    while True:        
        roll_dice = input("Player {0}, it's your turn. Press enter to roll your dice.".format(player_name))
        roll1 = random.randint(1,6)
        if no_of_dice == 2 :
            roll2 = random.randint(1,6)
            roll = roll1 + roll2 
            print("Player {0} gets a {2}. It's a {3} on dice1 & {4} on dice2.".format(player_name, square, roll, roll1, roll2))
        else:
            roll2 = 0
            roll = roll1 + roll2 
            print("Player {0} gets a {2}.".format(player_name, square, roll))
        
                
        if square + roll > 100:
            print("Player {0} can't move so stays on square {1}.".format(player_name, square))
        else:
            square += roll
            print("Player {2} moves to square {0} from square {1}.".format(square,square-roll,player_name))
            if square == 100:
                return 100
            next = snakes_n_ladders.get(square, square)
            if square < next:
                print("Player {1} lands on a ladder. And thus climbs up to {0}.".format(next,player_name))
                if square == 100:
                    return 100
                square = next
            elif square > next:
                print("Player {1} gets bitten by a snake. And thus now slithers down to {0}.".format(next,player_name))
                square = next
        if roll1 == 6 or roll2 == 6 or not RollAgain:
            print("Its a sixer. Roll again.")
        else:    
            return square
    
#setup game play, player_names, final winner       
def game_play():
    players = []
    player_names = []
    for i in range(0, no_of_players):
        ele = 1
        players.append(ele)
        player_names.append(input('Enter player ' + str(i + 1) + ' name: '))
           
    while True:
        for i in range(0, no_of_players):
            next_square = turn(player_names[i], players[i])
            if next_square == 100:
                print("Congratulations player " + player_names[i] + "!!. You are the winner!")
                return
            players[i] = next_square
            print()

game_play()
