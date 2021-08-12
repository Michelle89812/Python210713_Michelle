# DAO = Data Access Object
from lab.login.Model import User

class UserDao:
    __users = [
        User('john', '1234'),
        User('mary', '5678')
    ]

    def find_user(self, username):
        for user in self.__users:
            if user.username == username:
                return user
        return None

    def find_add_user(self):
        return self.__users
