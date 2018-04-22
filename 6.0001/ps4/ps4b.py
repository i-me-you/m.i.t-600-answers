# Problem Set 4B
# Name: <i-me-you>
# Collaborators:none
# Time Spent: x:xx  N/A    15feb 2018

import string



### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):                                      #creating the object type 'message'
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

#        pass #delete this line and replace with your code here
    def __str__(self):
        '''returns the message string'''
        return str(self.message_text)
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

#        pass #delete this line and replace with your code here

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy()

#        pass #delete this line and replace with your code here

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        uppercase = string.ascii_uppercase
        lowercase = string.ascii_lowercase
        shift_dict = {}
##mapping uppercase letters
        for char in uppercase:
            x = uppercase.index(char) + shift
            if x >= 26:
                x = (x - 26)
            shift_dict[char] = uppercase[x]
##mapping lowercase letters
        for item in lowercase:
            y = lowercase.index(item) + shift
            if y >= 26:
                y = (y - 26)
            shift_dict[item] = lowercase[y]
        return shift_dict
#        pass #delete this line and replace with your code here

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        ###DOES NOT MODIFY THE self.message_text
        ###returns shifted version .. the message text remains unchanged
        shift_dictionary = self.build_shift_dict(shift)
        TEXT = ''
        for char in self.message_text:
            if not char.isalpha():
                TEXT += char
            else:
                TEXT += shift_dictionary[char]
        return TEXT
#        pass #delete this line and replace with your code here

class PlaintextMessage(Message):                           #creating an object of type 'message/' named plaintextmessage
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)
        '''
        Message .__init__(self, text)
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)  
#        pass #delete this line and replace with your code here

#############################???????????///
    def __str__(self):
        '''returns encoded text .. i guess'''
        return 'Encoded message:: ' + str(self.get_message_text_encrypted)
    
    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift
#        pass #delete this line and replace with your code here

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict.copy()
#        pass #delete this line and replace with your code here

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted
#        pass #delete this line and replace with your code here

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
#        pass #delete this line and replace with your code here


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
#        pass #delete this line and replace with your code here

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        dict_shift = {}                                   #pair of shift nd msg wth shift
        max_num_shift = {}                       #pair of shift and num of valid words formed wth it
        dict_message_list = {}                   #pair of shift and list of msg wth shift
        
        ###now i have a dictionary of shifts and decrypted messages
        for shift in range(0,27):
            dict_shift[shift] = self.apply_shift(shift)
        
        ##finding the best shift value
        
        ##dictionary of shifts and decrypted msg list
        for char in dict_shift.keys():
            dict_message_list[char] = dict_shift[char].split()
        
        for item in dict_message_list.keys():                     #thru err key
            max_num_shift[item] = 0                   #each shift has 0 to start
            for eachword in dict_message_list[item]:            #each key's value which is a list
                if is_word(self.valid_words, eachword):       #if the word is valid
                    max_num_shift[item] += 1                    #increase the value paired wthe d shift by 1 for each word
        
        ##get best shift value ie key wth largest value
        def key_with_max_value(d):
            ''' d = dictionary
            create a list of d.keys() and d.values()
             return max value'''
         
            key_list = list(d.keys())
            value_list = list(d.values())
            return key_list[value_list.index(max(value_list))]
        
        return (key_with_max_value(max_num_shift), self.apply_shift(key_with_max_value(max_num_shift)))
#        pass #delete this line and replace with your code here

if __name__ == '__main__':

#    #Example test case (PlaintextMessage)
#    plaintext = PlaintextMessage('hello', 2)
#    print('Expected Output: jgnnq')
#    print('Actual Output:', plaintext.get_message_text_encrypted())
#
#    #Example test case (CiphertextMessage)
#    ciphertext = CiphertextMessage('jgnnq')
#    print('Expected Output:', (24, 'hello'))
#    print('Actual Output:', ciphertext.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE
    #Plaintext test cases
#    Plaintext = PlaintextMessage('Hello, World!',4)
#    print ('Expected Output: Lipps, Asvph!' )
#    print ('Actual Output: ', Plaintext.get_message_text_encrypted())
#
#    x = 'aou'    
#    Plaintext2 = PlaintextMessage(x,6)       
#    print ('Expected Output : gua')
#    print ('Actual Output :', Plaintext2.get_message_text_encrypted())
#    
#    #Cyphertext test cases         
#    ciphertext = CiphertextMessage('Lipps, Asvph!')
#    print ('Expected output:(22, Hello, World!)')
#    print ('Actual Output :', ciphertext.decrypt_message())
#    
#    ciphertext2 = CiphertextMessage('dcf')
##    print ('Expected output: bad')
#    print ('Actual output :', ciphertext2.decrypt_message())
    
    
#    #TODO: best shift value and unencrypted story 
#    '''best shift value = 12
#    unencrypted story =Jack Florey is a mythical character created on the spur of a moment to help
#    cover an insufficiently planned hack. He has been registered for classes at MIT twice before, 
#    but has reportedly never passed aclass. It has been the tradition of the residents of East Campus to
#    become Jack Florey for a few nights each year to educate incoming students in the ways, means, and
#    ethics of hacking. '''
    
    
#    encrypted_story = get_story_string()
#    print(encrypted_story)
#    story = Message(encrypted_story)
#    decrypting_story = CiphertextMessage(encrypted_story)
#    print (decrypting_story.decrypt_message())
#    
    
    pass #delete this line and replace with your code here
