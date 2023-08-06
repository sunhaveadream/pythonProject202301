import tkinter as tk


class Browser:
    def __init__(self, master):
        self.master = master
        master.title("大学成绩管理系统")


root = tk.Tk()
browser = Browser(root)
root.mainloop()