import tkinter as tk


# Splits word into a list of characters for the ceasar cipher
def split(word):
    return [char for char in word]


# Generates a key with equal length to the plaintext for the vigenere cipher
def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return key
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return "".join(key)


# All ciphers handled here
def cipher(text, mode):
    cipher_text = []
    # ========== Ceasar cipher ==========
    if mode == "ceasar":
        cipher1 = [char for char in "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
        cipher2 = [char for char in "yzabcdefghijklmnopqrstuvwx YZABCDEFGHIJKLMNOPQRSTUVWX"]
        for char in text:
            cipher_letter = cipher1[cipher2.index(char)]
            cipher_text.append(cipher_letter)
        return "".join(cipher_text)

    # ========== Vernam cipher ==========
    elif mode == "vernam":
        key = "cvwopslweinedvq9fnasdlkfn2"
        answer = ""
        p = 0
        for char in text:
            answer += chr(ord(char) ^ ord(key[p]))
            p += 1
            if p == len(key):
                p = 0
        return answer

    # ========== Vigenere cipher ==========
    else:
        keyword = "DOMHILL"
        key = generateKey(text, keyword)
        for i in range(len(text)):
            x = (ord(text[i]) +
                 ord(key[i])) % 26
            x += ord('A')
            cipher_text.append(chr(x))
        return "".join(cipher_text)


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.plainText = ""
        self.mode = ""

        # ========== Create all graphical widgets ==========

        # Input box
        self.inputBox = tk.Entry(self)
        self.inputBox.pack(side="top")
        # Submit button
        self.submit = tk.Button(self, text="CONVERT", fg="red", command=self.check_box)
        self.submit.pack(side="bottom")

        # Different cipher buttons
        self.vigenere = tk.Button(self, text="Vigenere", fg="black", command=self.check_vigenere)
        self.vigenere.pack(side="bottom")
        self.vernam = tk.Button(self, text="Vernam", fg="black", command=self.check_vernam)
        self.vernam.pack(side="bottom")
        self.ceasar = tk.Button(self, text="Ceasar", fg="black", command=self.check_ceasar)
        self.ceasar.pack(side="bottom")

        # Result and type of cipher in use
        self.resultValue = tk.StringVar()
        self.resultLabel = tk.Label(textvariable=self.resultValue, fg="red")
        self.resultLabel.pack(side="bottom")

        self.modeValue = tk.StringVar()
        self.modeLabel = tk.Label(textvariable=self.modeValue, fg="green")
        self.modeLabel.pack(side="bottom")

    def check_box(self):
        self.plainText = self.inputBox.get()
        try:
            self.resultValue.set(cipher(self.plainText, self.mode))
        except ValueError:
            self.resultValue.set("Numbers not valid")

    # When a mode is clicked, the 'mode' variable is changed here
    def check_vigenere(self):
        self.mode = "vigenere"
        self.modeValue.set(self.mode)

    def check_vernam(self):
        self.mode = "vernam"
        self.modeValue.set(self.mode)

    def check_ceasar(self):
        self.mode = "ceasar"
        self.modeValue.set(self.mode)


root = tk.Tk()
app = Application(master=root)
app.mainloop()
