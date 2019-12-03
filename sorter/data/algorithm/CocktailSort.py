import time
from threading import Thread

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
        end = len(data) -1
        start = 0
        swapped = True

        while (swapped):

            swapped = False

            for i in range(start, end):
                if (data[i] > data[i + 1]):
                    holder = data[i]
                    data[i] = data[i + 1]
                    data[i + 1] = holder
                    swapped = True

            if (swapped == False):
                break
            swapped = False
            end = end - 1

            for i in range(end - 1, start - 1, -1):
                if (data[i] > data[i + 1]):
                    holder = data[i]
                    data[i] = data[i + 1]
                    data[i + 1] = holder
                    swapped = True
            start = start + 1