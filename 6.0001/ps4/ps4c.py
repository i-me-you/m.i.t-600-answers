# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string, random
from ps4a import get_permutations


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


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        pass #delete this line and replace with your code here
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text
        pass #delete this line and replace with your code here

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy()
        pass #delete this line and replace with your code here
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        cipher_dict = {}
        index_count = 0
        count = 0
        
        ##mapping consonants to the dict
        for char in CONSONANTS_LOWER:
            cipher_dict[char] = char
        for char in CONSONANTS_UPPER:
            cipher_dict[char] = char
            
        ##map vowel permutation to input 
        for char in VOWELS_LOWER:
            cipher_dict[char] = vowels_permutation[index_count]
            index_count += 1
        for char in VOWELS_UPPER:
            cipher_dict[char] = vowels_permutation[count].upper()
            count += 1
        return cipher_dict
#        pass #delete this line and replace with your code here
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        ##use transpose dictionary to encrypt message text
        TEXT = ''
        for char in self.message_text:
            if not char.isalpha():
                TEXT += char
            else:
                TEXT += transpose_dict[char]
#                print (TEXT,transpose_dict[char])            ##TESTING
        return TEXT
#        pass #delete this line and replace with your code here
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text)
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
#        pass #delete this line and replace with your code here

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        ###HELPER FUNCTION TO GET NUM OF VALID WORDS IN A TEXT (DECRYPTED)
        def get_max_words(decrpt_text,wordlist):
            '''derypt_text = a decrypted text based on transpose dict
            wordlist = list of valid words
            returns the num of valid words in decrpted text'''
            wordcount = 0
            decrpt_text = decrpt_text.lower()
            decrpt_text = decrpt_text.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
            for word in decrpt_text.split():
                if word in wordlist:
                    wordcount += 1
            return wordcount

#        TEST_LIST = []          #TESTIINGG

        num_valid_word_dict = {}                     #DICT OF 'permutation' -> no of  VALID WORDS IN decrypted message
        for char in get_permutations('aeiou'):    #going thru each permutation
            
            transpose_dictionary = self.build_transpose_dict(char)
            decrypted_text = self.apply_transpose(transpose_dictionary)
            num_valid_word_dict[char] = get_max_words(decrypted_text, self.valid_words)
#            TEST_LIST.append(decrypted_text)            ###TESTING



##      print (TEST_LIST)     #list of all ddecrypted msgs     #uncomment line 202
                                    #incase the msg contains slangs/name's etc ,,


###HELPER FUNCTION TO GET THE KEY WITH LARGEST VALUE IN A DICTIONARY
        def key_with_max_value(d):
            ''' d = dictionary
            create a list of d.keys() and d.values()
             return max value'''
            key_list = list(d.keys())
            value_list = list(d.values())
            return key_list[value_list.index(max(value_list))]


        max_valid_words = []             #for storing all the permutations  that makes maximum num of valid words
        decrypt_msg_dict = {}                     #dict of 'permutation' -> 'decrypted msg wth max num of valid words'
        x = max(num_valid_word_dict.values())
        for item in num_valid_word_dict.keys():
            if num_valid_word_dict[item] == x:
                max_valid_words.append(item)

        for item in max_valid_words:          ##getting a list of permutation nd decrypted msg
            permutation = item
            enc_dict = self.build_transpose_dict(permutation)
            decrypt_msg_dict[item] = self.apply_transpose(enc_dict)  

        decrypt_msg_list = []           #list of most valid decrpyted messages
#        print (num_valid_word_dict)
#        print (max_valid_words)
#        print (decrypt_msg_dict)



        for msg in decrypt_msg_dict.values():
            decrypt_msg_list.append(msg)
        print (num_valid_word_dict)


        ##MAKE IT RETURN SELF IF NO VALID WORDS
        if all(item == 0 for item in num_valid_word_dict.values()):
            return self.message_text
        else:
            return random.choice(decrypt_msg_list)                #returnin' any
#        pass #delete this line and replace with your code here
    

if __name__ == '__main__':

    # Example test case
#    print ('TESTING 1======================================')
#    message = SubMessage("Hello World!")
#    permutation = "eaiuo"  #aeiou a-e , e-a ,i-i, o-u, u- o
#    enc_dict = message.build_transpose_dict(permutation)
#
#    print("Original message:", message.get_message_text(), "Permutation:", permutation)
#    print("Expected encryption:", "Hallu Wurld!")
#    print("Actual encryption:", message.apply_transpose(enc_dict))
#    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
#    print("Decrypted message:", enc_message.decrypt_message())
##     
    #TODO: WRITE YOUR TEST CASES HERE
#    
#    print ('TESTING 2========================================')
#    message2 = SubMessage('aeiou')
#    permutation2 = 'ieauo'     #a-i e-e i-a o-u u-o
#    enc_dict2 = message2.build_transpose_dict(permutation2)
#    print ("Original message:", message2.get_message_text(), 'Permutation:', permutation2)
#    print ('Expected encryption:', 'ieauo')
#    #print (enc_dict2)
#    print ("Actual encryption:", message2.apply_transpose(enc_dict2))
#    enc_message2 = EncryptedSubMessage(message2.apply_transpose(enc_dict2))
#    print ('Decrypted message:', enc_message2.decrypt_message())