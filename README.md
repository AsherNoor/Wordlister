# Wordlister
A program to help you create a wordlist from a PDF or Text file.

--------------
| Wordlister |
--------------
Coded using Python 3.

A program to help you create a wordlist from a PDF or Text file.
You give it a Text or a PDF file, it will extract the text from said file, remove punctuations, numbers, duplicates, and give you a text file with what is left in list form.

HOW TO USE IT:
--------------
Make sure the PDF or Text file is in the same folder as Wordlister.
Simply run Wordlister.py and it will prompt you for what it needs.

Running From Terminal
---------------------
If you are planning on running it from the terminal, you need to make sure that you have PyPDF2 installed on the host machine. Otherwise it will give you an error.
> pip install PyPDF2

Ubuntu:
For some reason, Ubuntu has a hard time running this from terminal, you may need to use an IDE for it.

Parrot / Kali:
As long as you have the PyPDF2 installed on the machine, you would be able to simply ( python Wordlister.py ).


Using an IDE
------------
This is the preferd method to be honest, it ran perfectly.
I created and tested it using PyCharm, and in doing so, it gave me the Wordlist in the same folder as the program.
If you use VS Code, it will put the Wordlist in your /home folder.
If you use anything else, you may need to check you /var folder, and do a search for "YourFileName_Wordlist.txt"


Files
-----
You will find 4 files in here.
Wordlister.exe (Executiable for Windows)
Wordlister.py
PDFfunction.py
TEXTfunction.py

Wordlister imports PDFfunction & TEXTfunction, to make it an all in one experience, allowing you to create one of each or more.

You can of course run the other 2 files on their own if you like, both will create a wordlist for you. 
PDFfunction takes a .pdf file.
TEXTfunction takes a .txt file.


Hope you enjoy the program.
Ash Noor (ryn0f1sh)
www.AshNoor.net
www.ryn0f1sh.blog
