# class Car:
#     brand ="",
#     model ="",
#     year = 2026
# car1= Car()
# car1.brand="nissan"
# car1.model="gtr"
# car1.year=2025
# print(car1.brand, car1.model, car1.year)


# class Animal :
#     Type =""
#     Espèce=""
#     Couleur =""
# animal1 = Animal()
# animal1.Type="Mammifères"
# animal1.Espèce="Chien"
# animal1.Couleur="noiar"
# animal2 = Animal()
# animal2.Type="Mammifères"
# animal2.Espèce="chat"
# animal2.Couleur="noiar"

# print(animal1.Type , animal1.Espèce , animal1.Couleur)
# print(animal2.Type , animal2.Espèce , animal2.Couleur)

# class Student : 
#     def __init__(self, name , age):
#         self. name =name
#         self.age = age
# ahmed = Student("AHMED" , 20)
# student2 = Student("sami" , 18)

# print(ahmed.name , ahmed.age)
# print(student2.name , student2.age)

# class Car : 
#     def __init__(self, brand , speed):
#         self. brand =brand
#         self.speed=speed

#     def Show_info(self):
#         print(self.brand , self.speed)
# car1 = Car("toyota", 230)
# car1.Show_info()
# car2 = Car("nissan", 250)
# car2.Show_info()



# class Student : 
#     def __init__(self, name , age):
#         self.__name =name
#         self.__age = age
#     def student_info(self):
#         print(self.__name , self.__age)

# S1 = Student("LOTFE" , 22)
# S1.__name="djamel"
# S1.__age=50

# S2 = Student("AMAR" , 19)
# S2.__name="samira"
# S2.__age=18
# S1.student_info()
# S2.student_info()


# class Student : 
#     def __init__(self, age):
#             self.__age = age
#     def get_age(self):
#          return self.__age
#     def set_age(self, age):
#         if age> 0:
#              self.__age = age
        
# s1 = Student(19)
# s1.set_age(19)
# print(s1.__age)





# class BankAccount : 
#      def __init__(self, balonce):
#             self.__balonce = balonce
#      def get_balance(self):
#         return self.__balonce
#      def deposit_balonce(self , deposit):
#         self.__balonce = self.__balonce + deposit
#      def withdraw_balonce(self , withdraw):
#         self.__balonce = self.__balonce - withdraw

# bankaccount1=BankAccount(250)
# bankaccount1.deposit_balonce (750)
# bankaccount1.withdraw_balonce(120)

# print(bankaccount1.get_balance())





