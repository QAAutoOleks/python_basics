def create_new_string(given_string):
    new_string = given_string[0] + given_string[len(given_string) // 2] + given_string[len(given_string) - 1]
    return new_string

print(create_new_string("James"))