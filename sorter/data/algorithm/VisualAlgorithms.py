import time

class VisualAlgorithms:

    def __init__(self, driver):
        self.driver = driver

    def visual_bubble_sort(self, data):
        working_data = data
        not_sorted = True
        while not_sorted:
            for i in range(len(working_data) - 1):
                if working_data[i] > working_data[i + 1]:
                    holder = working_data[i]
                    working_data[i] = working_data[i + 1]
                    working_data[i + 1] = holder
                    not_sorted = True
                    self.driver.get_view().update()
                    time.sleep(.01)
                    self.driver.get_controller()._draw_data(working_data)
                    break
                not_sorted = False



    def visual_quick_sort(self, data, low, high):
        working_data = data
        if low < high:
            pivot_index = self.partition(working_data, low, high)
            self.visual_quick_sort(working_data, low, pivot_index - 1)
            self.visual_quick_sort(working_data, pivot_index + 1, high)

    def partition(self, data, low, high):
        pivot = data[high]
        i = (low - 1)
        for j in range(low, high):
            if data[j] < pivot:
                i += 1
                temp = data[i]
                data[i] = data[j]
                data[j] = temp
                self.driver.get_view().update()
                time.sleep(.01)
                self.driver.get_controller()._draw_data(data)
        temp = data[i + 1]
        data[i + 1] = data[high]
        data[high] = temp
        return i + 1