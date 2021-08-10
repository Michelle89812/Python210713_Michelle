class Account:
    name      = ''  # 公有屬性
    __balance = 0   # 私有屬性


    def saving(self, amount):  # 存款
        if amount > 0:
            self.__balance = self.__balance + amount
            print('存款 $%d 成功' % amount)
        else:
            print('存款 $%d 失敗' % amount)

        self.printBalance()

    def withdraw(self, amount):  # 提款
        if 0 < amount <= self.__balance - amount:
            self.__balance = self.__balance - amount
            print('提款 $%d 成功' % amount)
        else:
            print('提款 $%d 失敗' % amount)
        self.printBalance()

    def printBalance(self):
        print('帳戶餘額 $%d' % self.__balance)
