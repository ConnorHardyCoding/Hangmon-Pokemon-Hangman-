import random


# Function that opes file with parameters depending on a difficulty chosen by user
def opening_files(filename: str, num1: int, num2: int, difficulty_key: str):
    data = []
    with open (filename) as file:
        count = 0
        for line in file:
            line = line.replace("\n", "")
            data.append(line)
            count += 1
            if difficulty_key == "a" and count == num1:
                    return data
            elif difficulty_key == "b" and count == num2:
                    return data
        return data  

# Function that opens a file based on user choice
def pokemon_names_moves_or_both(choice_key: str, difficulty_key: str):
    diction = []

    if choice_key == "a":
        return opening_files("pokemon_names.txt", 388, 727, difficulty_key)
    elif choice_key =="b":
        return opening_files("pokemon_moves.txt", 355, 727, difficulty_key)
    elif choice_key == "c":
        pokenames = opening_files("pokemon_names.txt", 388, 727, difficulty_key)
        pokemoves = opening_files("pokemon_moves.txt", 355, 727, difficulty_key)
        return pokenames + pokemoves
    
def display_hangman(tries):
    stages = [r"""
                --------------
                |            |
                |            |
                |      
                |          
                |         
                |        
                |       
                |        
                |                   
                |                   
                |        
                |        
                |
                |     
                =============
             """,
             r"""
                --------------
                |            |
                |    `;-.    |     ___,
                |      `.`\_...._/`.-"`
                |          
                |         
                |        
                |       
                |        
                |                   
                |                   
                |        
                |        
                |
                |     
                =============
             """,
             r"""
                --------------
                |            |
                |    `;-.    |     ___,
                |      `.`\_...._/`.-"`
                |        \        /      
                |        /()   () \    
                |       |)  .    ()\  
                |       \  -'-     ,;
                |        
                |                   
                |                   
                |        
                |        
                |
                |     
                =============
             """,
             r"""
                --------------
                |            |
                |    `;-.    |     ___,
                |      `.`\_...._/`.-"`
                |        \        /      
                |        /()   () \    
                |       |)  .    ()\  
                |       \  -'-     ,;
                |        ;.__       |  
                |                   |
                |                   |
                |        \    ,     ;
                |        
                |
                |     
                =============
             """,
             r"""
                --------------
                |            |
                |    `;-.    |     ___,
                |      `.`\_...._/`.-"`
                |        \        /      
                |        /()   () \    
                |       |)  .    ()\  
                |       \  -'-     ,;
                |        ;.__       |  
                |       / ,         |
                |      (_/          |
                |        \    ,     ;
                |        
                |
                |     
                =============
             """,
             r"""
                --------------
                |            |
                |    `;-.    |     ___,
                |      `.`\_...._/`.-"`
                |        \        /      
                |        /()   () \    
                |       |)  .    ()\  
                |       \  -'-     ,;
                |        ;.__     ,;|  
                |       / ,    / ,  |
                |      (_/    (_/ ,;|
                |        \    ,     ;   THREE WRONG GUESSES LEFT
                |        
                |
                |     
                =============
             """,
             r"""
                --------------
                |            |
                |    `;-.    |     ___,
                |      `.`\_...._/`.-"`
                |        \        /      
                |        /()   () \    
                |       |)  .    ()\  
                |       \  -'-     ,;
                |        ;.__     ,;|  
                |       / ,    / ,  |
                |      (_/    (_/ ,;|
                |        \    ,     ;   TWO WRONG GUESSES LEFT!
                |         >   \    /
                |        (_,-'
                |     
                =============
             """,
             r"""
                --------------
                |            |
                |    `;-.    |     ___,
                |      `.`\_...._/`.-"`
                |        \        /      
                |        /()   () \    
                |       |)  .    ()\  
                |       \  -'-     ,;
                |        ;.__     ,;|  
                |       / ,    / ,  |
                |      (_/    (_/ ,;|
                |        \    ,     ;   ONE WRONG GUESS LEFT!
                |         >   \    /
                |        (_,-'`> .'
                |             (_,'
                |     
                =============
             """,
             r"""
                --------------
                |            |
                |    `;-.    |     ___,
                |      `.`\_...._/`.-"`
                |        \        /      ,
                |        /()   () \    .' `-._
                |       |)  .    ()\  /   _.'
                |       \  -'-     ,; '. <
                |        ;.__     ,;|   > |
                |       / ,    / ,  |.-'.-'
                |      (_/    (_/ ,;|.<`
                |        \    ,     ;-`
                |         >   \    /
                |        (_,-'`> .'
                |             (_,'
                |     
                =============
             """]
    return stages[tries]
    
def play_again(player_name: str, difficulty_reset: str):
    while True:
        choice = str(input(f"Rotom: Would you like to play again, y or n?\n{player_name}: "))
        if choice.lower() == "n":
            print("Rotom: Maybe next time...")
            return False, difficulty_reset
        elif choice.lower() == "y":
            difficulty_reset_choice = input(f"Rotom: Would you like to reset difficulty or word choice, y or n?\n{player_name}: ")
            if difficulty_reset_choice not in ["y", "n"]:
                difficulty_reset_choice = input(f"Rotom: Invalid. Would you like to reset difficulty or word choice, y or n?\n{player_name}: ")
            elif difficulty_reset_choice == "y":
                difficulty_reset = True
            return True, difficulty_reset
        else:
            print("Rotom: Invalid entry")
    

# Different congratulations to spice things up
grats = ["Congratulations", "Woohoo", "Thats super", "Marvellous", "Alrighty then", "Ohhh boy"]

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Function that searches alphabet for a letter and blanks it out in order to show what letters are left to guess
def search_alphabet(alphabet:str, letter: str):
    newbet = list(alphabet)
    count = 0
    for let in newbet:
        if let == letter:
            newbet[count] = " "
        count += 1
    newbet = "".join(newbet)
    return newbet

