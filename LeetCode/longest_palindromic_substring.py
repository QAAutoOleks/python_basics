class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_begin = s
        s2 = s[::-1]
        out_begin = ""
        out_final = ""
        index1 = 0
        index2 = 0
        for j in s:
            for i in s2:
                if i == s[index1]:
                    out_begin += i
                    index1 += 1
                elif i == s[0]:
                    out_begin = i
                    index1 = 1
                else:
                    out_begin = ""
                    index1 = 0
            index1 = 0
            index2 += 1
            s = s_begin[:len(s_begin) - index2:]
            s2 = s[::-1]
            if len(out_final) < len(out_begin):
                out_final = out_begin
            out_begin = ""
            if len(s) == 1:
                break
            elif len(out_final) == len(s_begin):
                break
                index1 = 0

        index2 = 0
        index1 = 0
        s = s_begin
        s2 = s[::-1]
        for j2 in s:
            for i2 in s2:
                if i2 == s[index1]:
                    out_begin += i2
                    index1 += 1
                elif i2 == s[0]:
                    out_begin = i2
                    index1 = 1
                else:
                    out_begin = ""
                    index1 = 0
            index1 = 0
            index2 += 1
            s = s_begin[index2::]
            s2 = s[::-1]
            if len(out_final) < len(out_begin):
                out_final = out_begin
            out_begin = ""
            if len(s) == 1:
                break
            elif len(out_final) == len(s_begin):
                break
        return out_final

sol = Solution()
for i in sol.longestPalindrome("cbbd"):
# for i in sol.longestPalindrome("aacabdkacaa"):
# for i in sol.longestPalindrome("bacabab"):
    print(i, end="")