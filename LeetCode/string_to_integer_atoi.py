class Solution(object):
    def myAtoi(self, s):
        str_finish = ""
        is_minus = False
        for symbol in s:
            if symbol.isnumeric():
                str_finish += symbol
            if symbol == "-":
                is_minus = True
        if is_minus == True:
            str_finish = "-" + str_finish
        
        return int(str_finish)


solution = Solution()
print(solution.myAtoi("   -42"))