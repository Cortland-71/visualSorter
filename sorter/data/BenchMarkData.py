class BenchMarkData:
    def __init__(self, driver):
        self.driver = driver
        self.num_elements = 0
        self.min_set = 0
        self.max_set = 0
        self.min_actual = 0
        self.max_actual = 0
        self.working_data = []

    def set_num_elements(self, num_elements):
        try:
            num_elements_parsed = int(num_elements)
            if num_elements_parsed > 0:
                self.num_elements = num_elements_parsed
                return
            self.num_elements = 0
        except Exception as e:
            print(e)

    def set_min_max(self, min, max):
        try:
            min_value = int(min); max_value = int(max)
            if min_value < max_value:
                self.min_set = min_value; self.max_set = max_value
                return
            self.min_set = 0; self.max_set = 0
        except Exception as e:
            print(e)

    def set_min_max_actual(self):
        try:
            self.min_actual = min(self.working_data)
            self.max_actual = max(self.working_data)
        except Exception:
            self.min_actual = 0
            self.max_actual = 0

    def generate_working_data(self):
        self.working_data = self.driver.get_controller()\
            .generate_data(self.min_set, self.max_set, self.num_elements)

    def get_working_data(self):
        return self.working_data

    def get_min_set(self):
        return self.min_set

    def get_max_set(self):
        return self.max_set

    def get_min_actual(self):
        return self.min_actual

    def get_max_actual(self):
        return self.max_actual






