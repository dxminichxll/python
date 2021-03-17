import tkinter as tk

root = tk.Tk()

image1 = tk.PhotoImage(file="images/dice1.jpg")
image2 = tk.PhotoImage(file="images/dice1.jpg")

label = tk.Label(root, image=image1)
label._image_ref = image1

foo = root.call(label.cget('image'), 'cget', '-file')
bar = image2['file']
print(foo)
