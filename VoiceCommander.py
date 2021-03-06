# import required module

import speech_recognition as sr
import keyboard
import time
import json

import winsound
from playsound import playsound

# explicit function to take input commands
# and recognize them

lang='hi-In'


def takeCommandHindi():
        global lang
        r = sr.Recognizer()
        
        with sr.Microphone() as source:
                # seconds of non-speaking audio before
                # a phrase is considered complete
                print('Listening')
                
                r.pause_threshold = 0.5
                
                audio = r.listen(source)
                
                try:
                        print("Recognizing")
                        if(lang=='en-In'):
                                print("Engish")
                        elif(lang=='hi-In'):
                                print("Hindi")
                        Query = r.recognize_google(audio, language=lang)
                        
                        # for listening the command in indian english
                        print("Command Recognized ='", Query, "'")
                
                # handling the exception, so that assistant can
                # ask for telling again the command
                except Exception as e:
                        print(e)
                        print("Say that again sir")
                        return "None"
                return Query

def takeaction(command):
        command=command.strip()
        keys=e[command].split()
        for key in keys:
                keyboard.press_and_release(key)
                time.sleep(0.1)


print(r"""

__/\\\________/\\\___________________________________________________________________/\\\\\\\\\____________________________________________________________________________________________/\\\_______________________________        
 _\/\\\_______\/\\\________________________________________________________________/\\\////////____________________________________________________________________________________________\/\\\_______________________________       
  _\//\\\______/\\\_________________/\\\__________________________________________/\\\/_____________________________________________________________________________________________________\/\\\_______________________________      
   __\//\\\____/\\\_______/\\\\\____\///______/\\\\\\\\_____/\\\\\\\\_____________/\\\_________________/\\\\\_______/\\\\\__/\\\\\______/\\\\\__/\\\\\____/\\\\\\\\\_____/\\/\\\\\\__________\/\\\______/\\\\\\\\___/\\/\\\\\\\__     
    ___\//\\\__/\\\______/\\\///\\\___/\\\___/\\\//////____/\\\/////\\\___________\/\\\_______________/\\\///\\\___/\\\///\\\\\///\\\__/\\\///\\\\\///\\\_\////////\\\___\/\\\////\\\____/\\\\\\\\\____/\\\/////\\\_\/\\\/////\\\_    
     ____\//\\\/\\\______/\\\__\//\\\_\/\\\__/\\\__________/\\\\\\\\\\\____________\//\\\_____________/\\\__\//\\\_\/\\\_\//\\\__\/\\\_\/\\\_\//\\\__\/\\\___/\\\\\\\\\\__\/\\\__\//\\\__/\\\////\\\___/\\\\\\\\\\\__\/\\\___\///__   
      _____\//\\\\\______\//\\\__/\\\__\/\\\_\//\\\________\//\\///////______________\///\\\__________\//\\\__/\\\__\/\\\__\/\\\__\/\\\_\/\\\__\/\\\__\/\\\__/\\\/////\\\__\/\\\___\/\\\_\/\\\__\/\\\__\//\\///////___\/\\\_________  
       ______\//\\\________\///\\\\\/___\/\\\__\///\\\\\\\\__\//\\\\\\\\\\______________\////\\\\\\\\\__\///\\\\\/___\/\\\__\/\\\__\/\\\_\/\\\__\/\\\__\/\\\_\//\\\\\\\\/\\_\/\\\___\/\\\_\//\\\\\\\/\\__\//\\\\\\\\\\_\/\\\_________ 
        _______\///___________\/////_____\///_____\////////____\//////////__________________\/////////_____\/////_____\///___\///___\///__\///___\///___\///___\////////\//__\///____\///___\///////\//____\//////////__\///__________
        
""")
try:
        with open('dict.json') as f:
                e = json.load(f)
except:
        print("Cant load Json")

choice=1

