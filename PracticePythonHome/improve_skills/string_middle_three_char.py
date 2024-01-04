def create_new_string(given_string):
    new_string = given_string[(len(given_string) // 2) - 1]
    new_string += given_string[(len(given_string) // 2)]
    new_string += given_string[(len(given_string) // 2) + 1]
    return new_string

print(create_new_string("JhonDipPeta"))