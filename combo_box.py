#call/import tk and ttk library 
import tkinter as tk
from tkinter import ttk


# function for the event to get selected item
def on_select(event):
    
    selected_item = event.widget.get()
    print("Selected item:", selected_item)

#root window 
root = tk.Tk()
root.title("Combobox Example")