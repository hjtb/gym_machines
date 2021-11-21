from oo_first import ContractDeveloper,DirectDeveloper

class HolidayMixin:
    """
    Mixin to calculate holiday entitlement by years of service.
    """
    def calculate_holidays1(self):
        """
        Returns holidays as an integer
        """
        BASE_HOLIDAY = 200
        bonus = 0
        holidays = BASE_HOLIDAY
        if self.no_of_years < 3:
            bonus = holidays + 1
        elif self.no_of_years <= 5:
            bonus = holidays + 2
        elif self.no_of_years > 5:
            bonus = holidays + 3
        return f'Holidays: {bonus}'

class DirectDeveloper(DirectDeveloper):
    def test(self):
        x = 1
    def calculate_holidays(self):
        """
        Returns holidays as an integer
        """
        BASE_HOLIDAY = 200
        bonus = 0
        holidays = BASE_HOLIDAY
        if self.no_of_years < 3:
            bonus = holidays + 1
        elif self.no_of_years <= 5:
            bonus = holidays + 2
        elif self.no_of_years > 5:
            bonus = holidays + 3
        return f'Holidays: {bonus}'


dev = DirectDeveloper("Eric", "Praline", 2, "python")
# There is no composition relationship here. A DirectDeveloper is an Employee
dev.test()
print(dev.details())
print(dev.calculate_holidays())
print(f'${dev.calculate_salary()}')

contractor = ContractDeveloper("Luigi", "Vercotti", 10, "python", 100000)
# When the contractor details are printed the Contract cost is obtained from ExternalContract class
# There is a composition relationship as contractor has an ExternalContract
# However, an external contract is not an employee
# ExternalContract is an object that could be reused by many other objects. 
print(contractor.details())
# The mixin can also be used
print(contractor.calculate_holidays())

