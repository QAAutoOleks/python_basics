class Solution(object):
    def myAtoi(self, s):
        str_finish = ""
        variable_for_str_characters = ""
        is_minus = False
        is_plus_before = False
        for symbol in s:
            if symbol == " " and len(str_finish) == 0:
                pass
            elif symbol == "+" and len(str_finish) == 0 and is_minus == False:
                is_plus_before = True
            elif symbol.isnumeric():
                str_finish += symbol
            elif symbol == "-" and is_plus_before == False and len(str_finish) == 0:
                is_minus = True
            else:
                break
        if is_minus == True and len(str_finish) > 0:
            str_finish = "-" + str_finish
        
        if len(str_finish) == 0:
            return 0
        elif int(str_finish) >= 2147483648:
            return 2147483647
        elif int(str_finish) < -2147483648:
            return -2147483648
        else:
            return int(str_finish)

solution = Solution()
print(solution.myAtoi("   +0 123"))