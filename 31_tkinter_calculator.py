import tkinter as tk

def calculator_sum():
    try:
        num1=float(first_number.get())
        num2=float(second_number.get())
        result=num1+num2
        result_lable.config(text=f"Result is :{result}")
    except ValueError:
        result_lable.config(text="Please Enter valid number")

# create main window  
window=tk.Tk()
window.title("simple calculator")
window.geometry("450x350")

title_lable=tk.Label(window,text="simple calculator",font=("Arial",16))
title_lable.pack(pady=5)
frame1=tk.Frame(window)
frame1.pack(pady=5)
num1_label=tk.Label(frame1,text="First Number:")
num1_label.pack(side=tk.LEFT)
first_number=tk.Entry(frame1,width=10)
first_number.pack()
# frame 2 
frame2=tk.Frame(window)
frame2.pack(pady=5)
num2_label=tk.Label(frame2,text="second Number:")
num2_label.pack(side=tk.LEFT)
second_number=tk.Entry(frame2,width=10)
second_number.pack()

calculate_button=tk.Button(window,text="Add Numbers",command=calculator_sum)
calculate_button.pack(pady=10)
result_lable=tk.Label(window,text="Result:",font=("Arial",12))
result_lable.pack(pady=10)
def clear_filed():
    first_number.delete(0,tk.END)
    second_number.delete(0,tk.END)
    result_lable.config(text="Result")
clear_button=tk.Button(window,text="clear filed",command=clear_filed)
clear_button.pack(pady=5)
# start the main loop for display GUI 
window.mainloop()