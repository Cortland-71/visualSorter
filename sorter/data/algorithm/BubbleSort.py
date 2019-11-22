import time
from threading import Thread

class BubbleSort(Thread):
    def __init__(self, list, driver):
        super().__init__()
        self.driver = driver
        self.unsorted_list = list.copy()
        self.time_before = time.perf_counter()
        self.total_time = 0
        self.start()

    def run(self):
        self.driver.get_bench_mark_view().set_bubble_time("Loading...")
        self.driver.get_bench_mark_view().set_time_label()
        not_sorted = True
        while not_sorted:
            for i in range(len(self.unsorted_list) - 1):
                if self.unsorted_list[i] > self.unsorted_list[i + 1]:
                    holder = self.unsorted_list[i]
                    self.unsorted_list[i] = self.unsorted_list[i + 1]
                    self.unsorted_list[i + 1] = holder
                    not_sorted = True
                    break
                not_sorted = False
        self.total_time = time.perf_counter() - self.time_before
        self.driver.get_bench_mark_view().set_bubble_time(self.total_time)
        self.driver.get_bench_mark_view().set_time_label()