def spaced_hangword(hangword: str): # Creates spaced hangman word
    spaced_hang = ""  
    for let in hangword:
        spaced_hang += f"{let} "
    return spaced_hang

def create_hangword_with_dashes(chosen_word: str):
    index_count = 0
    hangword = "-" * len(chosen_word)
    for item in chosen_word:
        if item == " ":
            listhangword = list(hangword)
            listhangword[index_count] = chosen_word[index_count]
            
            hangword = ''.join(listhangword)
        index_count+=1
    return hangword


# Main hangman function may try and streamline into different functions ect.
def main():
    difficulty_reset = False
    while True:
        # Initial statement asking if user wants to play
            
            choice = str(input(f"Rotom: Would you like to play hangmon? y or n?\nUser: "))

            if choice.lower() == "n":
                print("Rotom: Maybe next time...")
                return
            
            # If yes
            elif choice.lower() == "y":
                difficulty_reset_layer = True
                while difficulty_reset_layer: #  Resets to this layer if user resets difficulty
                    
                    if difficulty_reset == False: #  Skips asking a name if user is resetting difficulty
                        player_name = str(input("Rotom: Ok human, what is your preferred name?\nUser: ")).capitalize()  # User name
                    difficulty_reset = False

                    choice_key = str(input(f"Rotom: Would you like to play with pokemon names (enter 'a'), moves (enter 'b') or both (enter 'c')?\n{player_name}: "))  # Choice to play with names, moves, or both
                    while choice_key not in ["a", "b", "c"]:
                            choice_key = input(f"Rotom: Invalid entry. Would you like to play with pokemon names (enter 'a'), moves (enter 'b') or both (enter 'c')?\n{player_name}: ")
                    
                    difficulty_key = str(input(f"Rotom: Which difficulty would you prefer? Enter 'a' for gen 1-3, 'b' for gen 1-6 or 'c' for gen 1-9\n{player_name}: "))  # Difficulty choice of which gens
                    while difficulty_key not in ["a", "b", "c"]:
                        difficulty_key = input(f"Rotom: Invalid entry. Which difficulty would you prefer? Enter 'a' for gen 1-3, 'b' for gen 1-6 or 'c' for gen 1-9\n{player_name}: ")

                    pokemon_dictionary = pokemon_names_moves_or_both(choice_key, difficulty_key) #  Sets the list of words

                    reset_word_layer = True
                    while reset_word_layer:
                        if difficulty_reset == True:
                            break
                        chosen_word = random.choice(pokemon_dictionary).upper()  #  Sets/resets word
                        hangword = create_hangword_with_dashes(chosen_word)  # Sets/resets hangman word
                        #print(chosen_word) # Testing purposes
                        al = alphabet #  Sets/resets alphabet
                        here_is_your_word = True
                        saved_alphabet_list = [] #  Saves letters already searched
                        tries = 0
                        max_tries = False
                        game_end = False

                        game_layer = True
                        while game_layer:
                            spaced_hang = spaced_hangword(hangword)

                            # When the game begins says here is your word, then sets to false
                            if here_is_your_word == True:
                                print(f"Rotom: Here is your word:\n{display_hangman(tries)}\n{spaced_hang}\nRotom: Please guess a letter. Letters left: {al}")
                            else:
                                print(f"{display_hangman(tries)}\n{spaced_hang}\nRotom: Please guess a letter. Letters left: {al}")
                            here_is_your_word = False

                            letter = str(input(f"{player_name}: ")) #  User enters letter
                            letter = letter.upper()

                            valid_letter = True  # While loop to check if valid letter
                            while valid_letter:
                                if letter in saved_alphabet_list:
                                    print("Rotom: You have already searched that letter")
                                    letter = str(input(f"{player_name}: "))
                                    letter = letter.upper()
                                elif letter.isalpha() and len(letter) < 2:
                                    break
                                else:
                                    print("Rotom: That is not a valid letter please try another")
                                    letter = str(input(f"{player_name}: "))
                                    letter = letter.upper()
                                
                            saved_alphabet_list.append(letter) #  Saves entered letter to a list
                            al = search_alphabet(al, letter)
                            
                            index_count = 0
                            letter_count = 0
                            Success = False

                            # scans entered letter in word
                            for item in chosen_word:
                                if item == letter:
                                    Success = True
                                    listhangword = list(hangword)
                                    listhangword[index_count] = chosen_word[index_count]
                                    
                                    hangword = ''.join(listhangword)
                                    letter_count += 1
                                index_count+=1

                            if Success:  # If letter found in word
                                print(f"Rotom: {random.choice(grats)}, amount of {letter}'s in the word: {letter_count}")
                            else:
                            
                                tries += 1
                                if tries == 8:
                                    max_tries = True

                            if hangword == chosen_word: #  If word completed
                                spaced_hang = spaced_hangword(hangword)
                                print("Rotom: You win, no pokemon were harmed :)\nRotom: Here is the word: \n      ", chosen_word)
                                game_end = True
                                
                            elif max_tries: # If to many guesses, failure
                                print(display_hangman(tries))
                                print("Rotom: You lose, noooo pika noooo\nRotom: Here is the word: \n      ", chosen_word)
                                game_end = True
                            
                            if game_end:
                                play_again_choice, difficulty_reset = play_again(player_name, difficulty_reset)
                                
                                if not play_again_choice:
                                    return
                                break

                            
            else:
                print("Rotom: I'm sorry, I didn't catch that. Please enter 'y' or 'n'.")      



main()
