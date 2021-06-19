import os
from tkinter import *
from tkinter.filedialog import  asksaveasfilename, askopenfilename

root = Tk()
root.title("Notepad")
root.geometry("600x700")

textarea = Text(root, font="lucida")
textarea.pack()


def quitapp():
    root.destroy()


def newfile():
    global file
    root.title("untitled- notepad")
    file = None
    textarea.delete(1.0, END)


def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])
        if file == "":
            file = None

        else:
            # Save as a new file
            f = open(file, "w")
            f.write(textarea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(textarea.get(1.0, END))
        f.close()

    



def openfile():
    global file
    file = askopenfilename(defaultextension=".txt", filetype=[("All files", "*.*"), ("Text Document", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + "-Notepad")
        textarea.delete(1.0, END)
        f = open(file, "r")
        textarea.insert(1.0, f.read())
        f.close()


def cut():
    textarea.event_generate(("<<Cut>>"))


def copy():
    textarea.event_generate(("<<Copy>>"))


def paste():
    textarea.event_generate(("<<Paste>>"))


MenuBar = Menu(root)

FileMenu = Menu(MenuBar, tearoff=0)
file = None

FileMenu.add_command(label="new", command=newfile)
FileMenu.add_command(label="open", command=openfile)
FileMenu.add_command(label="save", command=savefile)
FileMenu.add_separator()
FileMenu.add_command(label="exit", command=quitapp)

MenuBar.add_cascade(label="file", menu=FileMenu)

EditMenu = Menu(MenuBar, tearoff=0)
EditMenu.add_command(label="cut", command=cut)
EditMenu.add_command(label="copy", command=copy)
EditMenu.add_command(label="paste", command=paste)
MenuBar.add_cascade(label="edit", menu=EditMenu)

root.config(menu=MenuBar)

root.mainloop()
