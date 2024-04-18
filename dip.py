# # from abc import ABC, abstractmethod

# # class Messenger(ABC):
# #     @abstractmethod
# #     def send_message(self, message):
# #         pass

# # class Email(Messenger):
# #     def send_message(self, message):
# #         print(f"Sending email: {message}")

# # class SMS(Messenger):
# #     def send_message(self, message):
# #         print(f"Sending SMS: {message}")


# # 

# class BankAccount:
#     def __init__(self):
#         self.__balance = 0  # Private attribute
    
#     def deposit(self, amount):
#         self.__balance += amount
    
#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insufficient balance.")

#     def get_balance(self):
#         return self.__balance


# class Car:
#     def __init__(self, make, model):
#         self.make = make    # Public attribute
#         self.model = model  

#     def drive(self):
#         print("Car is driving")  

# my_car = Car("Toyota", "Corolla")
# print(my_car.make)   # Output: Toyota
# my_car.drive()       # Output: Car is driving


class Person:
    def __init__(self, name, age):
        self._name = name    # Protected attribute
        self._age = age      # Protected attribute

    def display(self):
        print(f"Name: {self._name}, Age: {self._age}")  

class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number  # Public attribute

student = Student("Alice", 20, "12345")
student.display()           # Output: Name: Alice, Age: 20
print(student._name)        # Output: Alice
print(student.roll_number)  # Output: 12345