while(choice!=0):
        print("""\n
>< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >>< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >>< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >>< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >\n
1.Play\n2.View Commands\n3.Edit commands\n4.Restore Original Commands\n5.Add New Voice Commands\n6.Change Language\n0.Quit\n""")
        choice=int(input())
        if choice==1:
                while True:
                        if keyboard.is_pressed('ctrl+q'):
                                break;
                        if keyboard.is_pressed('q'):
                                command=takeCommandHindi()
                                
                                split_command=command.split()
                                try:
                                        takeaction(split_command[0])
                                        command=command.replace(split_command[0],"")
                                        takeaction(command)
                                        print("split command reached")
                                except Exception as er:
                                        print(er)
                                        if(command not in e):
                                                playsound(r'ERROR.mp3')
                                        else:
                                                takeaction(command)
                                        continue
        elif choice==2:
                for item in e:
                        print(item,"==>",e[item])
        elif choice==3:
                print("What command do you want to replace?\n")
                old_command=takeCommandHindi()
                if old_command not in e:
                        print(old_command,"Command does not exists! Please check using View Commands\n")
                else:
                        print("Speak New Command")
                        new_command=takeCommandHindi()
                        f.close()
                        e[new_command]=e.pop(old_command)
                        with open('dict.json', 'w') as f:
                                json.dump(e, f)
                        print("Command Succesfully Changed!\n")
                        f=open('dict.json')
        elif choice==4:
                o={#English
            'move':"f1 f1",
            'follow me':"f1 f2",
            'charge':"f1 f3",
            'advance':"f1 f4",
            'fall back':"f1 f5",
            'stop':"f1 f6",
            'retreat':"f1 f7",
            'line formation':"f2 f1",
            'Shield wall':"f2 f2",
            'loose formation':"f2 f3",
            'circle formation':"f2 f4",
            'square formation':"f2 f5",
            'v formation':"f2 f2",
            'column formation':"f2 f7",
            'scatter':"f2 f8",
            'toggle fire':"f4",
            'toggle mount':"f5",
            'toggle delegation':"f6",
            'face that way':"f7",
            'shield up':"f8",
            'line up':"f1 f9",
            #selection
            'infantry':"1",
            'arrows':"2",
            'cavalry':"3",
            'everyone':"4",
            'group 1':"1",
            'group 2':"2",
            'group 3':"3",
            'group 4':"4",

            
            #Hindi
            '???????????? ??????':"f1 f1",
            '???????????? ????????????':"f1 f2",
            '??????????????????':"f1 f3",
            '?????? ?????? ??????????????????':"f1 f3",
            '????????? ????????????':"f1 f4",
            '????????????':"f1 f5",
            '????????????':"f1 f6",
            '?????????????????????':"f1 f7",
            '???????????? ?????????':"f2 f1",
            '??????????????? ???????????????':"f2 f2",
            '???????????? ?????????':"f2 f3",
            '??????????????? ?????????':"f2 f4",
            '???????????? ?????????':"f2 f5",
            '????????????????????? ?????????':"f2 f2",
            '???????????? ?????????':"f2 f7",
            '?????????????????????':"f2 f8",
            '???????????? ??????????????????':"f4",
            '??????????????? ??????????????????':"f5",
            '???????????????????????????':"f6",
            '?????? ?????????':"f7",
            '???????????????':"f8",
            '?????????????????? ????????????':"f1 f9",
            #selection
            '???????????? ????????????':"1",
            '???????????????????????????':"2",
            '????????????????????????':"3",
            '????????????':"4",
            '??????????????? ????????????':"1",
            '????????????????????? ????????????':"2",
            '??????????????? ????????????':"3",
            '???????????? ????????????':"4",
            }
                f.close()
                with open('dict.json', 'w') as f:
                        json.dump(o, f)
                f=open('dict.json')
        elif choice==5:
                print("Speak New Command\n")
                new_command=takeCommandHindi()
                print("-",new_command.strip(),"-")
                if(new_command in e or new_command == None):
                        print("Command Already Exists!\n")
                else:
                        print('Enter Keys to Record (Eg: " f1 f2 "\n')
                        recorded=input()
                        e[new_command]=recorded
                        with open('dict.json', 'w') as f:
                                json.dump(e, f)
                        
        elif choice==6:
                l=int(input("1.Hindi\n2.English\n"))
                if(l==1):
                        lang='hi-In'
                elif(l==2):
                        lang='en-In'
