from gtts import gTTS
import webbrowser
import tkinter as tk

rawText = ""


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        # Create widgets
        self.inputBox = tk.Entry(self)
        self.inputBox.pack(side="top")

        self.submit = tk.Button(self, text="CONVERT", fg="red", command=self.check_box)
        self.submit.pack(side="bottom")

    def check_box(self):
        global rawText
        rawText = self.inputBox.get()
        self.master.destroy()


root = tk.Tk()
app = Application(master=root)
app.mainloop()


class TextToSpeech(object):

    def __init__(self, text):
        self.text = gTTS(text=text, lang='en', slow=False)

    def save(self):
        self.text.save("text-to-speech.mp3")
        webbrowser.open("text-to-speech.mp3")


speech = TextToSpeech(rawText)
speech.save()



