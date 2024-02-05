import math


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        arr = []
        s_editing = s
        s_result = ""
        number_in_iteration = 0
        while(len(s_editing) > 0):
            if number_in_iteration == 0:
                arr.append(s_editing[0:numRows])
                s_editing = s_editing[numRows:len(s)]
            else:
                arr.append(s_editing[0:1])
                s_editing = s_editing[1:len(s)]
            number_in_iteration += 1
            if number_in_iteration == numRows - 1:
                number_in_iteration = 0

        for i in range(0, len(arr)):
            for j in range(0, len(arr)//numRows):
                s_result += arr[j*numRows][i:i+1]
        
        return arr


solution = Solution()
print(
    solution.convert(
        "PAYPALISHIRING", 3)
)
