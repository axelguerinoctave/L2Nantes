from tkinter import *

fenetre = Tk()
fenetre.title("TP1")
fenetre.geometry("200x200")

frame1 = Frame(fenetre, borderwidth = 2, relief = GROOVE)
frame1.pack(side = TOP, padx = 5, pady = 5)

label = Label(frame1, text = "Hello World !", bg = "white")
label.pack()

frame2 = Frame(fenetre, borderwidth = 2, relief = GROOVE)
frame2.pack(side = BOTTOM, padx = 5, pady = 5)

bouton = Button(frame2, text = "Fermer", command = fenetre.destroy)
bouton.pack()

fenetre.mainloop()