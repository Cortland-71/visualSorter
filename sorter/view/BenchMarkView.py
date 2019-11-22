from tkinter import *


class BenchMarkView:
    def __init__(self, driver):
        self.driver = driver
        self.north_bg = "#282828"
        self.elements = []
        self.element_count = 0
        self.min_set = 0
        self.min_actual = 0
        self.max_set = 0
        self.max_actual = 0
        self.bubble_time = 0
        self.quick_time = 0


        self._main_frame()
        self._north_pane()
        self._title_label()

        self._num_elements_label()
        self._num_elements_field()
        self._min_num_label()
        self._min_num_field()
        self._max_num_label()
        self._max_num_field()
        self._back_button()
        self._start_button()

        self._rim_south_pane()
        self._center_pane()
        self._north_in_center_pane()
        self._south_in_center_pane()
        self._algorithms_label()
        self._info_label()

    def _main_frame(self):
        self.main_frame = Frame(self.driver.get_view())
        self.main_frame.pack_forget()
        self.main_frame.configure(bg=self.driver.get_view().get_default_bg())

    def get_frame(self):
        return self.main_frame

    def _north_pane(self):
        self.north_pane = PanedWindow(self.main_frame)
        self.north_pane.pack(fill=BOTH)
        self.north_pane.configure(bg=self.north_bg, height=100)

    def _title_label(self):
        self.title_label = Label(self.north_pane, text="Bench Marks")
        self.title_label.configure(font=f"Futura 20 italic", bg=self.north_bg, fg="#5d8aa8")
        self.title_label.pack(side=LEFT, padx=(20, 0), pady=(20, 20))

    # -------------------------------

    def _num_elements_label(self):
        self.num_elements_label = Label(self.north_pane, text="# of elements")
        self.num_elements_label.configure(font=f"Constantia 10 italic", bg=self.north_bg, fg="#999999")
        self.num_elements_label.pack(side=LEFT, padx=(30, 0), pady=(10, 10))

    def _num_elements_field(self):
        self.num_elements_field = Entry(self.north_pane)
        self.num_elements_field.configure(width= 12,font=f"consolas 12 normal", bg="#454545", fg="white")
        self.num_elements_field.pack(side=LEFT, padx=(5, 10), pady=(10, 10))

    def get_num_elements_entry(self):
        return self.num_elements_field.get()

    # -------------------------------

    def _min_num_label(self):
        self.min_num_label = Label(self.north_pane, text="Min value")
        self.min_num_label.configure(font=f"Constantia 10 italic", bg=self.north_bg, fg="#999999")
        self.min_num_label.pack(side=LEFT, padx=(20, 0), pady=(10, 10))

    def _min_num_field(self):
        self.min_num_field = Entry(self.north_pane)
        self.min_num_field.configure(width= 7,font=f"consolas 12 normal", bg="#454545", fg="white")
        self.min_num_field.pack(side=LEFT, padx=(5, 10), pady=(10, 10))\

    def get_min_num_entry(self):
        return self.min_num_field.get()

    # -------------------------------

    def _max_num_label(self):
        self.max_num_label = Label(self.north_pane, text="Max value")
        self.max_num_label.configure(font=f"Constantia 10 italic", bg=self.north_bg, fg="#999999")
        self.max_num_label.pack(side=LEFT, padx=(20, 0), pady=(10, 10))

    def _max_num_field(self):
        self.max_num_field = Entry(self.north_pane)
        self.max_num_field.configure(width= 7,font=f"consolas 12 normal", bg="#454545", fg="white")
        self.max_num_field.pack(side=LEFT, padx=(5, 10), pady=(10, 10))

    def get_max_num_entry(self):
        return self.max_num_field.get()

    # -------------------------------

    def _start_button(self):
        self.start_button = Button(self.north_pane, text="Start",
                                   command=lambda : self.driver.get_controller().start_bench_mark_button_press())
        self.start_button.configure(width=11, height=1, font=f"Futura 12 normal", bg="#03c03c", fg="white")
        self.start_button.pack(side=RIGHT, padx=(0,20), pady=(0,0))

    def _back_button(self):
        self.back_button = Button(self.north_pane, text="Back",
                       command=lambda : self.driver.get_controller().switch_frame_button_press(
                           self.main_frame, self.driver.get_visual_sort_view().get_frame()))
        self.back_button.configure(width=11, height=1, font=f"Futura 12 normal", bg="#767676", fg="white")
        self.back_button.pack(side=RIGHT, padx=(0,30), pady=(0,0))

    # -------------------------------

    def _rim_south_pane(self):
        self.south_pane = PanedWindow(self.main_frame)
        self.south_pane.pack(fill=BOTH)
        self.south_pane.configure(bg="#000000")

    # South pane
    def _center_pane(self):
        self.center_pane = PanedWindow(self.main_frame)
        self.center_pane.pack(fill=BOTH)
        self.center_pane.configure(bg=self.driver.get_view().get_default_bg())

    def _north_in_center_pane(self):
        self.north_in_center_pane = PanedWindow(self.center_pane)
        self.north_in_center_pane.configure(bg=self.driver.get_view().get_default_bg(), height=300)
        self.north_in_center_pane.pack(fill=BOTH)

    def _algorithms_label(self):
        self.algorithms_label = Label(self.north_in_center_pane, text="Sorting algorithms ---\n"
                                                                      "\tBubble Sort: 00:00:00:00\n"
                                                                      "\tQuick Sort:  00:00:00:00\n"
                                                                      "\tMerge Sort:  00:00:00:00")
        self.algorithms_label.configure(font=f"Consolas 15 normal",
                                        bg=self.driver.get_view().get_default_bg(), fg="orange", justify=LEFT)
        self.algorithms_label.pack(side=LEFT, padx=(150, 0), pady=(100,0))

    def set_time_label(self):
        self.algorithms_label["text"]="Sorting algorithms ---\n"\
                                      f"\tBubble Sort: {self.bubble_time}\n"\
                                      f"\tQuick Sort:  {self.quick_time}\n"\
                                      f"\tMerge Sort:  00:00:00:00"

    def _south_in_center_pane(self):
        self.south_in_center_pane = PanedWindow(self.center_pane)
        self.south_in_center_pane.configure(bg=self.driver.get_view().get_default_bg(), height=300)
        self.south_in_center_pane.pack(fill=BOTH)



    def _info_label(self):
        self.info_label = Label(self.south_in_center_pane, text="Info ---\n"
                                                                "\tData set sample:\n"
                                                                "\tElement count: \n"
                                                                "\tMin set: \n"
                                                                "\tMin actual: \n"
                                                                "\tMax set: \n"
                                                                "\tMax actual: \n"
                                                                "\tBest time: \n"
                                                                "\tAlgorithm:")
        self.info_label.configure(font=f"Consolas 15 normal",
                                       bg=self.driver.get_view().get_default_bg(), fg="orange", justify=LEFT)
        self.info_label.pack(side=LEFT, padx=(150, 0), pady=(50,0))

    def set_info_label(self):
        self.info_label["text"]="Info ---\n"\
            f"\tData set sample: {self.elements[0:8]}\n"\
            f"\tElement count: {self.element_count}\n"\
            f"\tMin set: {self.min_set}\n" \
            f"\tMin actual: {self.min_actual}\n"\
            f"\tMax set: {self.max_set}\n" \
            f"\tMax actual: {self.max_actual}\n"\
            f"\tBest time: \n"\
            f"\tAlgorithm:"

    def set_elements(self, elements):
        self.elements = elements

    def set_element_count(self, element_count):
        self.element_count = element_count

    def set_mins(self, set, actual):
        self.min_set = set
        self.min_actual = actual

    def set_maxs(self, set, actual):
        self.max_set = set
        self.max_actual = actual

    def set_bubble_time(self, time):
        self.bubble_time = time

    def set_quick_time(self, time):
        self.quick_time = time

