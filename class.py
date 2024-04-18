# class Student:
#     name = "Rashu"

# s1= Student()
# print(s1.name)

#class creation

class employee:
    def putdata(self):
        self.id=int(input("Enter employee ID"))   #property(variables to store the datas
        self.name=input("Enter employee name") 
        self.salary=int(input("Enter salary"))
    

    def display(self):
        print("Employee id:",self.id) #methods
        print("Employee name:",self.name)
        print("Employee id:",self.salary)

#object

a=employee()
a.putdata()
a.display()