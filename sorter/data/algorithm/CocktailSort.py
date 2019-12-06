
from threading import Thread
import time
class CocktailSort(Thread):
    def __init__(self, list, driver):
        super().__init__()
        self.list = list.copy()
        self.driver = driver
        self.total_time = 0
        self.time_before = time.perf_counter()
        self.start()

    def run(self):
        self.driver.get_bench_mark_view().set_cocktail_time("Loading...")
        self.driver.get_bench_mark_view().set_time_label()
        self.cocktail_sort(self.list)
        self.total_time = time.perf_counter() - self.time_before
        self.driver.get_bench_mark_data().add_time(self.total_time)
        self.driver.get_bench_mark_view().set_cocktail_time(self.total_time)
        self.driver.get_bench_mark_view().set_time_label()
        self.driver.get_controller().update_view()


    def cocktail_sort(self, data):
        working_data = data
        end = len(working_data) - 1
        start = 0
        swapped = True

        while swapped:
            for i in range(start, end):
                self.bubble_condition(working_data, i)
            end -= 1
            swapped = False
            for i in range(end - 1, start - 1, -1):
                self.bubble_condition(working_data, i)
                swapped = True
            start += 1
            if swapped == False:
                break

    def bubble_condition(self, working_data, i):
        if (working_data[i] > working_data[i + 1]):
            holder = working_data[i]
            working_data[i] = working_data[i + 1]
            working_data[i + 1] = holder

