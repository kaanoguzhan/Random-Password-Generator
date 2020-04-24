from tkinter import Button, Label, Text, Spinbox, Checkbutton, Tk, N, S, E, W, INSERT, END
import tkinter.font as font
from datetime import datetime
import string
import random


class Frame:
    root = Tk()
    global useUppercase, useNumbers, useSymbols, useUNICODE
    useUppercase = True
    useNumbers = True
    useSymbols = True
    useUNICODE = False

    def __init__(self):
        self.root.protocol('WM_DELETE_WINDOW', self.exitProgram)
        self.root.wm_title("Random Password Generator")
        self.root.resizable(width=False, height=False)
        self.root.geometry("535x125")

        self.btn_generate = Button(self.root, text='Generate', width=10, font=font.Font(size=15),
                                   command=self.generatePassword)
        self.btn_generate.grid(row=0, column=0, rowspan=2, sticky=N + S + E + W)

        self.lbl_progress = Label(self.root, text='Ready', height=2, width=23, background='black', foreground='yellow',
                                  font=font.Font(size=15))
        self.lbl_progress.grid(row=0, column=1, sticky=N + S + E + W)

        self.txt_password = Text(self.root, height=3, width=23, font=font.Font(size=15))
        self.txt_password.grid(row=1, column=1, columnspan=2, sticky=N + S + E + W)

        self.lbl_strength = Label(self.root, height=2, font=font.Font(size=13), text="Strength")
        self.lbl_strength.place(x=395, y=0)

        self.spn_strength = Spinbox(self.root, width=5, font=font.Font(size=13), values=(20, 32, 64, 128, 256, 2048))
        self.spn_strength.place(x=465, y=9)

        self.chb_uppercase = Checkbutton(self.root, text="Use Uppercase", width=15, command=self.switchUppercase)
        self.chb_uppercase.place(x=395, y=35)
        if useUppercase:
            self.chb_uppercase.select()

        self.chb_number = Checkbutton(self.root, text="Use Numbers  ", width=15, command=self.switchNumbers)
        self.chb_number.place(x=395, y=56)
        if useNumbers:
            self.chb_number.select()

        self.chb_symbol = Checkbutton(self.root, text="Use Symbols   ", width=15, command=self.switchSymbols)
        self.chb_symbol.place(x=395, y=77)
        if useSymbols:
            self.chb_symbol.select()

        self.chb_symbol = Checkbutton(self.root, text="Use UNICODE ", width=15, command=self.switchUNICODE)
        self.chb_symbol.place(x=395, y=98)

    def generatePassword(self):
        self.txt_password.delete(1.0, END)

        chars = string.ascii_lowercase
        if useUppercase:
            chars = chars + string.ascii_uppercase
        if useNumbers:
            chars = chars + string.digits
        if useSymbols:
            chars = chars + string.punctuation
        if useUNICODE:
            chars = chars + get_random_unicodes(100)

        for _ in range(int(self.spn_strength.get())):

            self.txt_password.insert(INSERT, random.choice(chars))
            self.txt_password.tag_add("start", "1.0", END)
            self.txt_password.tag_config("start", foreground="#228B22", justify="center")

        self.root.clipboard_clear()
        self.root.clipboard_append(self.txt_password.get("1.0", END))
        self.lbl_progress["text"] = "Copied to clipboard"
        now = datetime.now()
        print("Password generated at  " + now.strftime(" %d %B %Y - %H:%M:%S:%f"))
        print("================================\n")
        print(self.txt_password.get("1.0", END))
        print("================================\n\n")
        self.lbl_progress["text"] = "Generated at [" + now.strftime("%H:%M:%S:%f")[:12] +"]\n"+ "Copied to clipboard"

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

    def switchUNICODE(self):
        global useUNICODE
        if useUNICODE:
            self.lbl_progress["text"] = "Ready"
            useUNICODE = False
        else:
            self.lbl_progress["text"] = "Ready (Unicodes are risky)"
            useUNICODE = True

    def exitProgram(self):
        self.root.destroy()

    def run(self):
        self.root.mainloop()


def get_random_unicodes(length):
    def get_random_unicode():
        random_unicode = chr(random.randrange(0xFFFD))
        if isprintable(random_unicode):
            return u"".join(random_unicode)
        else:
            return get_random_unicode()
    unicodes = ""
    for _ in range(length):
        unicodes += get_random_unicode()
    print("Unicode String for Random Passoword:", unicodes)
    return unicodes


def isprintable(s):
    import re
    test = re.compile(r'[\u00BF-\uFFFF]')
    exclude_1 = bool(test.search(s))
    exclude_2 = not bool(re.search(r'[\uD800-\uDFFF]', s))
    exclude = exclude_1 & exclude_2
    try:
        print("Unicode Test:", s, "->", exclude_1, exclude_2)
    except Exception as e:
        print("Exception:", e)
    return exclude

frame = Frame()

frame.run()
