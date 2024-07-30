 class Person:
    def __init__(self, Name, Gender, Marital_status, Residence):
                self.Name = Name
                self.Gender = Gender
                self.Marital_status = Marital_status
                self.Residence = Residence
    def salutation(self):
     print("Hello, my name is " + self.Name)

    def fullname(self):
      return self.Name + " " + self.Gender
# ass
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def describe_Employee(self):
        print("Name" + self.name + "i am" + self.age)



class ManagerEmployee(Employee):
    def __init__(self, name, age, salary, gender):
        super().__init__(name, age, salary)
        self.gender = gender

class developerEmployee(Employee):
    def __init__(self, name, age, salary, prog_language):
        super().__init__(name, age, salary, prog_language)
        self.prog_language = prog_language

class Human_resource(Employee):
    def __init__(self, name, age, salary, speciality, background):
        super().__init__(name, age, salary, speciality, background)
        self.speciality = speciality

