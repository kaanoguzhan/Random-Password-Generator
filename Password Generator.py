from time import sleep
import tkFont
from Tkinter import *


class Frame():
    root = Tk()

    def __init__(self):
        self.root.protocol('WM_DELETE_WINDOW', self.exitProgram)
        self.root.wm_title("Random Password Generator")
        self.root.resizable(width=False, height=False)
        self.root.geometry("450x110")

        self.btn_generate = Button(self.root, text='Generate', height=5, width=10, font=tkFont.Font(size=13), command=self.generatePassword)
        self.btn_generate.grid(row=0, column=0, rowspan=2)

        self.lbl_progress = Label(self.root, height=2, width=22, background='black', foreground='yellow', font=tkFont.Font(size=25),  text="Ready")
        self.lbl_progress.grid(row=0, column=1)

        self.txt_password = Text(self.root, height=3, width=22, font=tkFont.Font(size=15))
        self.txt_password.grid(row=1, column=1, columnspan=2)

        self.lbl_strength = Label(self.root, height=2, font=tkFont.Font(size=13), text="Strength")
        self.lbl_strength.place(x=310, y=0)

        self.spn_strength = Spinbox(self.root, width=5, font=tkFont.Font(size=13), values=(8, 16, 32, 64))
        self.spn_strength.place(x=380, y=9)

        self.chb_uppercase = Checkbutton(self.root, text="Use Uppercase", width=15, command=self.switchUppercase)
        self.chb_uppercase.place(x=310, y=35)

        self.chb_number = Checkbutton(self.root, text="Use Numbers  ", width=15, command=self.switchNumbers)
        self.chb_number.place(x=310, y=56)

        self.chb_symbol = Checkbutton(self.root, text="Use Symbols   ", width=15, command=self.switchSymbols)
        self.chb_symbol.place(x=310, y=77)

    def generatePassword(self):
        self.txt_password.insert(INSERT, "Hello")
        self.txt_password.tag_add("start", "1.0", "2.0")
        self.txt_password.tag_config("start", foreground="#228B22", justify="center")

    def switchUppercase(self):
        print 1

    def switchNumbers(self):
        print 1

    def switchSymbols(self):
        print 1

    def exitProgram(self):
        self.root.destroy()

    def run(self):
        self.root.mainloop()


frame = Frame()


frame.run()
