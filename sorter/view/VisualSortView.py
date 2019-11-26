from tkinter import *


class VisualSortView():
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.north_bg = "#282828"
        self.radio_button_index = IntVar()
        self._main_frame()
        self._north_pane()
        self._title_label()
        self._generate_button()
        self._sort_radio()
        self._bench_mark_button()
        self._start_button()
        self._rim_south_pane()
        self._south_pane()
        self._canvas()
        self.set_start_button_disabled()
        self.radio_button_index.set(0)

    def _main_frame(self):
        self.main_frame = Frame(self.driver.get_view())
        self.main_frame.pack(fill=BOTH, expand=True)
        self.main_frame.configure(bg=self.driver.get_view().get_default_bg())

    def get_frame(self):
        return self.main_frame

    def _north_pane(self):
        self.north_pane = PanedWindow(self.main_frame)
        self.north_pane.pack(fill=BOTH)
        self.north_pane.configure(bg=self.north_bg, height=100)

    def _title_label(self):
        self.title_label = Label(self.north_pane, text="Visual Sorter")
        self.title_label.configure(font=f"Futura 20 italic", bg=self.north_bg, fg="gray")
        self.title_label.pack(side=LEFT, padx=(20, 0), pady=(20, 20))

    def _generate_button(self):
        self.generate_button = Button(self.north_pane, text="Generate",
                                      command=lambda : self.driver.get_controller().generate_button_press())
        self.generate_button.configure(width=15, height=1, font=f"Futura 12 normal", bg="#0099cc", fg="white")
        self.generate_button.pack(side=LEFT, padx=(30, 20), pady=(20, 20))

    def _sort_radio(self):
        radios = {"Bubble sort": 0,
                  "Quick sort": 1,
                  "Cocktail sort": 2}
        for i in radios.keys():
            self.radio = Radiobutton(self.north_pane, text=i)
            self.radio.configure(var=self.radio_button_index, value=radios[i], width=10, bg=self.north_bg, fg="gray",
                                 font=f"Futura 12 normal")
            self.radio.pack(side=LEFT, padx=(1, 1))

    def _start_button(self):
        self.start_button = Button(self.north_pane, text="Start",
                                   command=lambda : self.driver.get_controller().start_visual_sort_button_press())
        self.start_button.configure(width=11, height=1, font=f"Futura 12 normal", bg="#03c03c", fg="white")
        self.start_button.pack(side=RIGHT, padx=(0, 20), pady=(10, 10))

    def _bench_mark_button(self):
        self.bench_button = Button(self.north_pane, text="Bench Marks",
                                   command=lambda : self.driver.get_controller().switch_frame_button_press(
                                       self.main_frame, self.driver.get_bench_mark_view().get_frame()))
        self.bench_button.configure(width=11, height=1, font=f"Futura 12 normal", bg="#ff3333", fg="white")
        self.bench_button.pack(side=RIGHT, padx=(0, 30), pady=(10, 10))

    def _rim_south_pane(self):
        self.south_pane = PanedWindow(self.main_frame)
        self.south_pane.pack(fill=BOTH)
        self.south_pane.configure(bg="#000000")

    # South pane
    def _south_pane(self):
        self.south_pane = PanedWindow(self.main_frame)
        self.south_pane.pack(fill=BOTH)
        self.south_pane.configure(bg=self.driver.get_view().get_default_bg())

    def _canvas(self):
        self.canvas = Canvas(self.south_pane)
        self.canvas.configure(width= 1035, height=600, bg="#1e1e1e", highlightthickness=0)
        self.canvas.pack(pady=(20,20))

    def set_generate_button_disabled(self):
        self.generate_button["state"] = "disabled"

    def set_generate_button_enabled(self):
        self.generate_button["state"] = "normal"

    def set_start_button_disabled(self):
        self.start_button["state"] = "disabled"

    def set_start_button_enabled(self):
        self.start_button["state"] = "normal"