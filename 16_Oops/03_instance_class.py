class Employee:
    company = "Apple"  #This is class attribute
    def __init__(self, salary, name, bond,company):
        self.salary = salary # Create an instance attribute of name salary ans assign it with salary
        self.name = name
        self.bond = bond
        self.company = company

    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The name of the employee is {self. name}. Salary is {self.salary}. The bond is {self.bond} years.")

e1 = Employee(3400,"Krishna",3,"Google")
print(e1.company) #will always print instance attribute whenever present
print(Employee.company) # This will always print class attribute

# Object Introspection
print(dir(e1))