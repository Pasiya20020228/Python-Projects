import datetime
import tkinter as tk

# create a dictionary to store the birthdays
birthdays = {}

# create a function to add a new birthday to the dictionary
def add_birthday():
    name = name_entry.get()
    date = date_entry.get()
    try:
        # parse the date string and store it as a datetime object
        date_obj = datetime.datetime.strptime(date, '%m/%d/%Y')
        birthdays[name] = date_obj
        status_label.config(text=f"{name}'s birthday added successfully.")
    except ValueError:
        status_label.config(text="Invalid date format. Please use mm/dd/yyyy.")

# create a function to check for upcoming birthdays
def check_birthdays():
    today = datetime.datetime.now().date()
    upcoming = []
    for name, date in birthdays.items():
        if (date.month, date.day) >= (today.month, today.day):
            upcoming.append((name, date))
    if len(upcoming) == 0:
        status_label.config(text="No upcoming birthdays.")
    else:
        msg = "Upcoming birthdays:\n"
        for name, date in upcoming:
            msg += f"{name}: {date.month}/{date.day}\n"
        status_label.config(text=msg)

# create the GUI
root = tk.Tk()
root.title("Birthday Reminder")

name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

date_label = tk.Label(root, text="Date (mm/dd/yyyy):")
date_label.pack()
date_entry = tk.Entry(root)
date_entry.pack()

add_button = tk.Button(root, text="Add Birthday", command=add_birthday)
add_button.pack()

check_button = tk.Button(root, text="Check Upcoming Birthdays", command=check_birthdays)
check_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()