class Employee:
    """Creates an instance of Employee"""
    
    def __init__(self, name, annual_salary):
        # instance attributes
        self.name = name
        self.annual_salary = annual_salary
        
    def calculate_monthly_salary(self):
        monthly_salary = self.annual_salary/12
        return monthly_salary
        
class CustomerServiceEmployee(Employee):
    """Creates an instance of CustomerServiceEmployee"""
    def __init__(self, name, annual_salary, department):
        self.department = department
        super().__init__(name, annual_salary)



cs_manager  = CustomerServiceEmployee("Kelly Johnson", 42000, "Customer Service")
kellys_monthly_salary = cs_manager.calculate_monthly_salary()
print(kellys_monthly_salary)
