import time

class VisualAlgorithms:

    def __init__(self, driver):
        self.driver = driver
        self.held_data = []
        self.started = True

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
                    break
                not_sorted = False
            self.driver.get_view().update()
            time.sleep(.01)
            self.driver.get_controller()._draw_data(working_data)



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


    #Cocktail sort

    def visual_cocktail_sort(self, data):
        working_data = data
        n = len(working_data)
        swapped = True
        start = 0
        end = n - 1
        while (swapped == True):

            self.driver.get_view().update()
            time.sleep(.01)
            self.driver.get_controller()._draw_data(working_data)

            swapped = False

            for i in range(start, end):
                if (working_data[i] > working_data[i + 1]):
                    holder = working_data[i]
                    working_data[i] = working_data[i + 1]
                    working_data[i + 1] = holder
                    swapped = True

            if (swapped == False):
                break
            swapped = False
            end = end - 1

            for i in range(end - 1, start - 1, -1):
                if (working_data[i] > working_data[i + 1]):
                    holder = working_data[i]
                    working_data[i] = working_data[i + 1]
                    working_data[i + 1] = holder
                    swapped = True


            start = start + 1


