# Problem Set 4A
# Name: <I-ME-YOU>                          JOBI CLINTON
# Collaborators:NONE
# Time Spent: x:xx   N/A    15th feb 2018

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    ##COME BACK AND REALLY UNDERSTAND THIS
    
    permutations = []
    if len(sequence) <= 1:                                #base case
        return [sequence]                            ##recursion down to 1
                                                            ## 's' returns 's'
                                                            ## 'st' returns 'st' 'ts' ie .. it returns t then s , s then t
                                                            ##permutation [a,b,c] = [a + permutation [b,c],b + permutation[a,c],c + permutation[a,b]]
                                                        ##dunno how none of this works buh it works
    else:
        for item in sequence:    
            word = get_permutations(sequence.replace(item, ''))     #assingning the recursive_func 
            for i in word:                                   #iterating through word
                permutations.append(item + i)                     #adding the first letter bck
        return permutations

if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'bazi'
    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here

