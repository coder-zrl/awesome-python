import tkinter as Tkinter
root = Tkinter.Tk()
photo = Tkinter.PhotoImage(file = "path/to/image.gif")
label = Tkinter.Label(image = photo)
label.pack()
root.mainloop()