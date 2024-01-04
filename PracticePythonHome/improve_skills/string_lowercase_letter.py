def create_new_string(given_string):
    new_string = ""
    given_string_edit = given_string.upper()
    index = 0
    for i in given_string:
        if i == given_string_edit[index]:
            new_string = new_string + i
            index += 1
        else:
            new_string = i + new_string
            index += 1
    return new_string

assert create_new_string("PyNaTive") == "eviayPNT"

# str1 = "PYnAtivE"
# print('Original String:', str1)
# lower = []
# upper = []
# for char in str1:
#     if char.islower():
#         # add lowercase characters to lower list
#         lower.append(char)
#     else:
#         # add uppercase characters to lower list
#         upper.append(char)

# # Join both list
# sorted_str = ''.join(lower + upper)
# print('Result:', sorted_str)