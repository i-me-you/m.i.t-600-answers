# Problem Set 2, hangman.py
# Name: akujobi clinton c
# Collaborators: none yet
# Time spent: dunno buh i finished 7:52 am 13th january 2018

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    
    return True
    #pass



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_word = ''
    
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word = guessed_word + letter
        else:
            guessed_word = guessed_word + '_ '
    
    return guessed_word
    #pass



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alphabet = string.ascii_lowercase
    alphaList = list(alphabet)
    
    for letter in letters_guessed:
        if letter in alphaList:
            alphaList.remove(letter)
    
    newAlpha = ''.join(alphaList)
    return newAlpha
    #pass



def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    num_guesses = 6
    num_warning = 3

    
    #START
    print ('Welcome to the game of hangman')
    
    #COME UP WITH SECRET WORD      
    
    print ('------------------------')
    
    #SHOW BOARD AND BLANKS TO THE PLAYER
    
    print ('I am thinking of a word that is',len(secret_word),'letters long')
    print ('You have ',num_warning,'warnings left')
    print ('You have',num_guesses,'guesses left')
    print ('Available letters: ', string.ascii_lowercase)
    
    #ASK PLAYER TO GUESS A LETTER
    letters_guessed = []
    while num_guesses > 0:
        
        #loop break condition
        LoopBreak = is_word_guessed(secret_word, letters_guessed)
        if LoopBreak is True:
            break
        
        print ('-----------------------------------')
        userInput = input('Please enter a letter:')
        
        #MAKING SURE THE USER INPUTS A "SINGLE ALPHABET" 
            
        if userInput.isalpha():      
            if len(userInput) == 1:
                userInput = str(userInput)          
                userInput = userInput.lower()          
            elif len(userInput) != 1 and num_warning > 0:    
                num_warning -= 1
                print ('Please input "1" letter')
                print ('You have ',num_warning,'warnings left')
                if len(userInput) != 1 and num_warning < 1:
                    num_guesses -= 1
                    print ('You now have',num_guesses, ' guesses left')
                
        elif (not userInput.isalpha()) and (num_warning > 0):
            num_warning -= 1
            print('That\'s not a valid letter, you have',num_warning,'warnings left:')
        
        elif (not userInput.alpha()) and (num_warning <= 0):
            num_guesses -= 1
            print ('You now have ',num_guesses, 'guesses left')

        def CheckingNatureOf_userInput(userInput):        
            '''
            userInput : (str) letter the user guesses
            Boolean............
            If user input is a "Single alphabet" returns true else false'''
            
            if userInput.isalpha() and len(userInput) == 1:
                return True
            else:
                return False

    
    
        #ADDING THE CORRECT USER INPUT TO LETTERS GUESSSED LIST
        
        letters_guessed == []
        UserInputChk = CheckingNatureOf_userInput(userInput)

        
        if UserInputChk is True:
            if userInput in letters_guessed:
                    num_guesses -= 1
                    print ('You have already picked that letter')
                    print ('You now have',num_guesses,'guesses left')
                    
            elif userInput not in letters_guessed:
                letters_guessed == letters_guessed.append(userInput)
        
        Available_letters = get_available_letters(letters_guessed)
        Guessed_word = get_guessed_word(secret_word, letters_guessed) 
        
        #CHECKING WHETHER THE INPUT IS IN THE SECRET WORD
        


        def CheckingInputIn_Secretword(userInput):
            '''
            userInput : (str) letter the user guesses
            Boolean .....
            Returns True if userInput is in secret word else False'''
            while UserInputChk is True:
                if userInput in secret_word:
                    return True
                else:
                    return False
        
        CheckInputIn_SecretWord = CheckingInputIn_Secretword(userInput)
        
        if UserInputChk :
            if CheckInputIn_SecretWord :   # is True  :
                print ('Good guess:', Guessed_word)
                print ('Available letters:', Available_letters )
                print ('----------------------------------')
            elif (not CheckInputIn_SecretWord) and (num_guesses > 0):
                num_guesses -= 1
                print ('Oops, That letter is not in the secret word')
                print ('You now have ',num_guesses,'guesses left')
                print ('Guess: ',Guessed_word)
            elif (not CheckInputIn_SecretWord) and (num_guesses <=0):
                print ('Failed')
                break

    def check_score(num_guesses,secret_word):
        '''
        num_guesses : number of remaining guesses the user has (str)
        secret_word : the word the user is guessing (int)
        Calculates the player's total score and returns the value,
        total = guesses remaining * total of unique characters in secret_word'''
        
        unique = []
        for char in secret_word:
            if char not in unique:
                unique.append(char)
        total = num_guesses * len(unique)
        return total
    
    score = check_score(num_guesses,secret_word)
    
    if num_guesses == 0:
        print ('You have run out of guesses and have lost the game!!!')
        print ('You shall be hanged!!!!..... The word was:',secret_word)
    if LoopBreak:
        print ('Congratulations you have won the game')
        print ('You guessed the secret word: ',secret_word)
        print ('Your score is: ',score)
    



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.split()         
    my_word = ''.join(my_word)            ## Removing the spaces in my_word
    
    BooleanStore =[]
    
    if len(my_word) == len(other_word):
        for x,y in zip(my_word,other_word):
            if x == y:
                BooleanStore.append(True)
            elif x == '_':
                BooleanStore.append(True)
            elif x != y:
                BooleanStore.append(False)
    elif len(my_word) != len(other_word):
        return False
    if False in BooleanStore:
        return False
    else:
        return True
        
    #pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.split()         
    my_word = ''.join(my_word)            ## Removing the spaces in my_word
    
    #check whether my_word matches any other word in wordlist and print it out
    #wordlist = list of words the computer chooses from
    MatchWords = []
    for word in wordlist:
        if match_with_gaps(my_word,word):
            MatchWords == MatchWords.append(word)                 #not appending
    
    if len(MatchWords) == 0:
        print ('No possible matches')
        print (MatchWords)
    elif len(MatchWords) > 0:
        MatchWords = ', '.join(MatchWords)
        print (MatchWords)
    
    #pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    num_guesses = 6
    num_warning = 3
