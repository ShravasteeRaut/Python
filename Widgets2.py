
from tkinter import *
from datetime import date

root = Tk()

root.title("Workshop Participant Greeting")
root.geometry("500x400")


root.configure(bg="#EAF6FF")

title_lbl = Label(
    root,
    text="Workshop Participant Greeting",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="#072F5F",
    pady=10
)

title_lbl.pack(fill=X)

instruction_lbl = Label(
    root,
    text="Welcome to the Workshop!\n"
         "Please enter your full name below.\n"
         "Then select the checkbox to receive your greeting.",
    font=("Arial", 12),
    fg="#333333",
    bg="#EAF6FF",
    justify=CENTER
)

instruction_lbl.pack(pady=20)

name_lbl = Label(
    root,
    text="Full Name:",
    font=("Arial", 12, "bold"),
    fg="#072F5F",
    bg="#EAF6FF"
)

name_lbl.pack()

name_entry = Entry(
    root,
    font=("Arial", 12),
    width=30
)

name_entry.pack(pady=8)

text_box = Text(
    root,
    height=6,
    width=45,
    font=("Arial", 11),
    wrap=WORD
)

text_box.pack(pady=15)

def display():
    name = name_entry.get()

    text_box.delete("1.0", END)

    if name.strip() == "":
        text_box.insert(
            END,
            "Please enter your full name."
        )
        return

    message = (
        "Hello " + name + "!\n\n"
        "Welcome to the Workshop Participant Greeting Application!\n"
        "We are happy to have you with us.\n\n"
        "Workshop Date: " + str(date.today())
    )

    text_box.insert(END, message)

check_var = IntVar()

check_btn = Checkbutton(
    root,
    text="Show my workshop greeting",
    variable=check_var,
    command=display,
    font=("Arial", 11),
    bg="#EAF6FF",
    fg="#072F5F",
    activebackground="#EAF6FF"
)

check_btn.pack(pady=5)

root.mainloop()
