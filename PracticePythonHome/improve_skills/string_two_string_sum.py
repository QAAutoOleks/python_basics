def create_new_string(given_string1, given_string2):
    mid_string1 = int(len(given_string1) / 2)
    mid_string2 = int(len(given_string2) / 2)
    new_string = given_string1[0] + given_string2[0]
    new_string += given_string1[mid_string1] + given_string2[mid_string2]
    new_string += given_string1[len(given_string1) - 1] + given_string2[len(given_string2) - 1]
    return new_string


assert create_new_string("America", "Japan") == "AJrpan"