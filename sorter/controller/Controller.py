import random
from tkinter import *
from sorter.data.algorithm.BubbleSort import *
from sorter.data.algorithm.QuickSort import *
class Controller:
    def __init__(self, driver):
        self.driver = driver

    def start_visual_sort_button_press(self):
        radio_selection = self.driver.get_visual_sort_view().radio_button_index.get()
        self.driver.get_visual_sort_view().set_generate_button_disabled()
        self.driver.get_visual_sort_view().set_start_button_disabled()
        if radio_selection == 0:
            self.driver.get_visual_algorithm().visual_bubble_sort(self.data)
        elif radio_selection == 1:
            self.driver.get_visual_algorithm().visual_quick_sort(self.data, 0, len(self.data)-1)
        self.driver.get_visual_sort_view().set_generate_button_enabled()

    def start_bench_mark_button_press(self):
        self.generate_bench_mark_data()
        BubbleSort(self.driver.get_bench_mark_data().get_working_data(), self.driver)
        QuickSort(self.driver.get_bench_mark_data().get_working_data(), self.driver)

    def generate_button_press(self):
        self.driver.get_visual_sort_view().set_start_button_enabled()
        self.data = self.generate_data(0,500,100)
        self._draw_data(self.data)

    @staticmethod
    def generate_data(min, max, num):
        data = []
        for i in range(num):
            data.append(random.randint(min, max))
        return data

    def _draw_data(self, data):
        self.driver.get_visual_sort_view().canvas.delete('all')
        for i in range(len(data)):
            x = (i + 2) * 10
            self.driver.get_visual_sort_view().canvas.create_line(x, 0, x, data[i],
                                                                fill='#0095b6',
                                                                width=5)

    def switch_frame_button_press(self, frame_to_hide, frame_to_show):
        frame_to_show.pack(fill=BOTH, expand=True)
        frame_to_hide.pack_forget()

    def generate_bench_mark_data(self):
        num_els = self.driver.get_bench_mark_view().get_num_elements_entry()
        min_entry = self.driver.get_bench_mark_view().get_min_num_entry()
        max_entry = self.driver.get_bench_mark_view().get_max_num_entry()
        self.driver.get_bench_mark_data().set_num_elements(num_els)
        self.driver.get_bench_mark_data().set_min_max(min_entry, max_entry)

        self.driver.get_bench_mark_data().generate_working_data()

    def update_view(self):
        self.driver.get_bench_mark_data().set_min_max_actual()
        self.driver.get_bench_mark_view().set_elements(self.driver.get_bench_mark_data().get_working_data())
        self.driver.get_bench_mark_view().set_mins(self.driver.get_bench_mark_data().get_min_set(),
                                                   self.driver.get_bench_mark_data().get_min_actual())
        self.driver.get_bench_mark_view().set_maxs(self.driver.get_bench_mark_data().get_max_set(),
                                                   self.driver.get_bench_mark_data().get_max_actual())
        self.driver.get_bench_mark_view().set_info_label()




