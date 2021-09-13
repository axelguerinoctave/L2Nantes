from tkinter import *

def Calculer1(long, larg):
    surf = long * larg
    label3.config(text = "Surface = {}".format(surf))

def Calculer2(event):
    long = float(entry1.get())
    larg = float(entry2.get())
    surf = long * larg
    label3.config(text = "Surface = {}".format(surf))


fenetre = Tk()
fenetre.title("Calcul Surface")
fenetre.geometry("230x150")

label1 = Label(fenetre, text = "Longueur :")
label1.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = W)

label2 = Label(fenetre, text = "Largeur :")
label2.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = W)

entry1 = Entry(fenetre, bg = "white")
entry1.insert(0, "0.0")
entry1.bind("<Return>", Calculer2)
entry1.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = W+E)

entry2 = Entry(fenetre, bg = "white")
entry2.insert(0, "0.0")
entry2.bind("<Return>", Calculer2)
entry2.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = W+E)

bouton = Button(fenetre, text = "Calculer !", command = lambda:Calculer1(float(entry1.get()), float(entry2.get())))
bouton.grid(row = 2, column = 0, columnspan = 2, padx = 5, pady = 10, sticky = W+E)

label3 = Label(fenetre, text = "Surface = 0", relief = GROOVE)
label3.grid(row = 3, column = 0, columnspan = 2, padx = 5, pady = 10, sticky = W+E)

fenetre.mainloop()