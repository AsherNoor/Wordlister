"""
----------------------------
| Text File Word Extractor |
----------------------------
By: ryn0f1sh (Ash Noor)
Email: ryn0f1sh@protonmail.com
Site: AshNoor.me
Blog: ryn0f1sh.blog

----------------
======================================================================
This function extracts all the data from a txt file.
It deletes punctuations & duplicate words.
Then creates a wordlist.
======================================================================
"""

'''The IMPORTS '''
import os
import sys
import string
from time import sleep

''' The Text Input '''
def text_extractor():
    '''---------------------
        User Input : The Text file name
        ----------------------'''
    ui_filename = input("Enter the name of the file without the '.txt': ")
    print("One moment, reading ", ui_filename)
    sleep(1)

    #-- Open and Read the file.
    TheFile = open(ui_filename+'.txt', 'r')
    #-- Extracting the text into a variable.
    text = TheFile.read()
    TheFile.close()

    #-- To remove any special characters attached to a word
    sleep(1)
    print("Removing punctuations and special characters.")
    translator = str.maketrans('', '', string.punctuation)
    new_text = text.translate(translator)

    #-- Creating an Empty wordlist
    wl =[]
    #-- Appending non-duplicates into the list.
    for word in new_text.split():
        if word not in wl:
            wl.append(word) #-- Add the word to wl
            wl.sort() #-- To Alphabetize



    #-- Info for the user
    sleep(1)
    print("Removing the duplicates.")
    sleep(1)
    print("Creating your text file.")


    #-- Creating the Text File
    with open(ui_filename+"_Wordlist.txt", 'a') as f:
        for x in wl:
            if x.isalpha():
                print(x, file=f)
            else:
                pass
        f.close()
        sleep(1)
        print("[- - - Your Wordlist Is Ready - - -]")




'''------------------
CALLING THE FUNCTIONS
----------------------'''
#-- Using a Main Guard to prevent it from running when Imported.
if __name__ == '__main__':
    text_extractor()
