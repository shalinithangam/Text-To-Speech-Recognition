## import libraries

from tkinter import *
from gtts import gTTS
from playsound import playsound



################### Initialized window####################

root = Tk()
root.geometry('350x300')
root.resizable(0,0)
root.config(bg = 'white')
root.title('ShaliniThangam - TEXT_TO_SPEECH')


##heading
Label(root, text = 'TEXT TO SPEECH' , font='Serif' , bg ='white').pack()

#label
Label(root, text ='Enter Text', font ='Serif', bg ='white').place(x=20,y=60)


##text variable
Msg = StringVar()


#Entry
entry_field = Entry(root,textvariable =Msg, width ='50')
entry_field.place(x=20 , y=100)


###################define function##############################

def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('shalinithangam.mp3')
    playsound('shalinithangam.mp3')

def Exit():
    root.destroy()

def Reset():
    Msg.set("")

#Button
Button(root, text = "SPEAK" , font = 'Serif', command = Text_to_speech, width =6).place(x=25, y=140)
Button(root,text = 'EXIT',font = 'Serif' , command = Exit, bg = '#7E4D00').place(x=110,y=140)
Button(root, text = 'RESET', font='Serif', command = Reset).place(x=175 , y =140)


#infinite loop to run program
root.mainloop()