#    letters_guessed = []   #**hmmm
    
    #START
    print ('Welcome to the game of hangman')
    
    #COME UP WITH SECRET WORD      
    
    print ('------------------------')
    
    #SHOW BOARD AND BLANKS TO THE PLAYER
    
    print ('I am thinking of a word that is',len(secret_word),'letters long')
    print ('You have ',num_warning,'warnings left')
    print ('You have',num_guesses,'guesses left')
    print ('Available letters: ', string.ascii_lowercase)
    print ('Hint:::::::Press "*" at any time in the game to see possible matches of secret word')
    
    #ASK PLAYER TO GUESS A LETTER
    letters_guessed = []
    while num_guesses > 0:
        
        #loop break condition
        LoopBreak = is_word_guessed(secret_word, letters_guessed)
        if LoopBreak is True:
            break
        
        print ('-----------------------------------')
        userInput = input('Please enter a letter:')
        
        Guessed_word = get_guessed_word(secret_word, letters_guessed)
        my_word = Guessed_word
        #MAKING SURE THE USER INPUTS A "SINGLE ALPHABET" 
        # if the user inputs '*' show possible matches
        
        if userInput.isalpha():      
            if len(userInput) == 1:
                userInput = str(userInput)          
                userInput = userInput.lower()          
            elif len(userInput) != 1 and num_warning > 0:    
                num_warning -= 1
                print ('Please input "1" letter')
                print ('You have ',num_warning,'warnings left')
                if len(userInput) != 1 and num_warning < 1:
                    num_guesses -= 1
                    print ('You now have',num_guesses, ' guesses left')
        
        #showing user the possible guesses if input is '*'
        
        elif (not userInput.isalpha() and (userInput == '*')):
            print (show_possible_matches(my_word))
        
        elif (not userInput.isalpha()) and (num_warning > 0) and (userInput != '*'):
            num_warning -= 1
            print('That\'s not a valid letter, you have',num_warning,'warnings left:')
        
        elif (not userInput.alpha()) and (num_warning <= 0)  and (userInput != '*'):
            num_guesses -= 1
            print ('You now have ',num_guesses, 'guesses left')
        

        
        def CheckingNatureOf_userInput(userInput):        
            '''
            userInput : (str) letter the user guesses
            Boolean............
            If user input is a "Single alphabet" returns true else false'''
            
            if userInput.isalpha() and len(userInput) == 1:
                return True
            else:
                return False

    
    
        #ADDING THE CORRECT USER INPUT TO LETTERS GUESSSED LIST
        
        letters_guessed == []
        UserInputChk = CheckingNatureOf_userInput(userInput)

        
        if UserInputChk is True:
            if userInput in letters_guessed:
                    num_guesses -= 1
                    print ('You have already picked that letter')
                    print ('You now have',num_guesses,'guesses left')
                    
            elif userInput not in letters_guessed:
                letters_guessed == letters_guessed.append(userInput)
        
        Available_letters = get_available_letters(letters_guessed)
        Guessed_word = get_guessed_word(secret_word, letters_guessed) 
        
        #CHECKING WHETHER THE INPUT IS IN THE SECRET WORD
        


        def CheckingInputIn_Secretword(userInput):
            '''
            userInput : (str) letter the user guesses
            Boolean .....
            Returns True if userInput is in secret word else False'''
            while UserInputChk is True:
                if userInput in secret_word:
                    return True
                else:
                    return False
        
        CheckInputIn_SecretWord = CheckingInputIn_Secretword(userInput)
        
        if UserInputChk :
            if CheckInputIn_SecretWord :   # is True  :
                print ('Good guess:', Guessed_word)
                print ('Available letters:', Available_letters )
                print ('----------------------------------')
            elif (not CheckInputIn_SecretWord) and (num_guesses > 0):
                num_guesses -= 1
                print ('Oops, That letter is not in the secret word')
                print ('You now have ',num_guesses,'guesses left')
                print ('Guess: ',Guessed_word)
            elif (not CheckInputIn_SecretWord) and (num_guesses <=0):
                print ('Failed')
                break

    def check_score(num_guesses,secret_word):
        '''
        num_guesses : number of remaining guesses the user has (str)
        secret_word : the word the user is guessing (int)
        Calculates the player's total score and returns the value,
        total = guesses remaining * total of unique characters in secret_word'''
        
        unique = []
        for char in secret_word:
            if char not in unique:
                unique.append(char)
        total = num_guesses * len(unique)
        return total
    
    score = check_score(num_guesses,secret_word)
    
    if num_guesses == 0:
        print ('You have run out of guesses and have lost the game!!!')
        print ('You shall be hanged!!!!..... The word was:',secret_word)
    if LoopBreak:
        print ('Congratulations you have won the game')
        print ('You guessed the secret word: ',secret_word)
        print ('Your score is: ',score)
    
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)

#WORKS LIKE A BITCH ON DRUGS