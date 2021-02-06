
from tkinter import *
from gui.app import App

if __name__ == '__main__':
    root = Tk()
    root.geometry("500x600")
    gui_app = App(root)
    root.mainloop()
