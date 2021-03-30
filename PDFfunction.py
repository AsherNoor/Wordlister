"""
----------------------------
| PTE (PDF Text Extractor) |
----------------------------
By: ryn0f1sh (Ash Noor)
Email: ryn0f1sh@protonmail.com
Site: AshNoor.me
Blog: ryn0f1sh.blog

----------------
======================================================================
This function extracts all the data from a PDF file into a text file.
It reads the extracted PDF data, deletes punctuations & duplicate words.
Then creates a wordlist..
======================================================================
"""

''' The IMPORTS '''
import string
from PyPDF2 import PdfFileReader, PdfFileWriter
from time import sleep
import codecs




''' The PDF Input  '''
def pdf_extractor():
    '''--------------------- 
    User Input : The PDF file name
    ----------------------'''
    # User Input : Name of the PDF file.
    ui_PDFFileName = str(input("Enter the PDF file name without the '.pdf': "))


    '''-------------------------------- 
    The PDF info extraction Section 
    --------------------------------'''
    # Opening the PDF file
    PDFfile = open(ui_PDFFileName+".pdf", "rb")
    # Reading the PDF file
    pdfread = PdfFileReader(PDFfile, strict=False)

    # Get the number of pages of this file.
    num_of_pages = pdfread.numPages
    print("One moment, reading ", ui_PDFFileName)
    sleep(1)



    '''------------------------------------------ 
    The TEXT file creation & appending section 
    ------------------------------------------'''
    # A While loop to extract the whole file.
    i = 0
    while i < num_of_pages:
        pageinfo = pdfread.getPage(i)
        txt = pageinfo.extractText()

        #Encode the txt to utf-8 (converts bytes to string)
        encoded = txt.encode("utf-8")

        # Write to a text file & close text file
        text_file = open("PDFextracted.txt", "a")
        text_file.write("Page: "+str(i+1)+"\n"+str(encoded)+"\n"*2)
        text_file.close()
        i += 1

    sleep(1)
    print("PDF text has been extracted.")
    #-- Call the Wordlist creator
    theTextFile(ui_PDFFileName)



'''------------------ 
The Wordlist Creation
---------------------'''
# -- Creating the Text File
def theTextFile (ui_PDFFileName):
    # -- Open and Read the file.
    TheFile = open('PDFextracted.txt', 'r')
    # -- Extracting the text into a variable.
    text = TheFile.read()
    TheFile.close()

    # -- To remove any special characters attached to a word
    translator = str.maketrans('', '', string.punctuation)
    new_text = text.translate(translator)

    # -- Empty list
    wl = []
    # -- Appending non-duplicates into the list.
    for word in new_text.split():
        if word not in wl:
            wl.append(word)  # -- Add the word to wl
            wl.sort()  # -- To Alphabetize

    # -- Info for the user
    sleep(1)
    print("Removing punctuations and special characters.")
    sleep(1)
    print("Removing the duplicates.")
    sleep(1)
    print("Creating your text file.")

    with open(ui_PDFFileName+"_Wordlist.txt", "a") as f:
        for x in wl:
            #cleaned_data = x.translate(str.maketrans('', '', string.punctuation))
            # -- To check if what's on the line is a word 'Alpha' or not.
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
    pdf_extractor()










"""
-------------------
| The Scratch Pad |
-------------------
Slices of codes that was not used.
----------------------------------

#This is only to display it on the screen.
print("The while extract \n", encoded).




"""