import tkinter as tk
from tkinter import colorchooser

current_x,current_y=0,0
color="black"
pen_size=5
def start_position(event):
    global current_x,current_y
    current_x,current_y=event.x,event.y
def draw_line(event):
    global current_x,current_y
    canvas.create_line(current_x,current_y,event.x,event.y,
                       fill=color,width=pen_size,capstyle=tk.ROUND,smooth=True)
    current_x,current_y=event.x,event.y


def change_color():
    global color
    new_color=colorchooser.askcolor()[1]
    if new_color:
        color=new_color
        color_button.config(bg=color)
def clean_canvas():
    canvas.delete("all")
def change_pen_size(new_size):
    global pen_size
    pen_size=new_size
def set_small_pen():
    change_pen_size(2)
def set_medium_pen():
    change_pen_size(5)
def set_large_pen():
    change_pen_size(10)
window=tk.Tk()
window.title("drawing app")
window.geometry("800x600")

title_label=tk.Label(window,text="drawing app",font=("Arial",16))
title_label.pack(pady=10)

toolbar=tk.Frame(window)
toolbar.pack(fill=tk.X,pady=5)

color_button=tk.Button(toolbar,text="choose color",command=change_color,bg=color)
color_button.pack(side=tk.LEFT,padx=5)
# clear button 
clear_button=tk.Button(toolbar,text="clear canvas",command=clean_canvas)
clear_button.pack(side=tk.LEFT,padx=5)

size_frame=tk.Frame(toolbar)
size_frame.pack(side=tk.LEFT,padx=5)

size_label=tk.Label(size_frame,text="pen size:")
size_label.pack(side=tk.LEFT)

small_button=tk.Button(size_frame,text="small",command=set_small_pen)
small_button.pack(side=tk.LEFT,padx=2)

medium_button=tk.Button(size_frame,text="medium",command=set_medium_pen)
medium_button.pack(side=tk.LEFT,padx=2)

large_button=tk.Button(size_frame,text="Large",command=set_large_pen)
large_button.pack(side=tk.LEFT,padx=2)

canvas=tk.Canvas(window,bg="white")
canvas.pack(fill=tk.BOTH,expand=True,padx=10,pady=10)
## bind mouse event to canvas
canvas.bind("<Button-1>",start_position)  ## this record starting coordinates for drawing
canvas.bind("<B1-Motion>",draw_line) ##this track movment and draw lines 
instruction_lablel=tk.Label(window,text="click and drag to draw",font=("Arial",10))
instruction_lablel.pack(pady=10)

window.mainloop()




