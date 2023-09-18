# Project 1 
# Title: Calculator app 
# Code author: Jason Christopher
# Description: Simple calculator app 
# Add sin, cos, tan functionalities

# Start of code 

from tkinter import *
expression = ""

gui = Tk()
gui.geometry("280x325")
gui.resizable(0,0)
gui.title("Calculator app")

text_to_display = StringVar()


# Main calculator functions
# Functions here will allow user interaction
def widget_click(input_val):
    global expression
    expression = expression + str(input_val)
    text_to_display.set(expression)

def clear_button():
    global expression
    expression = ""
    text_to_display.set(expression)

def equal_button():
    global expression
    result = str(eval(expression))
    text_to_display.set(result)
    expression = result

def delete_button():
    global expression
    expression = expression[:-1]
    text_to_display.set(expression)


# Main interface code
# The window will be divided into two main sections
# 1. Display frame - User input will be displayed at the top of the window
# 2. Button frame - User input will be received at the lower half of the window

# ---------------------------------------------------------------------------------
# Display frame
display_frame = Frame(gui, width=280, height=200, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
display_frame.pack(side = TOP)

# ---------------------------------------------------------------------------------
# Input field
input_field = Entry(display_frame, font=("serif",18,"bold"), textvariable = text_to_display, width=50, bg="#eee", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)


# ---------------------------------------------------------------------------------
# Buttons frame
button_frame = Frame(gui, width=280, height=340, bg = "grey")
button_frame.pack()

# ---------------------------------------------------------------------------------
# Row 1
button_clear = Button(button_frame, text = "C", fg = "black", width = 9, height = 3, bd = 0, bg = '#fff', cursor = "hand2", command = lambda: clear_button()).grid(row=1, column = 0, padx = 1, pady = 1)
button_del = Button(button_frame, text = "<-", fg = "black", width = 9, height = 3, bd = 0, bg = '#fff', cursor = "hand2", command = lambda: delete_button()).grid(row=1, column = 1, padx = 1, pady = 1)
button_div = Button(button_frame, text = "/", fg = "black", width = 9, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: widget_click("/")).grid(row=1, column = 2, padx = 1, pady = 1)
button_mul = Button(button_frame, text = "x", fg = "black", width = 9, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: widget_click("*")).grid(row=1, column = 3, padx = 1, pady = 1)

# ---------------------------------------------------------------------------------
# Row 2
button_7 = Button(button_frame, text = "7", fg = "black", width = 9, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: widget_click(7)).grid(row=2, column = 0, padx = 1, pady = 1)
button_8 = Button(button_frame, text = "8", fg = "black", width = 9, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: widget_click(8)).grid(row=2, column = 1, padx = 1, pady = 1)
button_9 = Button(button_frame, text = "9", fg = "black", width = 9, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: widget_click(9)).grid(row=2, column = 2, padx = 1, pady = 1)
button_sub = Button(button_frame, text = "-", fg = "black", width = 9, height = 3, bd = 0, bg = '#fff', cursor = "hand2", command = lambda: widget_click('-')).grid(row=2, column = 3, padx = 1, pady = 1)

# ---------------------------------------------------------------------------------
# Row 3
button_4 = Button(button_frame, text = "4", fg = "black", width = 9, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: widget_click(4)).grid(row = 3, column = 0, padx = 1, pady = 1)
button_5 = Button(button_frame, text = "5", fg = "black", width = 9, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: widget_click(5)).grid(row = 3, column = 1, padx = 1, pady = 1)
button_6 = Button(button_frame, text = "6", fg = "black", width = 9, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: widget_click(6)).grid(row = 3, column = 2, padx = 1, pady = 1)
button_add = Button(button_frame, text = "+", fg = "black", width = 9, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: widget_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)


# ---------------------------------------------------------------------------------
# Row 4
button_1 = Button(button_frame, text = "1", fg = "black", width = 9, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: widget_click(1)).grid(row=4, column = 0, padx = 1, pady = 1)
button_2 = Button(button_frame, text = "2", fg = "black", width = 9, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: widget_click(2)).grid(row=4, column = 1, padx = 1, pady = 1)
button_3 = Button(button_frame, text = "3", fg = "black", width = 9, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: widget_click(3)).grid(row=4, column = 2, padx = 1, pady = 1)
button_equal = Button(button_frame, text = "=", fg = "black", width = 9, height = 7, bd = 0, bg = '#fff', cursor = "hand2", command = lambda: equal_button()).grid(row = 4, column = 3, rowspan=3, padx = 1)

# ---------------------------------------------------------------------------------
# Row 5
button_0 = Button(button_frame, text = "0", fg = "black", width = 19, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: widget_click(0)).grid(row = 5, column = 0, columnspan=2, padx = 1, pady = 2)
button_dot = Button(button_frame, text = ".", fg = "black", width = 9, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: widget_click(".")).grid(row = 5, column = 2, padx = 1, pady = 2)


gui.mainloop()

