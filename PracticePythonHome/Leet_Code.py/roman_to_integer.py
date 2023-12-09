class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }
        output = 0
        if len(s) == 1:
            output = dict[s[0]]
        else:
            for i in range(0, len(s)):
                if i == 0:
                    output += dict[s[0]]
                elif s[i - 1: i + 1] in dict:
                    output += dict[s[i - 1 : i + 1]] - dict[s[i - 1]]
                else:
                    output += dict[s[i]]
        return output


solution = Solution()
print(solution.romanToInt("LVIII"))
