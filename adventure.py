#adventure text based game

def position_0(user_char):
    print ("<---<---<---<---")
    print("\t\t^")
    print("\t\t|")
    print("\t\t|")
    print ("X--->--->")
    print("\t|\t^")
    print("\t|\t|")
    print("\tv\t|")
    print("\t|\t^")
    print("\t|\t|")
    print("\tv\t|")
    print("\t--->--->")

def position_1(user_char):
    print ("<---<---<---<---")
    print("\t\t^")
    print("\t\t|")
    print("\t\t|")
    print ("--->--->M")
    print("\t|\t^")
    print("\t|\t|")
    print("\tv\t|")
    print("\t|\t^")
    print("\t|\t|")
    print("\tv\t|")
    print("\t--->--->")

def get_char():
    user_char = raw_input("Pick a single char to use as your player.\neg. 'A','$','*', etc\npick: ")

    if len(user_char)>1:
        get_char()
    else:
        return user_char


# --CODE STARTS HEREEEE-- --CODE STARTS HEREEEE-- --CODE STARTS HEREEEE-- --CODE STARTS HEREEEE-- --CODE STARTS HEREEEE--
print("\n----- Heyyy, welcome to the Oppong Adventure Game -----\n")
print("----- The objective of this game is to go through the maze looking for something -----\n")

# GETS USER CHAR FOR THE MAP
get_char() 

#print "\nThis will be your char through the game: ",get_char(), "\n"








