from threading import Thread
import time
class QuickSort(Thread):
    def __init__(self, list, driver):
        super().__init__()
        self.list = list.copy()
        self.driver = driver
        self.total_time = 0
        self.time_before = time.perf_counter()
        self.start()

    def run(self):
        self.driver.get_bench_mark_view().set_quick_time("Loading...")
        self.driver.get_bench_mark_view().set_time_label()
        self.quick_sort(self.list, 0, len(self.list)-1)
        self.total_time = time.perf_counter() - self.time_before
        self.driver.get_bench_mark_view().set_quick_time(self.total_time)
        self.driver.get_bench_mark_view().set_time_label()


    def quick_sort(self, data, low, high):
        if low < high:
            pivot_index = self.partition(data, low, high)
            self.quick_sort(data, low, pivot_index - 1)
            self.quick_sort(data, pivot_index + 1, high)

    def partition(self, data, low, high):
        pivot = data[high]
        i = (low - 1)
        for j in range(low, high):
            if data[j] < pivot:
                i += 1
                temp = data[i]
                data[i] = data[j]
                data[j] = temp
        temp = data[i + 1]
        data[i + 1] = data[high]
        data[high] = temp
        return i + 1
