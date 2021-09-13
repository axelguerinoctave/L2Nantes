from tkinter import *

window = Tk()

window.title("Trace Fonction")
window.geometry("500x400")

frame_params = Frame(window)
frame_params.place(x = 0, y = 0, width = 500, height = 100)

frame_functiondef = Frame(frame_params, bg = "yellow")
frame_functiondef.place(x = 0, y = 0, width = 250, height = 100)

frame_bounds = Frame(frame_params)
frame_bounds.place(x = 250, y = 0, width = 250, height = 100)

frame_xmin = Frame(frame_bounds, bg = "red")
frame_xmin.place(x = 0, y = 0, width = 125, height = 50)

frame_xmax = Frame(frame_bounds, bg = "purple")
frame_xmax.place(x = 0, y = 50, width = 125, height = 50)

frame_ymin = Frame(frame_bounds, bg = "black")
frame_ymin.place(x = 125, y = 0, width = 125, height = 50)

frame_ymax = Frame(frame_bounds, bg = "orange")
frame_ymax.place(x = 125, y = 50, width = 125, height = 50)

frame_canvas = Frame(window, bg = "blue")
frame_canvas.place(x = 0, y = 100, width = 500, height = 300)

window.mainloop()