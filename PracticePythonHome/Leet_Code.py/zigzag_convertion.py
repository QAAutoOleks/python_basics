import math


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        arr_input = Solution.sequences(numRows, s)
        array = []
        x = 0
        b = 1
        for i in range(0, len(s)):
            array.insert(
                x, Solution.create_array(numRows, s, Solution.y, Solution.z, arr_input)
            )
            x += 1
            b += 1
        return Solution.output(array, numRows, s)

    y = 0
    z = 0

    def create_array(numRows, s, y, z, arr_input):
        y = y
        z = z
        arr_output = list()
        for i in range(0, numRows):
            if y in arr_input and z < len(s):
                arr_output.insert(i, s[z])
                z += 1
                Solution.z += 1
                y += 1
                Solution.y += 1
            else:
                arr_output.append(" ")
                y += 1
        Solution.y = y
        Solution.z = z
        return arr_output

    def sequences(numRows, s):
        quantity_in_row = 1
        quantity_generous = 0
        quantity_row = numRows
        arr = list()
        while len(arr) < len(s):
            for i in range(0, numRows):
                if quantity_row == numRows:
                    arr.append(quantity_generous)
                    quantity_generous += 1
                else:
                    if quantity_in_row == quantity_row:
                        arr.append(quantity_generous)
                        quantity_generous += 1
                        quantity_in_row += 1
                    else:
                        quantity_generous += 1
                        quantity_in_row += 1
            quantity_in_row = 1
            quantity_row -= 1
            if quantity_row == 1:
                quantity_row = numRows
        return arr

    def output(array, numRows, s):
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
print(solution.convert("PAYPALISHIRING", 3))