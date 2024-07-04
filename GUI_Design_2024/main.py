import tkinter as tk
from tkinter import ttk
root = tk.Tk()

width, height = 400,400

display_width = root.winfo_screenwidth()
display_height = root.winfo_screenheight()

#calculate center of screen
left = int(display_width/2 - width/2)
top = int(display_height/2 - height/2)

root.geometry(f'{width}x{height}+{left}+{top}') #widthxheight+left+top

root.title("Hello World")

#resizable window
root.resizable(True, False)

root.iconbitmap('images/up_logo.png')

#functions
def button_click_func():
    entry_field_value = entry.get()
    if (entry_field_value != "") :
        label.configure(text="Your Enter Data: " + entry_field_value)
        Add_button.configure(state='disabled')
    else :
        label.configure(text="Empty Data Detected")



def button_clear():
    label.configure(text='Deleted')
    entry.delete(0, tk.END)
    entry.insert(0, "")
    Add_button.configure(state='enabled')

#widgets

#text field - entry
entry = ttk.Entry(root)
entry.pack()

#button
#Old modern button using tk
#button = tk.Button(root, text='Click Me')
#button.pack()

#New modern button using ttk
Add_button = ttk.Button(root, text='Add', command=button_click_func)
Add_button.pack()

Clear_button = ttk.Button(root, text='Clear', command=button_clear)
Clear_button.pack()

#label
label = ttk.Label(root)
label.pack()
label.configure(text='Enter Data into Text Box and Click Add to Show')



root.mainloop()
