name = input("Введіть ім'я користувача  ")
new_name = input("Введіть нове ім'я користувача ")
new_last_name = input("Введіть нове прізвище користувача ")
new_second_name = input("Введіть нове по батькові користувача ")


class User:
# your code goes here
    count_users = 0
    name = ""
    def __init__(self, name):
        self.count_users += 1
        User.count_users += 1
        self.name = name
    def change_username(self, username):
        self.name = self.name.replace(name, username)
    @classmethod
    def get_count(cls):
        print(User.count_users)
    @staticmethod
    def prepare_name(name, last_name, second_name):
        return last_name + " " + name[0] + "." + second_name[0] + "."

new_username = User.prepare_name(new_name, new_last_name, new_second_name)

user1 = User(name)
print(user1.name)
print(User.count_users)
print(user1.count_users)
user1.change_username(new_username)
print(user1.name)

user2 = User(name)
print(User.count_users)
print(user2.count_users)
