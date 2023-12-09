class Solution(object):
    def longestCommonPrefix(self, strs):
        first_one = ""
        flag = True
        index = 0
        while flag:
            for i in strs:
                if len(i) != 0 and len(i) > index:
                    first_one += i[index]
                else:
                    flag = False
                    break
            index += 1
        first_two = first_one[0: ((index - 1) * len(strs))]
        output = ""
        for i in range(0, len(first_two), len(strs)):
            flag2 = False
            for j in range(i + 1, i + len(strs)):
                if first_two[j] != first_two[i]:
                    flag2 = True
                    break
            if not flag2:
                output += first_two[i]
            else:
                break

        return output


solution = Solution()
print(solution.longestCommonPrefix(["cir", "car"]))