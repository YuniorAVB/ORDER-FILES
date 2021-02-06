from gui.topbar import Topbar


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Order File")

        self.topbar = Topbar(root)
