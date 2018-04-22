# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <i-me-you>
# Collaborators : <none>
# Time spent    : <dunno but finished on 22/01/2018>
###took like a week tho 
###steady income idea use bots for ads traffic and get the money for the traffic
###replicating unique bots
###


import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
WILDCARD = '*'

SCRABBLE_LETTER_VALUES = {
    WILDCARD:0,'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    word = word.lower()
    #FIRST COMPONENT SUM OF POINTS FOR LETTERS IN WORD
    FirstComponent = 0
    
    for item in word:
        FirstComponent += SCRABBLE_LETTER_VALUES[item]
    
    x = 7 * len(word) - 3 * (n - len(word))
    if 1 > x:
         SecondComponent = 1
    elif x > 1:
        SecondComponent = x
    
    return FirstComponent * SecondComponent
    
    
    
    #pass  # TO DO... Remove this line when you implement this function

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    y = []
    for letter in hand.keys():
        for j in range(hand[letter]):
#            print( letter, end=' ')      # print all on the same line
            y.append(letter)                            #edit1 cuz of none ish
#    print()                              # print an empty line
    return ' '.join(y)                           #edit two
    
#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels-1):          #adds (ceil(n/3)-1) random vowels to make up hand
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):        #adds 7 - ceil(n/3) random consonants to make up hand
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    #give one wildcard per  hand
    for i in range(len(WILDCARD)):
        hand[WILDCARD] = 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    ##eg hand = {'a':2,'b':3,'c':4}   ie 'aa bbb cccc'  
    ##eg word = 'abc'   or  'aaabcd'
    ## returns {'a':1,'b':2,'c':3}  or {'a':0,'b':2,'c':3}   
    ##if word contains a letter that is not in hand dict ignore the letter or if a letter appears
    ##more than the frequency in hand dict ignore the extras
    
    
    HandCopy = hand.copy()
    word = word.lower()
    def letter_freq_in_word(word):                  #same aas word_to_dict just word_to_dict accounts for wildcards
        '''word = str
        returns dict of letters in word and their frequencies
        i.e if word = 'apple' returns {'a':1,'p':2,'l':1,'e':1}'''
        Dict = {}
        for i in word:
            if i not in Dict.keys():
                Dict[i] = 1
            elif i in Dict.keys():
                Dict[i] += 1
        return Dict
    
    LetterFrequency = letter_freq_in_word(word)
    for item in LetterFrequency.keys():                
        if item in HandCopy:
            HandCopy[item] = HandCopy[item] - LetterFrequency[item]   ##deleting the keys that r empty
            if HandCopy[item] < 1:
                HandCopy[item] = 0
                del(HandCopy[item])
        
    return HandCopy
    #pass  # TO DO... Remove this line when you implement this function

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    HandCopy = hand.copy()
##    BooleanStore = []
    word = word.lower()
    def word_to_dict(word):
        '''word = str
        returns dict of letters in word and their frequencies
        i.e if word = 'apple' returns {'a':1,'p':2,'l':1,'e':1}'''
        Dict = {}
        for i in word:
            if i not in Dict.keys():
                Dict[i] = 1
            elif i in Dict.keys():
                Dict[i] += 1
            elif i == WILDCARD:                 #wildcard mod
                Dict[WILDCARD] = 1
        return Dict
    
#    LetterFrequency = letter_freq_in_word(word)
    
    
    #compaaring hand dict and letter frequency in word  dict
    def compare_dicts(dict1,dict2):
        '''dict1/dict2: dictionaries
        checks to see if all the key values in dict1 can be contained in 
        dict2'''
        
        ##dict1 = word turned to dict {alphabet -> occurence}
        ##dict2 = hand
        
        Bool = []
        for item in dict1:
            if (item in dict2):
                if dict2[item] >= dict1[item]:
                    Bool.append(True)
                elif dict2[item] < dict1[item]:
                    Bool.append(False)
            elif item not in dict2:
                Bool.append(False)
        if False in Bool:
            return False
        else:
            return True
    
    ##checking whether if wild card is replaced by a vowel it makes a valid word
    def checkWildWord(wildword):
        '''wildword = str containing wildcard '*'      
        checks if  the wildcard '*' in word can for a valid word in wordlist if replaced by a vowel'''
        vowel = 'aeiou'
        for char in vowel:
            if wildword.replace('*',char) in word_list:
                return True
    
    if compare_dicts(word_to_dict(word),HandCopy) and checkWildWord(word):
        return True
    else:
        return False
    
