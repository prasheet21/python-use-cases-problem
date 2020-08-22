#!python

import os 
import pyttsx3

pyttsx3.speak("Welcome to the User Commands Manual")
pyttsx3.speak("Hello prasheet ... hope you are fine . Tell me what can i do for you .. ?")
while True : 
    text = input("Enter any task of your choice : ").lower() 
    if text == "exit" :
        pyttsx3.speak("Thankyou for using this command manual")
        print("Thankyou for using this command manual")
        break
    if not "not" in text :
        if (("run" in text) or ("launch" in text) or ("open" in text)) :
            if (("chrome" in text) or ("google" in text) or ("google chrome" in text) or ("browser" in text)) :
                pyttsx3.speak("Opening Chrome")
                os.system("chrome &") 
            elif ("notepad" in text) or ("text editor" in text) or ("editor" in text) :
                pyttsx3.speak("Opening notepad ")
                os.system("notepad &")
            elif ("visual studio code" in text) or ("visual studio" in text) or ("studio code" in text) :
                pyttsx3.speak("Opening visual studio code")
                os.system("code . &")
                
            elif ("microsoft edge" in text) or ("edge" in text) or ("msedge" in text) :
                pyttsx3.speak("Opening microsoft edge")
                os.system("msedge &")
                
            elif ("media player" in text) or ("player" in text) :
                if ("vlc" in text) :
                    pyttsx3.speak("Opening vlc player")
                    os.system("vlc &")
                else : 
                    pyttsx3.speak("Opening windows media player")
                    os.system("wmplayer &")
                
            elif ("command prompt" in text) or ("cmd" in text) or ("terminal" in text) or ("cli" in text) or ("command line" in text) :
                pyttsx3.speak("Opening command prompt new terminal")
                os.system("start cmd ")
                
            elif ("jupyter notebook" in text) or ("jupyter" in text) or ("notebook" in text) : 
                pyttsx3.speak("Opening jupyter notebook")
                os.system("jupyter notebook &")
                          
            elif ("microsoft word" in text) or ("word" in text) or ("ms word" in text) or ("msword" in text) :
                pyttsx3.speak("Opening microsoft word")
                os.system("start winword &")
                
            elif ("microsoft excel" in text) or ("excel" in text) or ("ms excel" in text) or ("msexcel" in text) :
                pyttsx3.speak("opening microsoft excel")
                os.system("start excel &")
                
            elif ("microsoft powerpoint" in text) or ("powerpoint" in text) or ("ms powerpoint" in text) or ("mspowerpoint" in text) :
                pyttsx3.speak("opening microsoft powerpoint")
                os.system("start powerpnt &")
                
            elif ("calc" in text) or ("calculator" in text) :
                pyttsx3.speak("opening calculator")
                os.system("calc &")
            elif ("powershell" in text) or ("windows shell" in text) :
                pyttsx3.speak("Opening powershell terminal")
                os.system("start powershell")
            else :
                print("Command not found")
        else :
            if ("hi" in text) or ("hello" in text) :
                pyttsx3.speak("Hii Prasheet")
                print("Hii Prasheet")
            elif ("about" in text) and ("you" in text) or ("how" in text) and ("you" in text) :
                pyttsx3.speak("I am fine .... hope the same for you !!")
                print("I am fine .... hope the same for you !!")
            elif ("capabilities" in text) or ("can you do" in text) :
                pyttsx3.speak("i can open following things for you : google chrome , notepad , visual studio code , microsoft edge , vlc media player , windows media player , command prompt terminal , jupyter notebook , windows media player , microsoft word , microsoft excel , microsoft powerpoint , windows powershell , calculator ....... and you can type exit to leave this manual")
                print("google chrome \n notepad \n visual studio code \n microsoft edge \n vlc media player \n windows media player \n command prompt terminal \n jupyter notebook \n windows media player \n microsoft word \n microsoft excel \n microsoft powerpoint \n windows powershell \n calculator \n type 'exit' to leave")
            elif ("thanks" in text) or ("thanx" in text) or ("thankyou" in text) :
                pyttsx3.speak("welcome")
                
                