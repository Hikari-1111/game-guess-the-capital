#Guess the capital game_NEW

import random

#Introduction
print("Ready to test your knowledge of the world capitals?\n")
print("Guess each capital word by word, but be careful: you can only make 5 mistakes.\n")
print("Good luck!\n")
input("PRESS ENTER TO CONTINUE.")

words_list = [
    "BISHKEK", "SUVA", "TASHKENT", "MINSK", "LILONGWE", "PARAMARIBO", "TBILISI", "ISTANBUL", "ATHENS",
    "WINDHOEK", "REYKJAVIK", "BANJUL", "OUAGADOUGOU", "DUSHANBE", "APIA", "MALABO", "MADRID", "BANGKOK",
    "MAPUTO", "ANTANANARIVO", "THIMPHU", "ASHGABAT", "MONTEVIDEO", "QUITO", "PODGORICA", "CHISINAU", "VILNIUS"
    ]

#Sets the number of mistakes to be max 5
mistakes = 5
running = True

#Checks whether player has any attemps left
def attempts_check():
    global mistakes
    global selected_word

    if mistakes >= 0:
        return player_guess()          
    elif mistakes < 0:
        print(selected_word)
        print()
        print("GAME OVER.\n")

        running = False
        return running

#Main function for game loop
def player_guess():
    global mistakes                                                      
    global guessed_letter

    #Player input
    print("".join(underscores))
    print()
    guessed_letter = input("Guess a letter.\n ").upper()

    #Checks if the input is a single letter
    if len(guessed_letter) != 1 or not guessed_letter.isalpha():              
        return player_guess()

    #Checks if the letter guessed is contained in the selected word
    if guessed_letter in selected_word:
        for i in range (len(selected_word)):
            #If the selected letter is correct
            if selected_word[i] == guessed_letter:
                underscores[i] = guessed_letter

        print("Correct!\n")
                
        #Checks if there is still any letter to guess
        if "_" in underscores:                                         
            return attempts_check()
                
        #If all the letters have been guessed, player wins
        elif "_" not in underscores:                                
            print("".join(underscores))
            print()
            print("YOU WIN!\n")
            return False
        
    #If player guesses a wrong letter
    elif guessed_letter not in selected_word:                                                    
        mistakes -= 1

        if mistakes > 0:
            print("Nope!\n")
            print("You now have " + str(mistakes) + " attempts left.\n")
        elif mistakes == 0:
            print("You have no attempts left!\n")

        return attempts_check()

#Checks if player wants to play again
def play_again():
    global running
    global mistakes
    replay = input("Would you like to play again? [Y/N]  ").upper()

    #If yes, game loop starts again
    if replay == "Y":
        mistakes = 5
        running = True
    elif replay == "N":
        print("Until next time!")

while running:
    #A random word from the list is picked
    selected_word = random.choice(words_list)
    underscores = ["_"] * len(selected_word)

    #Game loop begins
    running = player_guess()                                    

    if running == False:
        print("Thank you for playing.\n")
        play_again()
