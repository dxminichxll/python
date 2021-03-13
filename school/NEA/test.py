# # import tkinter as tk
# #
# # class MainApplication(tk.Frame):
# #     def __init__(self, parent, *args, **kwargs):
# #         tk.Frame.__init__(self, parent, *args, **kwargs)
# #         self.parent = parent
# #
# #
# # if __name__ == "__main__":
# #     root = tk.Tk()
# #     MainApplication(root).pack(side="top", fill="both", expand=True)
# #     root.mainloop()
#
# import tkinter as tk
#
# class GUI(tk.Frame):
#     def __init__(self, master):
#         # tk.Frame.__init__(self, parent, *awgs, **kwargs)
#         tk.Frame.__init__(self)
#         self.master = master
#         self.master.title("Dice game")
#         self.master.geometry('640x480-8-200')
#         self.frame = tk.Frame(self.master)
#
# class userAuthentification(GUI):
#     def __init__(self, master):
#         # self.frame = tk.Frame(self.master)
#         GUI.__init__(self, master)
#         self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
#         self.button1.pack()
#         self.frame.pack()
#     def new_window(self):
#         self.newWindow = tk.Toplevel(self.master)
#         self.app = Demo2(self.newWindow)
#
#
# class Demo2:
#     def __init__(self, master):
#         self.master = master
#         self.frame = tk.Frame(self.master)
#         self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
#         self.quitButton.pack()
#         self.frame.pack()
#     def close_windows(self):
#         self.master.destroy()
#
#
# def main():
#     root = tk.Tk()
#     app = userAuthentification(root)
#     root.mainloop()
#
# if __name__ == '__main__':
#     main()


import sqlite3

db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

for row in db.execute("SELECT * FROM users"):
    print(row)
