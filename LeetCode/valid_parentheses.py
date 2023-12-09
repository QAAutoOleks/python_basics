class Solution(object):
    def isValid(self, s):
        if len(s) == 1 or len(s) % 2 != 0:
            return False
        elif len(s) == 0:
            return True
        elif len(s) > 1 and len(s) % 2 == 0:
            index = 0
            a1 = 0
            ind_a1 = []
            a2 = 0
            ind_a2 = []
            b1 = 0
            ind_b1 = []
            b2 = 0
            ind_b2 = []
            c1 = 0
            ind_c1 = []
            c2 = 0
            ind_c2 = []
            for i in s:
                if i == "(":
                    a1 += 1
                    ind_a1.append(index)
                elif i == "{":
                    b1 += 1
                    ind_b1.append(index)
                elif i == "[":
                    c1 += 1
                    ind_c1.append(index)
                elif i == ")":
                    a2 += 1
                    ind_a2.append(index)
                    if a1 < a2 or s[index - 1] == "[" or s[index - 1] == "{" or (b1 != b2 and ind_b1[0] > ind_a1[0] and a1 < 3) or (c1 != c2 and ind_c1[0] > ind_a1[0] and c1 < 2):
                        return False
                elif i == "}":
                    b2 += 1
                    ind_b2.append(index)
                    if b1 < b2 or (ind_b2[0] == 2 and ind_b1[0] == 0) or (a1 != a2 and ind_a1[0] > ind_b1[0] and b1 < 2) or (c1 != c2 and ind_c1[0] > ind_b1[0] and b1 != b2):
                        return False
                elif i == "]":
                    c2 += 1
                    ind_c2.append(index)
                    if c1 < c2 or (c1 == c2 and a1 != a2 and ind_a1[0] > ind_c1[0] and c1 < 3) or (a1 < a2 and ind_a1[0] > ind_c1[0]) or (b1 != b2 and ind_b1[0] > ind_b1[0]):
                        return False
                index += 1
            if a1 != a2 or b1 != b2 or c1 != c2:
                return False
            else:
                return True


solution = Solution()
print(solution.isValid("([([)]])"))