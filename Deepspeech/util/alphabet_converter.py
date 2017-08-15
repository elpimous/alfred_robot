# -*- coding: utf-8 -*-
import os

########################################################################################
#
#   A simple routine who use an alphabet string to assign a value to each character,
#   and assign the n_character value.
#
#
#   for use in DEEPSPEECH project
#
#                                               Vincent FOUCAULT elpimous12@orange.fr
########################################################################################

# Mod v1.1 #

cwd = os.getcwd()

try :
    with open(cwd+'/data/alphabet/alphabet.txt') as alphabet:
        "read your alphabet file characters"
        characters = alphabet.readlines()[1] #read lign 2
        "transform to unicode"
        characters = unicode(characters, 'utf8')
        characters = characters.replace('\n','') # can be usefull, in case of line return on last alphabet letter
        "split list"
        characters = characters.split(',')
        "assign number of characters in your personal alphabet"
        characters_numbers = len(characters)

except :
	print('\n\n-----------------------------------------------------------\n!!! Alphabet_converter must be started from Deepspeech dir\
	\n-----------------------------------------------------------\n\n')


"Convert each letter to corresponding value"
def read(letter):
    "replace the letter by an integer (ex: a,b,c,d   c=3)"
    if letter in characters:
        letter = characters.index(letter)+1
    else :
        print("\n\n--------------------------------------------\n!!! the letter <"+letter+"> isn't in your alphabet !\
        \nPlease change it content !\n--------------------------------------------\n\n")
    return(letter)


"Return each value to corresponding letter"
def write(data):
    data-=1
    letter = characters[data]
    return(letter)


