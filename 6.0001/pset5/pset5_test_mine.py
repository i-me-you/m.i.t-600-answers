# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 19:56:15 2018

@author: me!
"""

'''test cases'''
from ps5 import *
test = TitleTrigger('Purple CoW')
test2 = TitleTrigger('purple cow')

##using their inputs but their same input fails in their test cases why??

cuddly = 'the purple cow is soft and cuddly'
exclaim = 'purple!!! cow!!!'
symbols = 'purple&^%$$cow'
spaces = 'did you see a purple cow?'
caps = 'the farmer owns a really PURPLE cow'
exact = 'purple cow'
plural = 'purple cows are cool'
seperate = 'that purple blob over there is a cow'
brown = 'how now brown cow'
badorder = 'cow*** purple&&'
nospaces = 'purplecowpurplecowpurplecow'
nothing = 'i like poison dart frogs'


truecases = (cuddly, exclaim, symbols, spaces, caps, exact)
falsecases = (plural, seperate, brown, badorder, nospaces, nothing)

for test in (test, test2):
    for item in truecases:
        assert test.evaluate(item), 'didnt fire'
    for item in falsecases:
        assert not test.evaluate(item), 'fired'
#for char in falsecases:
#    if test.evaluate(char) == True:
#        print (char, 'failed should be false')
#    elif test.evaluate(char) == False:
#        print ('ALL GOOD')
#        
#for char in truecases:
#    if test.evaluate(char) == True:
#        print ('ALL GOOD')
#    elif test.evaluate(char) == False:
#        print (char, 'failed should be true')
#
#for char in falsecases:
#    if test2.evaluate(char) == True:
#        print (char, 'failed should be false')
#    elif test2.evaluate(char) == False:
#        print ('ALL GOOD')
#        
#for char in truecases:
#    if test2.evaluate(char) == True:
#        print ('ALL GOOD')
#    elif test2.evaluate(char) == False:
#        print (char, 'failed should be true')
