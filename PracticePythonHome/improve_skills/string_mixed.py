def create_new_string(given_string1, given_string2):
    new_string = ""
    if len(given_string1) <= len(given_string2):
        for i in range(0, len(given_string1)):
            new_string += given_string1[i] + given_string2[len(given_string2) - 1 - i]
        if len(given_string1) < len(given_string2):    
            new_string += given_string2[len(given_string2) - len(given_string1) - 1::-1]
    else:
        for i in range(0, len(given_string2)):
            new_string += given_string2[i] + given_string1[len(given_string1) - 1 - i]
        if len(given_string2) < len(given_string1):  
            new_string += given_string1[len(given_string1) - len(given_string2) - 1::-1]
    return new_string

print(create_new_string("Abc", "Xyz"))
