"""
-----------------
| [bini-tek] \\ |
-----------------
By: [bini-tek]\\
Email: binitek.baltimore@gmail.com
Site: www.binitek.com
Discord: Home of bini-tek (https://discord.gg/4GqDrH)


----------------------
| Version #:  001    |
| DATE:  Mar/29/2021 |
----------------------

---------------
| EXPLANATION |
---------------
| Wordlister
| To create a wordlist out of a Text or PDF file.
----------------------



----------------
| CONTRIBUTORS |
----------------
| Ash Noor (ryn0f1sh)
| Coder
| Site: AshNoor.me
| Email: ryn0f1sh@protonmail.com
| Blog: ryn0f1sh.blog
---------------------------------

"""

# -- IMPORTS --
from time import sleep

#-- My custom function.
import PDFfunction as PDE
import TEXTfunction as TDE





#-------------------------
# -- The Intro Function --
def intro():
    print("\n-----------------------"
           "\nWelcome to Wordlister"
           "\n-----------------------")

    # -- Call the File Choice function to start the program.
    fileChoice()

# --- End of Intro Function --
#-----------------------------




#------------------------------------
# -- The fileChoice Function here --
def fileChoice ():
    #-- info for user
    print("PLEASE NOTE: "
          "\nMake sure the file you are extracting is the same folder as this program.")
    sleep(2)

    #-- The Menu of File Types..
    print("\n-----------"
          "\n| M E N U |"
          "\n-----------"
          "\n[1]: Text (.txt) File."
          "\n[2]: PDF (.pdf) File.")

    #-- UI: The type of file.
    sleep(1)
    file_type = int(input("What type of file are you using?: "))

    #-- Analysing the UI.
    if (file_type == 1):
        TDE.text_extractor()
    elif (file_type == 2):
        PDE.pdf_extractor()
    else:
        print("No such choice")

    run_again()

# -- End of File Choice Function --
#----------------------------------




#-----------------------------
# -- The Run Again Function --
def run_again():
    # Getting the Y/N answer.
    yn_answer = input("\n\nRun Wordlister again? y/n : " )
    if (yn_answer.lower() == 'y'):
       # -- Call the File Choice function again.
       fileChoice()
    else:
        #-- Call the Outro function.
        outro()
# --- End of Run Again Function --
#---------------------------------







#-------------------------
# -- The Outro Function --
def outro():

    print("\nThank you for using Wordlister."
          "\nExiting Program, please wait.")
    sleep(2)

    print("\n-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-"
        "\nCoded by: Ash Noor (ryn0f1sh)"
        "\nSite: www.AshNoor.me"
        "\nEmail: ryn0f1sh@protonmail.com"  
        "\n----- ----- ----- ----- -----"
        "\nBrought to you by: [bini-tek]\\\\"
        "\nSite: www.binitek.com"          
        "\nEmail: binitek.baltimore@gmail.com"
        "\nDiscord: Home of bini-tek (https://discord.gg/4GqDrH)"    
        "\n-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-")
    # -- Any Key to Exit --
    input("\n\n\t>->-> [ Please press ENTER key to Exit ] <-<-<")
# --- End of Outro Function --
#-----------------------------





"""
Calling The functions here.
- I will call the Intro().
- Intro () will call the program's main function.
- The others are embedded within that.
- I will also call the Run Again() function.
"""

intro()
