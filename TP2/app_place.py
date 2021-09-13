from tkinter import *

fenetre = Tk()
fenetre.title("TP2 place")
fenetre.geometry("200x200")

label1 = Label(fenetre, text = "LABEL n°1", bg = "blue")
label2 = Label(fenetre, text = "LABEL n°2", bg = "red")
label3 = Label(fenetre, text = "LABEL n°3", bg = "green")
label1.place(x = 20, y = 20, width = 120, height = 25)
label2.place(x = 20, y = 50, width = 120, height = 25)
label3.place(x = 80, y = 80, width = 120, height = 25)

fenetre.mainloop()