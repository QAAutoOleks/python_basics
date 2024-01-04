def create_new_string(given_string1, given_string2):
    mid_string1 = int(len(given_string1) / 2)
    new_string = given_string1[0:mid_string1] + given_string2 + given_string1[mid_string1:]
    return new_string

assert create_new_string("Ault", "Kelly") == "AuKellylt"