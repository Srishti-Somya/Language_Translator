from tkinter import *
import tkinter as tk
from tkinter import ttk
from googletrans import Translator
from tkinter import messagebox
import googletrans
import speech_recognition





root = tk.Tk()
root.title("Language Translator")
root.geometry("590x370")

frame1 = Frame(root,width = 590,height = 370,relief = RIDGE,borderwidth = 5, bg = 'thistle3')
frame1.place(x = 0,y=0)

Label(root,text = "Language Translator",font = ("Helvetica 20 bold"),fg = "black",bg = 'thistle3').pack(pady = 10)


def translate():
    lang1 = text_entry1.get("1.0", "end-1c")
    cl = choose_language.get()

    if lang1 == "":
        messagebox.showerror("Language Translator","Enter the text to translate!")
    else:
        text_entry2.delete(1.0,"end")
        translat = Translator()
        output = translat.translate(lang1,dest = cl)
        text_entry2.insert("end",output.text)

def clear():
    text_entry1.delete(1.0,"end")
    text_entry2.delete(1.0,"end")

a = tk.StringVar()


auto_select = ttk.Combobox(frame1,width = 27, textvariable = a,state = "randomly", font = ("verdana",10,"bold"))

auto_select["values"] = (
                            "Auto Select" ,
                        )
auto_select.place(x = 15, y = 60)
auto_select.current(0)

l = tk.StringVar()
choose_language = ttk.Combobox(frame1, width = 27, textvariable = l, state = 'randomly', font = ("verdana",10,"bold"))

choose_language["values"] = (
                             'afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque', 'belarusian', 'bengali', 'bosnian', 'bulgarian', 'catalan', 'cebuano', 'chichewa', 'chinese (simplified)', 'chinese (traditional)', 'corsican', 'croatian', 'czech', 'danish', 'dutch', 'english', 'esperanto', 'estonian', 'filipino', 'finnish', 'french', 'frisian', 'galician', 'georgian', 'german', 'greek', 'gujarati', 'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hebrew', 'hindi', 'hmong', 'hungarian', 'icelandic', 'igbo', 'indonesian', 'irish', 'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'korean', 'kurdish (kurmanji)', 'kyrgyz', 'lao', 'latin', 'latvian', 'lithuanian', 'luxembourgish', 'macedonian', 'malagasy', 'malay', 'malayalam', 'maltese', 'maori', 'marathi', 'mongolian', 'myanmar (burmese)', 'nepali', 'norwegian', 'odia', 'pashto', 'persian', 'polish', 'portuguese', 'punjabi', 'romanian', 'russian', 'samoan', 'scots gaelic', 'serbian', 'sesotho', 'shona', 'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 'swedish', 'tajik', 'tamil', 'telugu', 'thai', 'turkish', 'ukrainian', 'urdu', 'uyghur', 'uzbek', 'vietnamese', 'welsh', 'xhosa', 'yiddish', 'yoruba', 'zulu'   
                            )
choose_language.place(x = 305, y = 60)
choose_language.current(0)


text_entry1= Text(frame1,width = 20,height = 7, borderwidth = 5, relief = RIDGE, font = ('verdana',15))
text_entry1.place(x = 10, y = 100)

text_entry2 = Text(frame1,width = 20,height = 7, borderwidth = 5,relief = RIDGE, font = ('verdana',15))
text_entry2.place(x = 300,y = 100)

btn1 = Button(frame1,command = translate, text = "Translate",relief = RAISED, borderwidth = 2, font = ('verdana',10,"bold"), bg = "#248aa2",fg = "white",cursor = "hand2")
btn1.place(x = 185,y = 300)

btn2 = Button(frame1,command = clear,text = "Clear",relief = RAISED, borderwidth = 2, font = ('verdana',10,"bold"), bg = "#248aa2",fg = "white",cursor = "hand2")
btn2.place(x = 300,y = 300)


####voice translation##





root.mainloop()
