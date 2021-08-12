# 服務登入所有相關作業
from lab.login.Dao import UserDao

class LoginError(Exception):
    def __init__(self, message):
        super.__init__(message)

class LoginService:
    __dao = UserDao()

    def login(self, username, password):
        # 先檢查是否有此人?
        user = self.__dao.find_user(username)
        if user is None:
            e = LoginError('查無此人')
            raise e
            # return False  # 查無此人
        else:
            # 檢查密碼
            if user.password == password:
                print('登入成功')
                return True
            else:
                e = LoginError('登入失敗')
                raise e  # 登入失敗
