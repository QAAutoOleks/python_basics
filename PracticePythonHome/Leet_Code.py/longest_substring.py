class Solution(object):
    def lengthofLongestsubstr(self, s):
        if len(s) == 1:
            return 1
        elif len(s) == 0:
            return 0
        else:
            string_finish = []
            string_return_add = [s[0]]
            for i in s:
                copy = False
                for j in string_return_add:
                    if j == i:
                        copy = True
                        for a in range(0, len(string_return_add)):
                            if string_return_add[0] != i:
                                string_return_add.pop(0)  # del string_return_add[0]
                                if len(string_return_add) == 1:
                                    string_return_add.pop(0)
                                    break
                            else:
                                string_return_add.pop(0)
                                break
                        string_return_add.append(i)
                        break
                    else:
                        copy = False
                if copy == False:
                    string_return_add.append(i)
                    if len(string_finish) <= len(string_return_add):
                        string_finish = string_return_add[:]
            if len(string_finish) == 0:
                return 1
            else:
                return len(string_finish)


solution = Solution()
print(solution.lengthofLongestsubstr("bikdmd"))
