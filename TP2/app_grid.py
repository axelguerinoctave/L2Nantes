from tkinter import *

fenetre = Tk()
fenetre.title("TP2 pack")
fenetre.geometry("200x200")

label1 = Label(fenetre, text = "LABEL n°1", bg = "blue")
label2 = Label(fenetre, text = "LABEL n°2", bg = "red")
label3 = Label(fenetre, text = "LABEL n°3", bg = "green")
label1.grid(row = 0, column = 0)
label2.grid(row = 1, column = 1)
label3.grid(row = 2, column = 2)
label4 = Label(fenetre, text = "LABEL n°4", bg = "yellow")
label4.grid(row= 0, column = 2)

fenetre.mainloop()