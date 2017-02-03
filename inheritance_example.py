# This is an elaborate example of classes using the property of inheritance in python

class Employee:

    raise_amt = 1.04
    no_of_emps = 0
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.no_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)
    def apply_raise(self):
        self.pay = self.pay * self.raise_amt       
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
    @classmethod
    #This is an alternative constructor
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

class Developer(Employee):
     raise_amt = 1.10

     def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang     
    


class Manager(Employee):
     def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

     def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

     def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

     def print_emp(self):
        for emp in self.employees:
            print(">", emp.fullname())

dev1 = Developer("corey", "Schafer", 50000, "Python")
dev2 = Developer("Vansh", "Rox", 60000, "Java")


mgr1 = Manager("Ashley", "Williams", 90000, [dev1])


#print(mgr1.email)
#mgr1.add_emp(dev2)
#mgr1.remove_emp(dev1)
#mgr1.print_emp()

print(issubclass(Developer, Employee)) # issubclass returns a boolean value (true/false) to check if the first argument is a child class of the second argument.
