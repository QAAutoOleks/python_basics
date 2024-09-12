class Solution(object):
    def reverse(self, x):

        string_a = ""
        x_abs = abs(x)
        string_x = str(x_abs)

        for a in string_x:
            string_a = a + string_a
        if x < 0:
            string_a = "-" + string_a

        return string_a


solution = Solution()
print(solution.reverse(123))