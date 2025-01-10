from tkinter import *
import tkinter.messagebox as msg

from controller.person_controller import PersonController


class PersonView:
    def save_click(self):
        status, data = PersonController.save(self.name.get(), self.family.get(),self.age.get())
        if status:
            msg.showinfo("Person Saved", data)
        else:
            msg.showerror("Person Save Error", data)

    def __init__(self):
        self.win = Tk()
        self.win.geometry("300x300")
        self.win.title("Person View")

        # Name
        Label(self.win, text="Name").grid(row=0, column=0)
        self.name = StringVar()
        Entry(self.win, textvariable=self.name).grid(row=0, column=1)

        # Family
        Label(self.win, text="Family").grid(row=1, column=0)
        self.family = StringVar()
        Entry(self.win, textvariable=self.family).grid(row=1, column=1)

        # Age
        Label(self.win, text="Age").grid(row=2, column=0)
        self.age = StringVar()
        Entry(self.win, textvariable=self.age).grid(row=2, column=1)

        Button(self.win, text ="Save", command = self.save_click).grid(row=3, column=0)


        self.win.mainloop()

