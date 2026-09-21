from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Reading Schedule Planner")
root.configure(bg="light blue")
root.geometry("650x400")

upload = Image.open("app_img_reading.jpg")
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)

label = Label(root, image=image, bg="light blue")
label.place(x=180, y=20)

label1 = Label(root, text="Hey User! Welcome to Reading Schedule Planner", bg="light blue")

label1.place(relx=0.5, y=340, anchor=CENTER)


def msg():
    MsgBox = messagebox.showinfo("Alert", "Do you want to plan your reading schedule?")
    if MsgBox == "ok":
        topwin()


button1 = Button(root, text="Let's get started!", command=msg, bg="brown", fg="white")
button1.place(x=250, y=360)


def topwin():
    top = Toplevel()
    top.title("Reading Schedule Planner")
    top.configure(bg="light grey")
    top.geometry("600x350+50+50")

    label1 = Label(top, text="Enter Total Pages in the Book", bg="light grey")
    entry1 = Entry(top)

    label2 = Label(top, text="Enter Pages to Read Per Day", bg="light grey")
    entry2 = Entry(top)

    lbl = Label(top, text="Reading Schedule Result", bg="light grey")

    l1 = Label(top, text="Complete Reading Days", bg="light grey")
    l2 = Label(top, text="Remaining Pages", bg="light grey")

    t1 = Entry(top)
    t2 = Entry(top)

    def calculator():
        try:
            total_pages = int(entry1.get())
            pages_per_day = int(entry2.get())

            if pages_per_day <= 0:
                messagebox.showerror("Error", "Pages per day must be greater than 0")
                return

            complete_days = total_pages // pages_per_day
            remaining_pages = total_pages % pages_per_day

            t1.delete(0, END)
            t2.delete(0, END)

            t1.insert(END, str(complete_days))
            t2.insert(END, str(remaining_pages))

        except ValueError:
            messagebox.showerror("Error", "Please enter valid whole numbers")

    btn = Button(top, text="Calculate", command=calculator, bg="brown", fg="white")

    label1.place(x=180, y=30)
    entry1.place(x=200, y=60)

    label2.place(x=180, y=90)
    entry2.place(x=200, y=120)

    btn.place(x=240, y=160)

    lbl.place(x=180, y=210)

    l1.place(x=140, y=240)
    t1.place(x=300, y=240)

    l2.place(x=140, y=280)
    t2.place(x=300, y=280)

    top.mainloop()


root.mainloop()