from tkinter import *

fenetre = Tk()
fenetre.title("TP2 pack")
fenetre.geometry("200x200")

label1 = Label(fenetre, text = "LABEL n°1", bg = "blue")
label2 = Label(fenetre, text = "LABEL n°2", bg = "red")
label3 = Label(fenetre, text = "LABEL n°3", bg = "green")
label1.pack(fill = X, padx = 40, pady = 5)
label2.pack(fill = X, padx = 40, pady = 5)
label3.pack(fill = X, padx = 40, pady = 5)

fenetre.mainloop()