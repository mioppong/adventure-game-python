#adventure text based game
#adventure text based game
def bad_move():
    print "\nLOL that seems like a bad move\n"

def clear_terminal():
    print(chr(27) + "[2J")

def press_to_continue():
    raw_input("\npress enter to continue...")

def position_0(user_char):
    print "<---<---<---<---"
    print "\t\t^"
    print "\t\t|"
    print "\t\t|"
    print user_char,"-->--->"
    print "\t|\t^"
    print "\t|\t|"
    print "\tv\t|"
    print "\t|\t^"
    print "\t|\t|"
    print "\tv\t|"
    print "\t--->--->"

def position_1(user_char):
    print "<---<---<---<---"
    print "\t\t^"
    print "\t\t|"
    print "\t\t|"
    print "--->-->",user_char
    print "\t|\t^"
    print "\t|\t|"
    print "\tv\t|"
    print "\t|\t^"
    print "\t|\t|"
    print "\tv\t|"
    print "\t--->--->"

def position_2(user_char):
    print "<---<---<---<---"
    print "\t\t^"
    print "\t\t|"
    print "\t\t|"
    print "--->-->"
    print "\t|\t^"
    print "\t|\t|"
    print "\tv\t|"
    print "\t|\t^"
    print "\t|\t|"
    print "\tv\t|"
    print "\t",user_char
    print "\t--->--->"

def position_3(user_char):
    print "<---<---<---<---"
    print "\t\t^"
    print "\t\t|"
    print "\t\t|"
    print "--->-->"
    print "\t|\t^"
    print "\t|\t|"
    print "\tv\t|"
    print "\t|\t^"
    print "\t|\t|"
    print "\tv\t|"
    print "\t--->--->", user_char

def position_4(user_char):
    print "<---<---<---<---"
    print "\t\t^"
    print "\t\t|"
    print "\t\t|"
    print "--->-->\t\t",user_char
    print "\t|\t^"
    print "\t|\t|"
    print "\tv\t|"
    print "\t|\t^"
    print "\t|\t|"
    print "\tv\t|"
    print "\t--->--->"
def position_5(user_char):
    print "<---<--<---<---", user_char
    print "\t\t^"
    print "\t\t|"
    print "\t\t|"
    print "--->-->"
    print "\t|\t^"
    print "\t|\t|"
    print "\tv\t|"
    print "\t|\t^"
    print "\t|\t|"
    print "\tv\t|"
    print "\t--->--->"
def position_6(user_char):
    print "<--<---",user_char,"<---<--"
    print "\t\t^"
    print "\t\t|"
    print "\t\t|"
    print "--->-->"
    print "\t|\t^"
    print "\t|\t|"
    print "\tv\t|"
    print "\t|\t^"
    print "\t|\t|"
    print "\tv\t|"
    print "\t--->--->"
def position_7(user_char):
    print user_char,"<---<---<---<---"
    print "\t\t^"
    print "\t\t|"
    print "\t\t|"
    print "--->-->"
    print "\t|\t^"
    print "\t|\t|"
    print "\tv\t|"
    print "\t|\t^"
    print "\t|\t|"
    print "\tv\t|"
    print "\t--->--->"

def get_char(): #get user player
    user_char = raw_input("Pick a single char to use as your player.\neg. 'A','$','*', etc\npick: ")

    if len(user_char)!= 1 :
        get_char()
    else:
        return user_char

def start_game():
    user_ready = raw_input("are you ready to start now?, Y, N: ")
    if (user_ready == 'Y'):
        return 1 #game can now begin
    else:
       return start_game()

def possible_moves():
    print("\npossible moves:\nU for up\nD for down\nL for left\nR for right")

def move_up_one_level(current_level):
    return (current_level+1)

def get_move_from_user():
    return raw_input("choice: ")
 
# --CODE STARTS HEREEEE-- --CODE STARTS HEREEEE-- --CODE STARTS HEREEEE-- --CODE STARTS HEREEEE-- --CODE STARTS HEREEEE--
clear_terminal()

print("\n----- Heyyy, welcome to the Oppong Adventure Game -----\n")
print("-----Go through the maze looking for and just have fun -----\n")

press_to_continue()
clear_terminal()
user_char = get_char() # GETS USER CHAR FOR THE MAP
clear_terminal()

current_level = 0 #keep track on user position

if (start_game() == 1 and current_level == 0):
    possible_moves()
    position_0 (user_char)
    
    keep_playing = True
    
while True:

    if get_move_from_user() == 'R' and current_level == 0:
        current_level = current_level + 1
        position_1(user_char)
    if get_move_from_user() == 'D' and current_level == 1:
        current_level = current_level + 1        
        position_2(user_char)
    if get_move_from_user() == 'R' and current_level ==2:
        current_level = current_level + 1
        position_3(user_char)
    if get_move_from_user() == 'U' and current_level == 3:
        current_level = current_level +1
        position_4(user_char)
    if get_move_from_user() == 'U' and current_level == 4:
        current_level = current_level + 1
        position_5(user_char)
    


        



    





