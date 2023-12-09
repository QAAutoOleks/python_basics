class Solution(object):
    def isPalindrome(self, x):
        pal = True
        list1 = []
        n2 = x
        a = 1
        if x < 0:
            pal = False
        else:
            while n2 > 9:
                a *= 10
                n2 /= 10
            while a > 0:
                list1.append(int(x // a))
                x %= a
                a = a // 10
            ind = -1
            for i in list1:
                if i != list1[ind]:
                    pal = False
                    break
                ind -= 1
        return pal

solution = Solution()
print(solution.isPalindrome(-12321))