#    pass  # TO DO... Remove this line when you implement this function

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    return sum(hand.values())
#    pass  # TO DO... Remove this line when you implement this function

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
#    hand = deal_hand(7)
    TotalScore = 0
    
    loopbreak = False
    
    while  len(hand) != 0:                   #while letters are still in hand
        
        print ('Current hand:',display_hand(hand))
        userinput = str(input('Enter word, or "!!" to indicate that you are finished:'))
        
        if userinput == '!!':
            loopbreak = True
            TotalScore = TotalScore
            break
    
        if is_valid_word(userinput,hand,word_list):
            hand = update_hand(hand,userinput)
            TotalScore += get_word_score(userinput,len(hand))
            print (userinput,'earned:',get_word_score(userinput,len(hand)),'points.......','Total:',TotalScore,'points')
        elif not is_valid_word(userinput,hand,word_list):
            
            hand = update_hand(hand,userinput)
            if len(hand) == 0:
                print ('That\'s not a valid word')
            elif len(hand) != 0:
                print ('That is not a valid word, Please choose another word')
    

    if loopbreak:
        print ('You Quit, Your total score is :',TotalScore, 'points')
    if len(hand) == 0:  #out of letters           #hmmmmmmmmm
        print ('You have run out of letters, Your total score is:',TotalScore, 'points')
        
    return TotalScore

#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    def letterInHandCheck(ltr,hand):
        '''ltr = random vowels,consonants 
        hand = dict
        returns true if ltr  in hand'''
        if ltr in hand.keys():
            return True
        else:
            return False
                                       
    def chooseRandomLetter(letter,hand):
        '''returns a random letter not in hand'''
#        vowels = list(VOWELS)
#        consonants = list(CONSONANTS)
#        if letterInHandCheck(x,hand):
#            vowels.remove(x)
#        if letterInHandCheck(y,hand):
#            consonants.remove(y)
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        listalpha = list(alphabets)
        if letter in hand.keys():
            listalpha.remove(letter)
            
        return random.choice(listalpha)
    
    def letter_freq_in_word(word):
        '''word = str
        returns dict of letters in word and their frequencies
        i.e if word = 'apple' returns {'a':1,'p':2,'l':1,'e':1}'''
        Dict = {}
        for i in word:
            if i not in Dict.keys():
                Dict[i] = 1
            elif i in Dict.keys():
                Dict[i] += 1
        return Dict

    HandCopy = display_hand(hand)             #changing hand to str
    Handlist = list(HandCopy)                         #changing str to list
    
    for item in Handlist:                       #removing spaces from list
        if item == ' ':
            Handlist.remove(item)
    
    NewCopy = ''.join(Handlist)                   #new word( without spaces
  #  print ('old copy:', NewCopy)
    
    if letter in NewCopy:
        NewCopy = NewCopy.replace(letter,chooseRandomLetter(letter,hand))
  #  print ('new copy:', NewCopy)
    if letter not in hand.keys():
        return hand
    elif letter in hand.keys():
        return letter_freq_in_word(NewCopy)

#    pass  # TO DO... Remove this line when you implement this function
       
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    ##gonna finish you now
    
    #WELCOME
    print ('''MIT word game...dealing with words
Let's see how well you can form words''')
    
    #GETTING NUMBER OF HANDS TO DEAL 
    FirstInput = int(input('''Enter a total number of hands
>'''))

    #DEALING THE INPUTTED NUMBER OF HANDS   (//iono whether inputted is a real word tho)
    
    TotalScoreOfHands = 0
    ListOfHands = []
    if FirstInput < 1:
        print ('Enter a non_negative int > 0')
    elif FirstInput >= 1:
        while FirstInput > 0:
            ListOfHands.append(deal_hand(HAND_SIZE))
            FirstInput -= 1

#### print (ListOfHands)
####first hand @ ListOfHands[0] 2nd @ ListOfhands[1].......etc
    ##CHOOSING HANDS                   #while list of hands empty
    for char in ListOfHands:
        Hand = char
        print ('Current hand:',display_hand(Hand))
        
    ##ASKING TO SUBSTITUTE A LETTER 
        SecondInput = input('''Would you like to substitute a letter?....... (Enter Yes/No)
>''')
        ###modules modules modules
        def CheckSecondInput(SecondInput):
            '''returns bool . true if second input is alpha false otherwise'''
            if SecondInput.isalpha():
                SecondInput = SecondInput.lower()
                return True
            elif not SecondInput.isalpha():
                return False

        
        ##some warning shots
        if not CheckSecondInput(SecondInput):
            print( '''You can\'t substitute a letter for this hand again,
next time enter "Yes or No"''')
            pass

        elif CheckSecondInput(SecondInput):
            SecondInput = SecondInput.lower()
        
        if SecondInput == 'no':
            pass
        elif SecondInput == 'yes':
            letterinput = str(input('Enter the letter to substitute  :'))
            Hand = substitute_hand(Hand,letterinput)
        elif SecondInput != 'yes' or 'no':
            print( '''You can\'t substitute a letter for this hand again,
next time enter "Yes or No"''')
        
        
        #playing a hand
#        play_hand(Hand,word_list)
        score_per_hand = play_hand(Hand,word_list)
        TotalScoreOfHands += score_per_hand
        print ('Total score for this hand :', score_per_hand)
        print ('----------------------------------')
        lastinput = str(input('''Do you want to replay the hand?     (Enter Yes/no)
        >'''))
        lastinput = lastinput.lower()
        if lastinput == 'yes':
            TotalScoreOfHands += play_hand(Hand,word_list)
        elif lastinput == 'no':
            ListOfHands.remove(char)
        
    print ('Total score of all hands:',TotalScoreOfHands)
#       print ('Current hand:', display_hand(Hand))


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
