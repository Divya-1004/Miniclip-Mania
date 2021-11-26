import random 
import time

# Hangman Game

def hangman():
    name = input("What is your name? ") 
    print("Good Luck ! ", name) 
    words = ['rainbow', 'computer', 'science', 'programming','anaconda', 'mathematics', 'player', 'condition','reverse', 'water', 'board', 'cheeks','exam']  

    word = random.choice(words) 
    print("Guess the characters") 
    guesses = '' 
    
    turns = 12
  
    while turns > 0: 
        failed = 0
        for char in word:  
            if char in guesses:  
                print(char) 
            else:  
                print("_") 
                failed += 1
                
        if failed == 0: 
            print("You Win")  
            print("The word is: ", word)  
            break
        guess = input("guess a character:")
        guesses += guess
        
        if guess not in word: 
            turns -= 1
            print("Wrong")
            print("You have", + turns, 'more guesses') 
    
            if turns == 0: 
                print("You Loose")
                print("The word is: ", word) 
                
# Snake and ladder Game

SL = 1
MAX_VAL = 50
snakes = {8: 4,18: 1,26: 10,39: 5,51: 6,54: 36,}
ladders = {3: 20,6: 14,11: 28,15: 34,17: 30,22: 37,}

player_turn_text = ["Your turn.","Go.","Please proceed.","Lets win this.","Are you ready?","",]
snake_bite = ["boohoo","bummer","snake bite","oh no","dang"]
ladder_jump = ["woohoo","woww","nailed it","oh my God...","yaayyy"]

def get_player_names():
    player1_name = None
    while not player1_name:
        player1_name = input("Please enter a valid name for first player: ").strip()

    player2_name = None
    while not player2_name:
        player2_name = input("Please enter a valid name for second player: ").strip()

    print("\nMatch will be played between '" + player1_name + "' and '" + player2_name + "'\n")
    return player1_name, player2_name

def got_snake_bite(old_value, current_value, player_name):
    print("\n" + random.choice(snake_bite).upper() + " ~~~~~~~~>")
    print("\n" + player_name + " got a snake bite. Down from " + str(old_value) + " to " + str(current_value))


def got_ladder_jump(old_value, current_value, player_name):
    print("\n" + random.choice(ladder_jump).upper() + " ########")
    print("\n" + player_name + " climbed the ladder from " + str(old_value) + " to " + str(current_value))


def snake_ladder(player_name, current_value, dice_value):
    time.sleep(SL)
    old_value = current_value
    current_value = current_value + dice_value

    if current_value > MAX_VAL:
        print("You need " + str(MAX_VAL - old_value) + " to win this game. Keep trying.")
        return old_value

    print("\n" + player_name + " moved from " + str(old_value) + " to " + str(current_value))
    if current_value in snakes:
        final_value = snakes.get(current_value)
        got_snake_bite(current_value, final_value, player_name)

    elif current_value in ladders:
        final_value = ladders.get(current_value)
        got_ladder_jump(current_value, final_value, player_name)

    else:
        final_value = current_value

    return final_value


def check_win(player_name, position):
    time.sleep(SL)
    if MAX_VAL == position:
        print("\n\n\nThats it.\n\n" + player_name + " won the game.")
        print("Congratulations " + player_name)
        print("\nThank you for playing the game.")
        return 1
    else:
        return 0

def sal():
    time.sleep(SL)
    player1_name, player2_name = get_player_names()
    time.sleep(SL)

    player1_current_position = 0
    player2_current_position = 0

    while True:
        time.sleep(SL)
        input_1 = input("\n" + player1_name + ": " + random.choice(player_turn_text) + " Hit the enter to roll dice: ")
        print("\nRolling dice...")
        time.sleep(SL)
        dice_value = random.randint(1, 6)
        print("Its a " + str(dice_value))
        time.sleep(SL)
        print(player1_name + " moving....")
        player1_current_position = snake_ladder(player1_name, player1_current_position, dice_value)
        check_win(player1_name, player1_current_position)
        if(check_win(player2_name, player2_current_position)==1):
            break
        input_2 = input("\n" + player2_name + ": " + random.choice(player_turn_text) + " Hit the enter to roll dice: ")
        print("\nRolling dice...")
        dice_value = random.randint(1, 6)
        print("Its a " + str(dice_value))
        time.sleep(SL)
        time.sleep(SL)
        print(player2_name + " moving....")
        player2_current_position = snake_ladder(player2_name, player2_current_position, dice_value)
        check_win(player2_name, player2_current_position)
        if(check_win(player2_name, player2_current_position)==1):
            break

# Tic Tac Toe

theBoard = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)

def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

def tic():

    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(theBoard)
        move=input("It's your turn," + turn + ".Move to which place?")
        
        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.")                
                print(turn + " won!!")               
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.")                
                print(turn + " won!!")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.")                
                print(turn + " won!!")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.")                
                print(turn + " won!!")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.")                
                print(turn + " won!!")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.")                
                print(turn + " won!!")
                break 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.")                
                print(turn + " won!!")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.")                
                print(turn + " won!!")
                break 

        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")
            break

        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'

print("MINICLIP MANIA!!")
x=int(input("Which game do you like to play?\n1. Hangman\n2. Snake and ladder\n3. Tic Tac Toe\nEnter your choice : "))
if(x==1):
    hangman()
elif(x==2):
    sal()
elif(x==3):
    tic()
else:
    print("Enter correct choice")
print("THANK YOU FOR PLAYING!! HAVE A GREAT TIME!!")
