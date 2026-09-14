from tkinter import *

from tkinter import messagebox

window = Tk()

window.title("After-School Routine Checker")

window.geometry("300x300")


def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)


window.bind("<Key>", handle_keypress)


def handle_click(event):
    print("\nThe routine area was clicked!")


routine_area = Button(window, text="Click Routine Area")

routine_area.pack()

routine_area.bind("<Button-1>", handle_click)


def check_task():

    task = entry.get()

    if task == "":
        messagebox.showwarning("Warning", "Please enter a task!")

    else:
        print("Next task: Homework")


entry = Entry(window)

entry.pack()


button = Button(window, text="Check Routine", command=check_task)

button.pack()


next_task = Label(window, text="Next task: Homework")

next_task.pack()


window.mainloop()