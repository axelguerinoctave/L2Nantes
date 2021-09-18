from tkinter import *
from draw import draw

def getParams(): 
    result = {
        "canvas": canvas,
        "function": entry_functiondef.get(),
        "xmin": float(entry_xmin.get()),
        "xmax": float(entry_xmax.get()),
        "ymin": float(entry_ymin.get()),
        "ymax": float(entry_ymax.get())
    }
    return result

window = Tk()

window.title("Trace Fonction")
window.geometry("500x450")

frame_params = Frame(window)
frame_params.place(x = 0, y = 0, width = 500, height = 100)

frame_functiondef = Frame(frame_params)
frame_functiondef.place(x = 0, y = 0, width = 250, height = 100)

label_functiondef = Label(frame_functiondef, text = "f(x) =")
label_functiondef.place(x = 30, y = 35, width = 40, height = 30)

entry_functiondef = Entry(frame_functiondef)
entry_functiondef.insert(0, "sin(x)")
entry_functiondef.place(x = 70, y = 35, width = 150, height = 30)

frame_bounds = Frame(frame_params)
frame_bounds.place(x = 250, y = 0, width = 250, height = 100)

frame_xmin = Frame(frame_bounds)
frame_xmin.place(x = 0, y = 0, width = 125, height = 50)

label_xmin = Label(frame_xmin, text = "xmin =")
label_xmin.place(x = 20, y = 10, width = 40, height = 30)

entry_xmin = Entry(frame_xmin)
entry_xmin.insert(0, "-5")
entry_xmin.place(x = 60, y = 10, width = 40, height = 30)

frame_xmax = Frame(frame_bounds)
frame_xmax.place(x = 0, y = 50, width = 125, height = 50)

label_xmax = Label(frame_xmax, text = "xmax =")
label_xmax.place(x = 20, y = 10, width = 40, height = 30)

entry_xmax = Entry(frame_xmax)
entry_xmax.insert(0, "5")
entry_xmax.place(x = 60, y = 10, width = 40, height = 30)

frame_ymin = Frame(frame_bounds)
frame_ymin.place(x = 125, y = 0, width = 125, height = 50)

label_ymin = Label(frame_ymin, text = "ymin =")
label_ymin.place(x = 20, y = 10, width = 40, height = 30)

entry_ymin = Entry(frame_ymin)
entry_ymin.insert(0, "-5")
entry_ymin.place(x = 60, y = 10, width = 40, height = 30)

frame_ymax = Frame(frame_bounds)
frame_ymax.place(x = 125, y = 50, width = 125, height = 50)

label_ymax = Label(frame_ymax, text = "ymax =")
label_ymax.place(x = 20, y = 10, width = 40, height = 30)

entry_ymax = Entry(frame_ymax)
entry_ymax.insert(0, "5")
entry_ymax.place(x = 60, y = 10, width = 40, height = 30)

frame_button = Frame(window)
frame_button.place(x = 0, y = 100, width = 500, height = 50)

button_tracer = Button(frame_button, text = "Tracer", command = lambda:draw(getParams()))
button_tracer.place(x = 200, y = 10, width = 100, height = 30)

frame_canvas = Frame(window)
frame_canvas.place(x = 0, y = 150, width = 500, height = 300)

canvas = Canvas(frame_canvas, bg = "white")
canvas.place(x = 20, y = 20, width = 460, height = 260)
window.mainloop()