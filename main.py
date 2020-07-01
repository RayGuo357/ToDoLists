import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.label = []
        self.pack()
        self.master.title("To-Do List Application")
        self.master.minsize(1000, 400)
        self.master.maxsize(1000, 400)
        self.create_widgets()

    def create_widgets(self):
        self.rFrame = tk.Frame()
        self.rFrame["borderwidth"] = 2
        self.rFrame["relief"] = "sunken"
        self.rFrame.pack(side="right")

        self.create = tk.Button(self.rFrame)
        self.create["text"] = "Create Task"
        self.create["command"] = self.createTask
        self.create.pack()

        self.pop = tk.Button(self.rFrame)
        self.pop["text"] = "Pop Task"
        self.pop["command"] = self.deleteTask
        self.pop.pack()

        self.lFrame = tk.Frame()
        self.lFrame["borderwidth"] = 2
        self.lFrame["relief"] = "sunken"
        self.lFrame.pack(side="left")

        self.master.update() # needed to update winfo_height()
        # self.frame["height"] = self.master.winfo_height()

    def createTask(self):
        self.label.append(tk.Checkbutton(self.lFrame))
        self.label[len(self.label) - 1]["text"] = str(len(self.label) - 1)
        self.label[len(self.label) - 1].pack()
        self.dynHeight()

    def deleteTask(self):
        self.label[len(self.label) - 1].destroy()
        del self.label[len(self.label) - 1]
        self.dynHeight()

    def dynHeight(self):
        for x in self.label:
            x["height"] = int(round(20 / len(self.label)))


root = tk.Tk()
app = Application(master=root)
app.mainloop()
