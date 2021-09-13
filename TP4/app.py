from tkinter import *

fenetre = Tk()

canvas = Canvas(fenetre, width = 300, height = 200, bg = "ivory")
canvas.pack()

canvas.create_polygon(100, 100, 200, 200, 100, 200)

fenetre.mainloop()