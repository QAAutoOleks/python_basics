class Solution(object):
    def reverse(self, x):

        string_a = ""
        x_abs = abs(x)
        string_x = str(x_abs)

        i = 0

        for a in range(len(string_x)-1, 0, -1):
            if string_x[a] == 0:
                i += 1
            else:
                break
        string_x = string_x[0:len(string_x)-i]

        for a in string_x:
            string_a = a + string_a
        if x < 0:
            string_a = "-" + string_a

        if int(string_a) > pow(2, 31)-1 or int(string_a) < pow(-2, 31):
            return 0
        else: return int(string_a)


solution = Solution()
print(solution.reverse(1230))