from tkinter import *
import tkinter as tk
from tkinter import ttk
from googletrans import Translator
from tkinter import messagebox
import googletrans
import speech_recognition
import googletrans
import speech_recognition
import gtts
import playsound

root = tk.Tk()
root.title("Language Translator")
root.geometry("590x370")

frame1 = Frame(root,width = 590,height = 370,relief = RIDGE,borderwidth = 5, bg = 'thistle3')
frame1.place(x = 0,y=0)

Label(root,text = "Language Translator",font = ("Helvetica 20 bold"),fg = "black",bg = 'thistle3').pack(pady = 10)


def translate():
    lang1 = text_entry1.get("1.0", "end-1c")
    il = auto_select.get()
    cl = choose_language.get()

    if lang1 == "":
        messagebox.showerror("Language Translator","Enter the text to translate!")
    else:
        text_entry2.delete(1.0,"end")
        translat = Translator()
        output = translat.translate(lang1,dest = cl)
        text_entry2.insert("end",output.text)

    def listen():
        lang_code_mapping = {
        'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'
        
        }

        cl = choose_language.get().lower()
        language = lang_code_mapping.get(cl, 'en')  # Default to English if the language is not found

        converted_audio = gtts.gTTS(output.text, lang=language)
        converted_audio.save("play1.mp3")
        playsound.playsound("play1.mp3")

    btn4 = Button(frame1,command = listen,text = "Listen",relief = RAISED, borderwidth = 2, font = ('verdana',10,"bold"), bg = "#248aa2",fg = "white",cursor = "hand2")
    btn4.place(x = 390,y = 300)

def clear():
    text_entry1.delete(1.0,"end")
    text_entry2.delete(1.0,"end")

def speak():
    il = auto_select.get()
    cl = choose_language.get()
    
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        voice = recognizer.listen(source)
        text = recognizer.recognize_google(voice,language = il)
        text_entry1.insert("end",text)
    
a = tk.StringVar()
auto_select = ttk.Combobox(frame1,width = 27, textvariable = a,state = "randomly", font = ("verdana",10,"bold"))

auto_select["values"] = (
                            'afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque', 'belarusian', 'bengali', 'bosnian', 'bulgarian', 'catalan', 'cebuano', 'chichewa', 'chinese (simplified)', 'chinese (traditional)', 'corsican', 'croatian', 'czech', 'danish', 'dutch', 'english', 'esperanto', 'estonian', 'filipino', 'finnish', 'french', 'frisian', 'galician', 'georgian', 'german', 'greek', 'gujarati', 'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hebrew', 'hindi', 'hmong', 'hungarian', 'icelandic', 'igbo', 'indonesian', 'irish', 'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'korean', 'kurdish (kurmanji)', 'kyrgyz', 'lao', 'latin', 'latvian', 'lithuanian', 'luxembourgish', 'macedonian', 'malagasy', 'malay', 'malayalam', 'maltese', 'maori', 'marathi', 'mongolian', 'myanmar (burmese)', 'nepali', 'norwegian', 'odia', 'pashto', 'persian', 'polish', 'portuguese', 'punjabi', 'romanian', 'russian', 'samoan', 'scots gaelic', 'serbian', 'sesotho', 'shona', 'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 'swedish', 'tajik', 'tamil', 'telugu', 'thai', 'turkish', 'ukrainian', 'urdu', 'uyghur', 'uzbek', 'vietnamese', 'welsh', 'xhosa', 'yiddish', 'yoruba', 'zulu'   
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
text_entry1.insert("end","Enter text")
text_entry1.place(x = 10, y = 100)

text_entry2 = Text(frame1,width = 20,height = 7, borderwidth = 5,relief = RIDGE, font = ('verdana',15))
text_entry2.insert("end","Translated text")
text_entry2.place(x = 300,y = 100)

btn1 = Button(frame1,command = translate, text = "Translate",relief = RAISED, borderwidth = 2, font = ('verdana',10,"bold"), bg = "#248aa2",fg = "white",cursor = "hand2")
btn1.place(x = 185,y = 300)

btn2 = Button(frame1,command = clear,text = "Clear",relief = RAISED, borderwidth = 2, font = ('verdana',10,"bold"), bg = "#248aa2",fg = "white",cursor = "hand2")
btn2.place(x = 300,y = 300)

####voice translation##
btn3 = Button(frame1,command = speak,text = "Speak",relief = RAISED, borderwidth = 2, font = ('verdana',10,"bold"), bg = "#248aa2",fg = "white",cursor = "hand2")
btn3.place(x = 100,y = 300)

root.mainloop()

