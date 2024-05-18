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

#Checks whether player has any attemps left
def attempts_check():
    global mistakes
    global selected_word

    if mistakes >= 0:
        return player_guess()                  #If you use return player_guess(), the player_guess() function will be called again recursively, and the result of this recursive call will be returned to the caller of the current player_guess() invocation. This means that the program execution will proceed based on the result of the recursive call; while only writing player_guess(), the result will not be returned to the caller of the current player_guess() invocation. Instead, the program execution will continue with the next line of code after the if statement.
    elif mistakes < 0:
        print(selected_word)
        print()
        print("GAME OVER.")

        running = False
        return running

#Main function for game loop
def player_guess():
    global mistakes                                                               #To use a global variable in a function, first declare it as global, then modify the value; you can't write global mistakes -= 1
    global selected_word
    global guessed_letter

    #Player input
    guessed_letter = input("Guess a letter. ").upper()

    #Checks if the input is a single letter
    if len(guessed_letter) != 1 or not guessed_letter.isalpha():                  #The isalpha() method returns True if all characters in the string are alphabetic (letters from 'a' to 'z' or 'A' to 'Z'). If guessed_letter contains any non-alphabetic character (such as digits, punctuation, or whitespace), guessed_letter.isalpha() will return False. The not keyword negates this result, so the condition becomes True if there are any non-alphabetic characters in guessed_letter.
        print("You can only input a single letter.") 
        return player_guess()

    #Checks if the letter guessed is contained in the selected word
    if guessed_letter in selected_word:
        for i in range (len(selected_word)):
            #If the selected letter is correct
            if selected_word[i] == guessed_letter:
                underscores[i] = guessed_letter

        print("Correct!\n")
        print("".join(underscores))
                
        #Checks if there is still any letter to guess
        if "_" in underscores:                                            #"in" is not only used in for loops for iterating elements, but also for checking membership in a sequence
            return attempts_check()
                
        #If all the letters have been guessed, player wins
        elif "_" not in underscores:                                       #"not in" is the opposite of "in"
            print("".join(underscores))
            print()
            print("YOU WIN!")
            return False
        
    #If player guesses a wrong letter
    elif guessed_letter not in selected_word:                                                    
        mistakes -= 1
        print("Nope!\n")
        print("You now have " + str(mistakes) + " attempts left.")

        return attempts_check()


running = True
while running:
    #A random word from the list is picked
    selected_word = random.choice(words_list)
    underscores = ["_"] * len(selected_word)
    print("".join(underscores))

    #Game loop begins
    running = player_guess()                                      #the line means that the player_guess() function is called, and the result of that function call (either True or False , or None which is still False )is stored in the variable running

    if running == False:
        print("Thank you for playing.")