class Employee:
    def __init__(self, salary, name, bond):
        self.salary = salary # Create an instance attribute of name salary ans assign it with salary
        self.name = name
        self.bond = bond

    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The name of the employee is {self. name}. Salary is {self.salary}. The bond is {self.bond} years.")

e1 = Employee(340000, "Krishna",5)
# print(e1.salary)
e1.get_info()