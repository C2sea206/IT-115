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

#array of items
items = ["item1", "item2", "item3", "item4", "item5"]

#tie array with combo box
combo_box = ttk.Combobox(root, values=items)
combo_box.bind("<<ComboboxSelected>>", on_select)

combo_box.pack()

root.mainloop()


