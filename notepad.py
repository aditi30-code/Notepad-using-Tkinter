from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newfile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)   #1.0 means pheli line ke 0 character p end tk delete

    
def openfile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()
    


def savefile():
    global file
    if file == None:   # when file is new
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":     # when no file is selected
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))
    

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad", "Notepad by Aditi")

root=Tk()
root.title("Untitled - Notepad")
#root.wm_iconbitmap("1.ico")
root.geometry("644x788")

TextArea = Text(root, font="lucida 13")
file = None # jo file khulegi starting m no file
TextArea.pack(expand=True, fill=BOTH)

Menubar=Menu(root)
Filemenu=Menu(Menubar,tearoff=0)
Filemenu.add_command(label="NewFile",command=newfile)
Filemenu.add_command(label="Open",command=openfile)
Filemenu.add_separator()
Filemenu.add_command(label="Save",command=savefile)
Filemenu.add_command(label="Exit",command=quitApp)

Menubar.add_cascade(label="File",menu=Filemenu)

Editmenu=Menu(Menubar,tearoff=0)
Editmenu.add_command(label="Cut",command=cut)
Editmenu.add_command(label="Copy",command=copy)
Editmenu.add_command(label="Paste",command=paste)

Menubar.add_cascade(label="Edit",menu=Editmenu)

HelpMenu = Menu(Menubar, tearoff=0)
HelpMenu.add_command(label = "About Notepad", command=about)

Menubar.add_cascade(label="Help", menu=HelpMenu)
root.config(menu=Menubar)

Scroll = Scrollbar(TextArea)
Scroll.pack(side=RIGHT,  fill=Y)
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)

root.mainloop()
