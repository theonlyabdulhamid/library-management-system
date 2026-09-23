# class BankAccount:
#     def __init__(self,owner,balance):
#         self.owner = owner
#         # encapsulation
#         self.__balance= balance

#     def deposit(self,amount):
#         if amount>0:
#             self.__balance += amount
#             return f"Deposited ${amount}. New balance: ${self.__balance}"
#         else:
#             return "Invalid amount"
#     def get_balance(self):
#         return self.__balance
# account=BankAccount("Hamid",4000)
# account.deposit(500)
# print(account.get_balance())

class Animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        return f"{self.name} is eating."
class Cat(Animal):
    def meow(self):
        return f"{self.name} says Meow!"
my_cat=Cat("Whis")
print(my_cat.eat())
print(my_cat.meow())
