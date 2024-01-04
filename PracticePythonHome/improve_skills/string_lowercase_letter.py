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