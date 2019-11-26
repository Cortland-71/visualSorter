import time
from threading import Thread

class CocktailSort:
    def visual_cocktail_sort(self, data):
        working_data = data
        n = len(working_data)
        swapped = True
        start = 0
        end = n - 1
        while (swapped == True):

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