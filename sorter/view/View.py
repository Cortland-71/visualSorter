import tkinter as tk


class View(tk.Tk):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.title("Cortland Carrillo Visual Sorter")
        self.geometry("1080x720")
        self.resizable(False, False)
        self.set_app_in_center()

    def set_app_in_center(self):
        w = 1080
        h = 720
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

    @staticmethod
    def get_default_bg():
        return "#333333"