from tkinter import Tk, Label, Button


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

        self.button_search = ButtonSeach(master)

    def greet(self):
        print("Greetings!")


class ButtonSeach:
    def __init__(self, master):
        self.button = Button(master, text="BUTTON SEACRH")
        self.button.pack()


root = Tk()
root.geometry("400x400")
my_gui = MyFirstGUI(root)
root.mainloop()
