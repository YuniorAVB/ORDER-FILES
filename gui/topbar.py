from tkinter import Frame, Button, Entry, W


class Topbar:
    def __init__(self, root):
        self.topbar = Frame(root)

        self.topbar.config(border="2", height=50)
        self.topbar.pack(side="top", fill="x", pady=30, padx=30)

        self.caja = Entry(self.topbar)
        self.caja.config(bg="grey", font="Calibri 14 bold")
        self.caja.place(relwidth=0.78, relheight=0.8)

        self.button = Button(self.topbar, text="Buscar Ruta")
        self.button.place(relx=0.8, relwidth=0.2, relheight=0.8)
