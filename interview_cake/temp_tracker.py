class TempTracker(object):
    def __init__(self):
        self.freq_list = [0] * 111
        self.total = 0.0
        self.num_records = 0
        self.min_t = 0
        self.max_t = 0
        self.mode = -1
        self.max_occurrences = 0

    def get_max(self):
        return self.max_t

    def get_min(self):
        return self.min_t

    def get_mean(self):
        return self.total / self.num_records

    def get_mode(self):
        return self.mode

    def insert(self, new_temp):
        self.freq_list[new_temp] += 1
        self.total += new_temp
        self.num_records += 1

        if new_temp < self.min_t:
            self.min_t = new_temp

        if new_temp > self.max_t:
            self.max_t = new_temp

        if self.freq_list[new_temp] > self.max_occurrences:
            self.max_occurrences = self.freq_list[new_temp]
            self.mode = new_temp
