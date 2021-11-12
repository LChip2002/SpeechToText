import collections
from operator import length_hint
import speech_recognition as sr
from tkinter import *
import random


images = ["Screenshot_2.png","download(1).png"]

def speak():
    increment = 1
    r = sr.Recognizer()
    with sr.Microphone() as source:        
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source) #Allows for the microphone to be used
        try:
            textspe = r.recognize_google(audio) #Recognizes the words said
            textspe2 = textspe[increment]
            print(textspe2)
            wordssep = textspe[increment].split() #Splits the spoken sentence into individual words         
            print(wordssep)  
        except:
            print("Sorry could not recognize what you said")

def game(): #Attempted and not finished a basic text rpg using your voice
    print("You have encountered an enemy, what will you do: Kill,Befriend, Run or Flirt")
    speak()
    print("You said:" , wordssep)
    if wordssep == "kill":
        print("You killed the enemy")
    else:
        print("Sorry didn't understand")    


def visualtext(): #Visualizes what you said in a tkinter box with a suprise
    root = Tk()
    label1 = Label(root, text=textspe, font="comic-sans-MS")
    #label1.pack()
    label1.grid(row=0, column=0)
    root.title("Speech")
    root.geometry("450x300")

    backimg = random.randint(0,(len(images)-1))
    #image1 = Image.open(images[backimg])
    img = PhotoImage(file=images[backimg])
    label2 = Label(root,image=img, width=200, height=200)
    label2.grid(row=2, column=0)
    button1 = Button(root, text="Enter Game", command=game)
    button1.grid(row=4, column=0)

    root.mainloop()
    
#Start of the program
eggcount = 0
r = sr.Recognizer()

with sr.Microphone() as source: #Uses the mic to record your voice
    r.adjust_for_ambient_noise(source)
    print("Speak Anything :")
    audio = r.listen(source) #Allows for the microphone to be used
    try:
        textspe = r.recognize_google(audio) #Recognizes the words said 
        print("You said :" , textspe)
        wordssep = textspe.split() #Splits the spoken sentence into individual words
        if "egg" in wordssep:
            eggcount += 1
    except:
        print("Sorry could not recognize what you said")
    
    
    #print(text)
    #print(len(text.split()))

    #for i in range (0, (len(wordssep)) - 1):
    
    
    print("You said egg:" , eggcount)
    visualtext()






    
    

