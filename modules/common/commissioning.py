import  math


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


    def converter_fahrenheit(self, temperature):
        c = 5 * (temperature-32) / 9

        return c


    def circle_area_calculator(self, r):
        s = math.pi * r**2

        return s


    def string_to_int(self, string_variable):
        int_result = abs(int(string_variable))

        return int_result