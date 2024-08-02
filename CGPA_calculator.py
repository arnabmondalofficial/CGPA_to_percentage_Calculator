import tkinter
import ast
from tkinter import *

root = Tk()
root.title("CGPA to Percentage Calculator")
root.geometry("600x600+100+200")
root.resizable(False, False)
root.configure(bg="#17161b")

equation=""

def show(value):
    global equation
    equation+=value
    result.config(text=equation)

def clear():
    global equation
    equation = ""
    result.config(text=equation)


def calculate():
    global equation
    try:
        num = float(equation)
        product = num * 9.5
    except ValueError:
        product = "error"
    except:
        product = "error"
    result.config(text=product)
    equation = ""


result = Label(root, width=25, height=2, font=("times new roman", 34))
result.pack()

Button(root, text="7", width=5, height=1, font=("arial",30, "bold"), bd=1, fg="#2a2d36", command=lambda:show("7")).place(x=50, y=125)
Button(root, text="8", width=5, height=1, font=("arial",30, "bold"), bd=1, fg="#2a2d36", command=lambda:show("8")).place(x=185, y=125)
Button(root, text="9", width=5, height=1, font=("arial",30, "bold"), bd=1, fg="#2a2d36", command=lambda:show("9")).place(x=320, y=125)

Button(root, text="4", width=5, height=1, font=("arial",30, "bold"), bd=1, fg="#2a2d36", command=lambda:show("4")).place(x=50, y=225)
Button(root, text="5", width=5, height=1, font=("arial",30, "bold"), bd=1, fg="#2a2d36", command=lambda:show("5")).place(x=185, y=225)
Button(root, text="6", width=5, height=1, font=("arial",30, "bold"), bd=1, fg="#2a2d36", command=lambda:show("6")).place(x=320, y=225)

Button(root, text="1", width=5, height=1, font=("arial",30, "bold"), bd=1, fg="#2a2d36", command=lambda:show("1")).place(x=50, y=325)
Button(root, text="2", width=5, height=1, font=("arial",30, "bold"), bd=1, fg="#2a2d36", command=lambda:show("2")).place(x=185, y=325)
Button(root, text="3", width=5, height=1, font=("arial",30, "bold"), bd=1, fg="#2a2d36", command=lambda:show("3")).place(x=320, y=325)
Button(root, text="0", width=4, height=1, font=("arial",30, "bold"), bd=1, fg="#2a2d36", command=lambda:show("0")).place(x=455, y=325)

Button(root, text=".", width=4, height=3, font=("arial",30, "bold"), bd=1, fg="#2a2d36", command=lambda:show(".")).place(x=455, y=125)

Button(root, text="Clear", width=6, height=1, font=("arial",30, "bold"), bd=1, fg="#2a2d36", command=lambda : clear()).place(x=405, y=425)

Button(root, text="Calculate", width=11, height=2, font=("arial",30, "bold"), bd=1, fg="#2a2d36", command=lambda : calculate()).place(x=50, y=425)

root.mainloop()