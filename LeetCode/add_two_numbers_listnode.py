class Solution(object):
    def addTwoNumbers(self, l1, l2):
        first_number = Solution.list_to_int(self, l1)
        second_number = Solution.list_to_int(self, l2)
        sum_int = first_number + second_number

        return sum_int

    def list_to_int(self, list_input):
        str_return = ""
        for i in list_input:
            str_return += str(i)
        
        return int(str_return)


l1 = [2,4,3]
l2 = [5,6,4]
solution = Solution()
print(solution.addTwoNumbers(l1, l2))