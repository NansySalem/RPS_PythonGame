import random
'''
Done by: Nansy Salem

rock rock   paper paper  scissors scissors
rock paper  paper rock
rock scissors scissors rock
paper scissors scissors paper

listing all possible combinations
'''
#tuple used as a reference to what user enters
my_game = ('rock', 'paper', 'scissors')
r = "rock"
p = "paper"
s = "scissors"
#defining a multi-dimensional array to capture all possible combinations and corresponding outcome
#column 0 user choice
#column 1 computer choice
#column 2 result
#each row represents a possible combination of user choices and it's results
#selections = [['rock','rock', "That's a tie"],['paper','paper',"That's a tie"],['scissors','scissors',"That's a tie"], ['rock','paper','You lose!'], ['rock','scissors','You win!'],['paper','rock', 'You win!' ],['paper','scissors','You lose!'],['scissors','rock','You lose!'],['scissors','paper','You win!' ]]

# flag for user to end game whenever he likes
play_again = True 

# reference to user choice when asked if he likes to play again
play_choices = ("yes", "Yes", "y")

c_score =0 # capturing overall computer score
u_score = 0 # capturing overall user score
games = 0 #for interations




'''After finishing the first round, this function checks with the user if he would like to continue playing, if yes, it resets scores'''
def continue_playing():
    play_choice = input("\nDo you like to start a new game? Yes or No\n")
    if play_choice in play_choices:
        return True
    else:
        return False
    
'''This function checks user and computer choices versus the game and updates scores accordingly'''
def start_game(game_rounds):
    games = 0
    global c_score
    global u_score
    while games < game_rounds : #playing the number of rounds specified by the user
        uchoice = input("Enter your choice: Rock, Paper or Scissors\n")
        uchoice = uchoice.lower()
        cchoice = random.choice(my_game)
        print("You choose:", uchoice ) #printing user and computer choices
        print("Computer choose:", cchoice)
        if uchoice == cchoice:
            print("It's a tie")
        elif (uchoice == r and cchoice == p) or (uchoice == p and cchoice == s ) or (uchoice == s and cchoice == r):
            print("You lose")
            c_score +=1
        else:
            print("You win")
            u_score+=1
        print("Your score:", u_score)
        print("Computer score:", c_score)
        if who_wins():
            break
        games+=1; 

def game_rounds_num():
    while True:
        game_rounds = input("How many games you like to play?\n")
        if game_rounds.isnumeric(): # validation to make sure number entered is numeric
            game_rounds = int(game_rounds)
            if game_rounds%2 == 0:
                print("Ideally, you should enter an ODD number for the games you want to play\n")
                continue
            else:
                break
    return game_rounds

def who_wins():
    global u_score
    global c_score
    global game_rounds
    if u_score > game_rounds//2:
        print("You win and your final score is", u_score, "vs computer score", c_score)
        return True
    if c_score > game_rounds//2:
        print("You lose and your final score is", u_score, "vs computer score", c_score)
        return True
    return False


while play_again:
    game_rounds = game_rounds_num()
    start_game(game_rounds)
    if u_score == c_score:
        print("Meh, that was a tie")
    play_again = continue_playing()
    u_score = c_score = game_rounds = 0

print("Thanks for trying our game!")


