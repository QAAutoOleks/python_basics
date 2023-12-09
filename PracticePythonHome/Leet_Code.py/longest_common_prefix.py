class Solution(object):
    def longestCommonPrefix(self, strs):
        first = ""
        flag = True
        index = 0
        while flag:
            for i in strs:
                if len(i) != 0 and len(i) > index:
                    first += i[index]
                else:
                    flag = False
                    break
            index += 1
        return first


solution = Solution()
print(solution.longestCommonPrefix(["Pes", "Sobaka", "Cat"]))