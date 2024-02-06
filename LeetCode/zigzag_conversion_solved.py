import math


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        arr = []
        s_editing = s
        s_result = ""
        zero_string = ""
        number_in_iteration = 0
        index_in_string = 1
        s_temp_full_column = ""
        counter_column = 0
        while(len(s_editing) > 0):
            if number_in_iteration == 0:
                if len(s_editing[0:numRows]) == numRows:
                    arr.append(s_editing[0:numRows])
                    s_editing = s_editing[numRows:len(s)]
                else:
                    for add_zero_to_full_column in range(
                        0, numRows - len(s_editing[0:numRows])):
                        s_temp_full_column += "0"
                    arr.append(s_editing[0:numRows]+s_temp_full_column)
                    s_temp_full_column = ""
                    s_editing = ""
            else:
                for add_zero in range(0, numRows):
                    if index_in_string != numRows-counter_column:
                        zero_string += "0"
                        index_in_string +=1
                    else:
                        zero_string += s_editing[0:1]
                        index_in_string += 1
                arr.append(zero_string)
                s_editing = s_editing[1:len(s)]
                zero_string = ""
            counter_column += 1
            number_in_iteration += 1
            index_in_string = 1
            if number_in_iteration == numRows - 1 or numRows == 1:
                number_in_iteration = 0
                index_in_string = 1
                counter_column = 0

        ind = 0
        while(ind != numRows):
            for string_element in arr:
                if string_element[ind] != "0":
                    s_result += string_element[ind]
            ind += 1

        return s_result


solution = Solution()
print(
    solution.convert(
        "AB", 1)
)
