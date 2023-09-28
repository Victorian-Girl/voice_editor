import tkinter
from tkinter import *
import pyttsx3


def voice_speed():
    voicespeed = tkinter.Toplevel(root)
    var1 = IntVar()
    voicespeed.title("Voice speed.")
    voicespeed.geometry("300x450+700+250")
    label = tkinter.Label(voicespeed, text="Ajust the speed of the voice.", font=("Helvetica", 15))
    label.pack(pady=10)

    def sel2():
        engine.setProperty("rate", int(var1.get()))
        label.config(command=talk())

    def my_check_button():
        C1 = Checkbutton(voicespeed, text="120", indicatoron=0, variable=var1, selectcolor="light blue",
                         onvalue=120, offvalue=200, height=2, width=10, command=sel2)
        C2 = Checkbutton(voicespeed, text="140", indicatoron=0, variable=var1, selectcolor="light blue",
                         onvalue=140, offvalue=200, height=2, width=10, command=sel2)
        C3 = Checkbutton(voicespeed, text="180", indicatoron=0, variable=var1, selectcolor="light blue",
                         onvalue=180, offvalue=200, height=2, width=10, command=sel2)
        C4 = Checkbutton(voicespeed, text="200", indicatoron=0, variable=var1, selectcolor="light blue",
                         onvalue=200, offvalue=200, height=2, width=10, command=sel2)
        C5 = Checkbutton(voicespeed, text="220", indicatoron=0, variable=var1, selectcolor="light blue",
                         onvalue=220, offvalue=200, height=2, width=10, command=sel2)
        C6 = Checkbutton(voicespeed, text="240", indicatoron=0, variable=var1, selectcolor="light blue",
                         onvalue=240, offvalue=200, height=2, width=10, command=sel2)
        C7 = Checkbutton(voicespeed, text="260", indicatoron=0, variable=var1, selectcolor="light blue",
                         onvalue=260, offvalue=200, height=2, width=10, command=sel2)
        C8 = Checkbutton(voicespeed, text="280", indicatoron=0, variable=var1, selectcolor="light blue",
                         onvalue=280, offvalue=200, height=2, width=10, command=sel2)
        C1.pack()
        C2.pack()
        C3.pack()
        C4.pack()
        C5.pack()
        C6.pack()
        C7.pack()
        C8.pack()

    button = tkinter.Button(voicespeed, text="select", command=my_check_button)
    button.pack(pady=10)

    third_menu = tkinter.Menu(voicespeed)
    files_menu2 = tkinter.Menu(third_menu, tearoff=0)
    files_menu2.add_command(label="Quit", activebackground="red", command=voicespeed.destroy)

    third_menu.add_cascade(label="Files", menu=files_menu2)

    voicespeed.config(menu=third_menu)


def voice_info():
    voiceinfo = tkinter.Toplevel(root)
    var = IntVar()
    voiceinfo.title("Voices available.")
    voiceinfo.geometry("800x400+700+250")
    label = tkinter.Label(voiceinfo, text="Voices on your pc.", font=("Helvetica", 20))
    label.pack(pady=10)

    def sel():

        selection = f"Voice number #{int(var.get())+1} selected"  #Consider #{int(var.get())+1}
        label.config(text=selection, command=talk())
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[int(var.get())].id)

    def voice():

        voices = engine.getProperty("voices")

        for idx, voice in enumerate(voices):
            r1 = Radiobutton(voiceinfo, text=voice.id, variable=var, value=idx, command=sel)
            r1.pack(anchor=W)
        label2 = Label(voiceinfo, text="Select a voice", font=("Helvetica", 20))
        label2.pack(pady=10)

    button = tkinter.Button(voiceinfo, text="Search", command=voice)
    button.pack(pady=10)

    second_menu = tkinter.Menu(voiceinfo)
    files_menu2 = tkinter.Menu(second_menu, tearoff=0)
    files_menu2.add_command(label="Quit", activebackground="red", command=voiceinfo.destroy)

    second_menu.add_cascade(label="Files", menu=files_menu2)

    voiceinfo.config(menu=second_menu)


root = Tk()
engine = pyttsx3.init()
root.title("Voices test for A.I. or Other script")
root.geometry("500x350")


def talk():
    #engine.setProperty("rate", 200)
    engine.say(my_entry.get(1.0, END))
    engine.runAndWait()
    my_entry.delete(1.0, END)


label = Label(root, text="Enter your text here", font=("Helvetica", 18))
label.pack(pady=20)

my_entry = Text(root, height=8, width=40, font=("Helvetica", 15))
my_entry.pack(pady=5)

my_button = Button(root, text="Speak", command=talk)
my_button.pack(pady=20)

mainmenu = tkinter.Menu(root)

files_menu = tkinter.Menu(mainmenu, tearoff=0)
files_menu.add_command(label="Quit", activebackground="red", command=root.quit)

option_menu = tkinter.Menu(mainmenu, tearoff=0)
option_menu.add_command(label="Check voices", command=voice_info)
option_menu.add_command(label="Voices speed", command=voice_speed)

mainmenu.add_cascade(label="Files", menu=files_menu)
mainmenu.add_cascade(label="Voices", menu=option_menu)


root.config(menu=mainmenu)
root.mainloop()
