import tkFont
import string
import random
from Tkinter import *


class Frame():
    root = Tk()
    global useUppercase, useNumbers, useSymbols
    useUppercase = True
    useNumbers = True
    useSymbols = False

    def __init__(self):
        self.root.protocol('WM_DELETE_WINDOW', self.exitProgram)
        self.root.wm_title("Random Password Generator")
        self.root.resizable(width=False, height=False)
        self.root.geometry("450x110")

        self.btn_generate = Button(self.root, text='Generate', height=5, width=10, font=tkFont.Font(size=13), command=self.generatePassword)
        self.btn_generate.grid(row=0, column=0, rowspan=2)

        self.lbl_progress = Label(self.root, text='Ready', height=2, width=22, background='black', foreground='yellow', font=tkFont.Font(size=25))
        self.lbl_progress.grid(row=0, column=1)

        self.txt_password = Text(self.root, height=3, width=22, font=tkFont.Font(size=15))
        self.txt_password.grid(row=1, column=1, columnspan=2)

        self.lbl_strength = Label(self.root, height=2, font=tkFont.Font(size=13), text="Strength")
        self.lbl_strength.place(x=310, y=0)

        self.spn_strength = Spinbox(self.root, width=5, font=tkFont.Font(size=13), values=(8, 16, 32, 64))
        self.spn_strength.place(x=380, y=9)

        self.chb_uppercase = Checkbutton(self.root, text="Use Uppercase", width=15, command=self.switchUppercase)
        self.chb_uppercase.place(x=310, y=35)
        self.chb_uppercase.select()

        self.chb_number = Checkbutton(self.root, text="Use Numbers  ", width=15, command=self.switchNumbers)
        self.chb_number.place(x=310, y=56)
        self.chb_number.select()

        self.chb_symbol = Checkbutton(self.root, text="Use Symbols   ", width=15, command=self.switchSymbols)
        self.chb_symbol.place(x=310, y=77)

    def generatePassword(self):
        self.txt_password.delete(1.0, END)

        for _ in range(int(self.spn_strength.get())):
            chars = string.ascii_lowercase
            if useUppercase:
                chars = chars + string.ascii_uppercase
            if useNumbers:
                chars = chars + string.digits
            if useSymbols:
                chars = chars + string.punctuation

            self.txt_password.insert(INSERT, random.choice(chars))
            self.txt_password.tag_add("start", "1.0", END)
            self.txt_password.tag_config("start", foreground="#228B22", justify="center")

        self.root.clipboard_clear()
        self.root.clipboard_append(self.txt_password.get("1.0", END))
        self.lbl_progress["text"] = "Copied to clipboard"

    def switchUppercase(self):
        global useUppercase
        if useUppercase:
            useUppercase = False
        else:
            useUppercase = True

    def switchNumbers(self):
        global useNumbers
        if useNumbers:
            useNumbers = False
        else:
            useNumbers = True

    def switchSymbols(self):
        global useSymbols
        if useSymbols:
            useSymbols = False
        else:
            useSymbols = True

    def exitProgram(self):
        self.root.destroy()

    def run(self):
        self.root.mainloop()


frame = Frame()


frame.run()
