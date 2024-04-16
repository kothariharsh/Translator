from tkinter import Frame,Label,Text,Scrollbar,PhotoImage,Button,GROOVE,WORD,END
from tkinter import ttk, messagebox
import googletrans
import textblob
from googletrans import Translator

root = Tk()
root.title("Translator using Google Translate")
root.geometry("1080x400")

def label_change():
    language1 = combo1.get().capitalize()
    language2 = combo2.get().capitalize()
    label1.configure(text=language1)
    label2.configure(text=language2)
    root.after(100, label_change)

def translate_now():
    try:
        text_ = text1.get(1.0, END)
        t1 = Translator()
        trans_text = t1.translate(text_, src = combo1.get(), dest=combo2.get())
        trans_text = trans_text.text

        text2.delete(1.0, END)
        text2.insert(END, trans_text)
    except Exception as e:
        messagebox.showerror("googletrans", "Please Try Again")


language = googletrans.LANGUAGES
language_list = list(language.values())
lang1 = language.keys()

# Sections to be used for Conversion

# Section 1
# Language Selection
combo1 = ttk.Combobox(root, values=language_list,state='r')
combo1.place(x=110, y=20)
combo1.set("ENGLISH")

# Language Label
label1 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="sky blue", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

# Frame for adding the data
df = Frame(root, bg="Black", bd=5)
df.place(x=10, y=120, width=400, height=210)

# Input Text
text1 = Text(df, bg="black", relief=GROOVE, wrap=WORD, font="Robote 20")
text1.place(x=0, y=0, width=430, height=200)

# ScrollBar for large sentences
scrollbar1 = Scrollbar(df)
scrollbar1.pack(side="right", fill="y")
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)


# Section 2
# Language Selection
combo2 = ttk.Combobox(root, values=language_list,state='r')
combo2.place(x=710, y=20)
combo2.set("SELECT LANGUAGE")

# Language Label
label2 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="sky blue", width=18, bd=5, relief=GROOVE)
label2.place(x=600, y=50)

# Frame for adding the data
df = Frame(root, bg="Black", bd=5)
df.place(x=640, y=120, width=400, height=210)

# Input Text
text2 = Text(df, bg="black", relief=GROOVE, wrap=WORD, font="Robote 20")
text2.place(x=0, y=0, width=430, height=200)

# ScrollBar for large sentences
scrollbar2 = Scrollbar(df)
scrollbar2.pack(side="right", fill="y")
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)


# Translate
arrow_image = PhotoImage(file="arrow1.png")
translate = Button(root, image=arrow_image, activebackground="black", cursor="hand1", bd=5, bg='red', width=150, height=150, command=translate_now)
translate.place(x=430 , y=130)

label_change()
root.configure(bg="white")
root.mainloop()