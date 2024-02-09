class Solution(object):
    def addTwoNumbers(self, l1, l2):
        first_number = Solution.list_to_int(self, l1)
        second_number = Solution.list_to_int(self, l2)
        sum_int = first_number + second_number
        sum_list = Solution.int_to_list(self, sum_int)

        return sum_list

    def list_to_int(self, list_input):
        str_return = ""
        for i in list_input:
            str_return += str(i)
        
        return int(str_return)

    def int_to_list(self, int_input):
        int_to_string = str(int_input)
        list_return = []
        for symbol in int_to_string:
            list_return.append(int(symbol))
        
        return list_return



l1 = [2,4,3]
l2 = [5,6,4]
solution = Solution()
print(solution.addTwoNumbers(l1, l2))