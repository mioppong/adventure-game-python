#adventure text based game
def bad_move():
    print ("\nLOL that seems like a bad move\n")

def clear_terminal():
    print(chr(27) + "[2J")

def press_to_continue():
    input ("\npress enter to continue...")

def position_0(user_char):
    print ("<---<---<---<---")
    print ("\t\t^")
    print ("\t\t|")
    print ("\t\t|")
    print (user_char,"-->--->")
    print ("\t|\t^")
    print ("\t|\t|")
    print ("\tv\t|")
    print ("\t|\t^")
    print ("\t|\t|")
    print ("\tv\t|")
    print ("\t--->--->")

def position_1(user_char):
    print ("<---<---<---<---")
    print ("\t\t^")
    print ("\t\t|")
    print ("\t\t|")
    print ("--->-->",user_char)
    print ("\t|\t^")
    print ("\t|\t|")
    print ("\tv\t|")
    print ("\t|\t^")
    print ("\t|\t|")
    print ("\tv\t|")
    print ("\t--->--->")

def position_2(user_char):
    print ("<---<---<---<---")
    print ("\t\t^")
    print ("\t\t|")
    print ("\t\t|")
    print ("--->-->")
    print ("\t|\t^")
    print ("\t|\t|")
    print ("\tv\t|")
    print ("\t|\t^")
    print ("\t|\t|")
    print ("\tv\t|")
    print ("\t",user_char)
    print ("\t--->--->")

def position_3(user_char):
    print ("<---<---<---<---")
    print ("\t\t^")
    print ("\t\t|")
    print ("\t\t|")
    print ("--->-->")
    print ("\t|\t^")
    print ("\t|\t|")
    print ("\tv\t|")
    print ("\t|\t^")
    print ("\t|\t|")
    print ("\tv\t|")
    print ("\t--->--->", user_char)

def position_4(user_char):
    print ("<---<---<---<---")
    print ("\t\t^")
    print ("\t\t|")
    print ("\t\t|")
    print ("--->-->\t\t",user_char)
    print ("\t|\t^")
    print ("\t|\t|")
    print ("\tv\t|")
    print ("\t|\t^")
    print ("\t|\t|")
    print ("\tv\t|")
    print ("\t--->--->")

def position_5(user_char):
    print ("<---<--<---<---", user_char)
    print ("\t\t^")
    print ("\t\t|")
    print ("\t\t|")
    print ("--->-->")
    print ("\t|\t^")
    print ("\t|\t|")
    print ("\tv\t|")
    print ("\t|\t^")
    print ("\t|\t|")
    print ("\tv\t|")
    print ("\t--->--->")

def position_6(user_char):
    print ("<--<---",user_char,"<---<--")
    print ("\t\t^")
    print ("\t\t|")
    print ("\t\t|")
    print ("--->-->")
    print ("\t|\t^")
    print ("\t|\t|")
    print ("\tv\t|")
    print ("\t|\t^")
    print ("\t|\t|")
    print ("\tv\t|")
    print ("\t--->--->")

def position_7(user_char):
    print (user_char,"<---<---<---<---")
    print ("\t\t^")
    print ("\t\t|")
    print ("\t\t|")
    print ("--->-->")
    print ("\t|\t^")
    print ("\t|\t|")
    print ("\tv\t|")
    print ("\t|\t^")
    print ("\t|\t|")
    print ("\tv\t|")
    print ("\t--->--->")

def get_char(): #get user player
    user_char = input("Pick a single char to use as your player.\neg. 'A','$','*', etc\npick: ")

    if len(user_char)!= 1 :
        get_char()
    else:
        return user_char

def start_game():
    user_ready = input("are you ready to start now?, Y, N: ")
    if (user_ready == 'Y'):
        return 1 #game can now begin
    else:
       return start_game()

def possible_moves():
    print("\POSSIBLE MOVES ***IMPORTANT***:\nU for up\nD for down\nL for left\nR for right")

def move_up_one_level(current_level):
    return (current_level+1)

def get_move_from_user():
    return input("choice: ")
 
def story_given_the_level(level_youre_on):
    if level_youre_on == 1:
         print ("You enter the maze looking for your lover")
    if level_youre_on == 2:
         print ("You keep looking because you can feel their presence")
    if level_youre_on == 3:
         print ("You meet an old lady on the way and help her with groceries")
    if level_youre_on == 4:
         print ("She directs you to go in a specific direction")
    if level_youre_on == 5:
         print ("Because you helped the old lady, you gain super powers to help look for your lover")
    if level_youre_on == 6:
         print ("You find a tunnel and are hesitant to go in, but you go in because you are in love with the thought of being in love")
    if level_youre_on == 7:
         print ("You exit the tunnel and realize everything you have been looking for has been right beside you the whole time")
# --CODE STARTS HEREEEE-- --CODE STARTS HEREEEE-- --CODE STARTS HEREEEE-- --CODE STARTS HEREEEE-- --CODE STARTS HEREEEE--
clear_terminal()

print("\n----- YEEOOO, welcome to the Oppong Adventure Game -----\n")
print("----- Go through the maze looking for and just have fun -----\n")

press_to_continue()
clear_terminal()
user_char = get_char() # GETS USER CHAR FOR THE MAP
clear_terminal()
keep_playing = 'Y'
game_has_begun = True

current_level = 0 #keep track on user position
if (start_game() == 1 and current_level == 0):
    clear_terminal()
    possible_moves()

while True:

    if game_has_begun is True:
        position_0 (user_char)        
        game_has_begun = False
        
    users_move = get_move_from_user()
    
    if users_move == 'R' and current_level == 0:
        clear_terminal()
        possible_moves()
        current_level = current_level + 1
        position_1(user_char)
        story_given_the_level(current_level)
    elif users_move == 'D' and current_level == 1:
        clear_terminal()
        possible_moves()
        current_level = current_level + 1        
        position_2(user_char)
        story_given_the_level(current_level)
    elif users_move == 'R' and current_level ==2:
        clear_terminal()
        possible_moves()
        current_level = current_level + 1
        position_3(user_char)
        story_given_the_level(current_level)
    elif users_move == 'U' and current_level == 3:
        clear_terminal()
        possible_moves()
        current_level = current_level +1
        position_4(user_char)
        story_given_the_level(current_level)
    elif users_move == 'U' and current_level == 4:
        clear_terminal()
        possible_moves()
        current_level = current_level + 1
        position_5(user_char)
        story_given_the_level(current_level)
    elif  users_move == 'L' and current_level == 5:
        clear_terminal()
        possible_moves()
        current_level = current_level + 1
        position_6(user_char)
        story_given_the_level(current_level)
    elif users_move == 'L' and current_level == 6:
        clear_terminal()
        possible_moves()
        current_level = current_level + 1
        position_7(user_char)
        story_given_the_level(current_level)
        keep_playing  = input("Do you want to keep playing or naa? Y, or another other char to quit: ")
        
        if keep_playing is 'Y':
            current_level = 0
            clear_terminal()
            game_has_begun = True
        else:
            print("AHHH You cool for Playing and have a blessed Day")
            break
    
    else:
        bad_move()
       