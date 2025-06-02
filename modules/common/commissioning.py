class Commissioning:


    def addition(self):
        a = 1
        return a


    def make_string(self, a, b):
        string_sum = a + b

        return string_sum


    def divisible_by_5_and_7(self, number_1):
        incr = 0
        for i in range(1, number_1):
            if i % 7 == 0 and i % 5 == 0:
                incr += 1
        return incr