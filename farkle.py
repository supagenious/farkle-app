# choose number of players
# enter player names
# start farkle

# roll all 6 dice
# choose which dice to keep
# choose to roll again or pass
# repeat

# player 2
# choose to use other players dice or roll again
# repeat play steps

# repeat player turns

# repeat turns until player reaches 10,000 pts
import sys
import random
class Player:
    name = 'player'
    number = 0
    score = 0
    number_of_dice = 6
    number_face_up = 1 

class Dice:
    number_up = 1

def roll():
    num = random.randint(1,6)
    return num

def turn(number_of_dice):
    if number_of_dice == 6:
        return roll(),roll(),roll(),roll(),roll(),roll()
    elif number_of_dice == 5:
        return roll(),roll(),roll(),roll(),roll()
    elif number_of_dice == 4:
        return roll(),roll(),roll(),roll()
    elif number_of_dice == 3:
        return roll(),roll(),roll()
    elif number_of_dice == 2:
        return roll(),roll()
    else:
        return roll()
    

def get_players():
    print("Farkle")
    num_of_player = input("Enter the number of players: ")
    print(num_of_player)

    players = []  
    i = 1
    while i <= int(num_of_player):
        name_of_player = input("Enter names of players: ")
        player = Player()
        player.name = name_of_player
        player.number = i
        players.append(player)
        i+=1
    return players  

def main():
    
    players = get_players()
    i = 0
    for p in players:
        dice = turn(p.number_of_dice) 
        print(dice)
        i+=1  
              
# if __name__ == "main":
main()