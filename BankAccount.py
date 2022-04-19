# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    def __init__(self, id, name, balance):
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    def deposit(self, amount):
        self.__balance += amount 
    def withdraw(self, amount):
        self.__balance -= amount
    #원하는 결과 출력(약속된 메서드, VBA 에서는 ToString()메서드)
    # def __str__(self):
    #     return "{0} , {1} , {2}".format(self.__id, \
    #         self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
account1.withdraw(3000)
# # 개발자 실수
# account1.balance = 15000000000
#print(account1.__balance) # 에러
print(account1._BankAccount__balance) # 정상출력, naming mangling
print(account1)
