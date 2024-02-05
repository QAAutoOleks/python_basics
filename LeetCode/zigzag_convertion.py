import math


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        quantity_in_row = 1
        quantity_generous = 0
        quantity_row = numRows
        arr1 = list()
        while len(arr1) < len(s):
            for i in range(0, numRows):
                if quantity_row == numRows:
                    arr1.append(quantity_generous)
                    quantity_generous += 1
                else:
                    if quantity_in_row == quantity_row:
                        arr1.append(quantity_generous)
                        quantity_generous += 1
                        quantity_in_row += 1
                    else:
                        quantity_generous += 1
                        quantity_in_row += 1
            quantity_in_row = 1
            quantity_row -= 1
            if quantity_row <= 1:
                quantity_row = numRows
        y = 0
        z = 0
        array = []
        x = 0
        b = 1
        while z < len(s):
            arr_output = list()
            for i in range(0, numRows):
                if y in arr1 and z < len(s):
                    arr_output.insert(i, s[z])
                    z += 1
                    y += 1
                else:
                    arr_output.append(" ")
                    y += 1
            array.insert(x, arr_output)
            arr_output = list()
            x += 1
            b += 1
        str = ""
        a = 0
        while len(str) < len(s):
            for row in array:
                if a < len(row):
                    if row[a] != " ":
                        str += row[a]
                else:
                    break
            a += 1
        return str


solution = Solution()
print(
    solution.convert(
        "acgvowybplftrgdhcdmqqsazmaucxggaimvykvcbjhxapaktfykvqmwemshjynjjbhhoejpnsoqioadvynqrboxnigzhtkqxrznwjclbrblhbpdcevvgmsvuzuduhvryvgwejkhcltlpiqroomucgsyfmcatxtuuasalcipqdcfnvybjmynsqlaepaanvujxokkruzhxeokzmnkalxsdisiauinseypskalebubfingwbqwonruylcyimnaqnpkyrwctsgadvhbyzynprjnclnkxcmppczpvxsqqarvvawuzwjopsdsfseeuttmxubssvjkxchtcdpbaaspuvjboqfkjaygucaozjyxlfspljrnjlefgqiwinjrnhzjjbyjlygygaorjhguskzaahziwiblpcubeumrvsrbufudocximylpfkzdudojhkmnhyecsyfmfbpudmerkpgrbiuvnkhuxvieuoimmnzsoqotfskpktjlbfjqqsknnuthjbwxoxpepfxuyjmkcvxfagvsaghoccxldvltscziiyciiqsklpsoyniyvsoyumlyjwtcztmjrqrzhlmsaeiarrbplpnfdydpxzrwsfflvyncjzxlfhoya",
        250,
    )
)
