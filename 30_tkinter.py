import tkinter as tk
def say_hello():
    name=name_entry.get()
    if name:
        gretting_label.config(text=f"hello, {name}")
    else:
        gretting_label.config(text="hello world")

# create a window 
window=tk.Tk()
window.title("My Tkinter App")
window.geometry("300x200")
# if you want to not reszie gui use 
window.resizable(False,False)
title_label=tk.Label(window,text="welcome to Tkinter",font=("arial",16))
title_label.pack(pady=10)
name_entry=tk.Entry(window,width=20)
name_entry.pack(pady=10)
hello_button=tk.Button(window,text="hello boy",command=say_hello)
hello_button.pack(pady=20)
gretting_label=tk.Label(window,text="",font=("arial",12))
gretting_label.pack(pady=10)
# start the main loop for display GUI 
window.mainloop()
