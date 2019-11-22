from sorter.controller.Controller import *
from sorter.view.View import *
from sorter.view.BenchMarkView import *
from sorter.view.VisualSortView import *
from sorter.data.BenchMarkData import *
from sorter.data.algorithm.VisualAlgorithms import *


class Driver:
    def __init__(self):
        self.view = View(self)
        self.controller = Controller(self)
        self.visual_sort_view = VisualSortView(self)
        self.bench_mark_view = BenchMarkView(self)
        self.bench_mark_data = BenchMarkData(self)
        self.visual_algorithm = VisualAlgorithms(self)

    def main(self):
        self.view.mainloop()

    def get_view(self):
        return self.view

    def get_controller(self):
        return self.controller

    def get_visual_sort_view(self):
        return self.visual_sort_view

    def get_bench_mark_view(self):
        return self.bench_mark_view

    def get_bench_mark_data(self):
        return self.bench_mark_data

    def get_visual_algorithm(self):
        return self.visual_algorithm


if __name__ == "__main__":
    driver = Driver()
    driver.main()