#adventure text based game

def clear_terminal():
    print(chr(27) + "[2J")

def press_to_continue():
    raw_input("\npress enter to continue...")

def position_0(user_char):
    clear_terminal()
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
    clear_terminal()
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

def get_char():
    user_char = raw_input("Pick a single char to use as your player.\neg. 'A','$','*', etc\npick: ")

    if len(user_char)!= 1 :
        get_char()
    else:
        return user_char

def start_game():
    user_ready = raw_input("are you ready to start now?, Y, N:")
    if (user_ready == 'Y'):
        return 1 #game can now begin
    else:
       return start_game()

def possible_moves():
    print("\npossible moves:\nU for up\nD for down\nL for left\nR for right")

# --CODE STARTS HEREEEE-- --CODE STARTS HEREEEE-- --CODE STARTS HEREEEE-- --CODE STARTS HEREEEE-- --CODE STARTS HEREEEE--
print("\n----- Heyyy, welcome to the Oppong Adventure Game -----\n")
print("-----Go through the maze looking for and just have fun -----\n")

press_to_continue()
clear_terminal()
user_char = get_char() # GETS USER CHAR FOR THE MAP
clear_terminal()

move_made = ""

if (start_game() == 1):
    position_0 (user_char)
    possible_moves()
    move_made = raw_input("choice: ")

    if move_made is 'U' :
        print "Gang shit"



    









