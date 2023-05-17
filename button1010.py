#Call on the tkinter library
import tkinter as tk 

#create function that prints when clicks
def button_click():
    print("Button clicked!")

#creates a window sets the title
root = tk.Tk()
root.title("Button Example")

#button widget packed inside the root window
button = tk.Button(root,text="Click Me!",command=button_click)
button.pack()

#starts the main event loop for tkinter
root.mainloop()












