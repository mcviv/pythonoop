from first import Person
from first import Employee
from first import ManagerEmployee
from first import developerEmployee
from first import Human_resource
# Person1= Person("john", "male", "married", "nairobi")
# Person1.salutation()
# print(Person1.fullname())
# print(Person1.Name)
# print(Person1.Gender)
# print(Person1.Marital_status)
# print(Person1.Residence)
# print(f"{Person1.Name}is of Gender: {Person1.Gender} Residence: {Person1.Residence} and marital status{Person1.Marital_status}")
#
# Person2 = Person("mark", "male", "single", "nairobi" )
# Person2.salutation()
# print(Person2.fullname())
# print(Person2.Name)
# print(Person2.Gender)
# print(Person2.Marital_status)
# print(Person2.Residence)
#
# Person3 = Person("moses", "male", "complicated", "moyale" )
# Person3.salutation()
# print(Person3.fullname())
# print(Person3.Name)
# print(Person3.Gender)
# print(Person3.Marital_status)
# print(Person3.Residence)
# # ass
#
# Employee1 = Employee("john", 24, 25000)
# print(Employee1.name)
# print(Employee1.age)
# print(Employee1.salary)
# Employee1.describe_Employee()

ManagerEmployee1 = ManagerEmployee("ann", 23, 10000, "female")
print(ManagerEmployee1.name)
print(ManagerEmployee1.age)
print(ManagerEmployee1.salary)
print(ManagerEmployee1.gender)

developerEmployee1 = (developerEmployee("anna", 20, 3000, "python"))
print(developerEmployee1.name)

Human_resource1 = Human_resource("james", 20, 5000, "guard", "kikuyu")
print(Human_resource1.name)



