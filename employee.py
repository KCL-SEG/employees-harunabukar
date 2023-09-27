"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract, salary, comission, hours=0, bonus=0, sold=0):
        self.contract = contract
        self.name = name
        self.salary = salary
        self.comission = comission

        if contract == 'hourly':
            self.hours = hours

        if comission == 'bonus':
            self.bonus = bonus
        elif comission == 'contract':
            self.bonus = bonus
            self.sold = sold
            
        
    def get_pay(self):
        if self.contract == "salary":

            if self.comission == "none":
                return self.salary
            
            elif self.comission == "bonus":
                return self.salary + self.bonus
            
            elif  self.comission == "contract":
                return self.salary +  (self.sold * self.bonus)
            
        elif self.contract == "hourly": 

            if self.comission == "none":
                return self.salary * self.hours
            elif self.comission == "bonus":
                return (self.salary * self.hours) + self.bonus
            
            elif self.comission == "contract":
                return (self.salary * self.hours) + (self.bonus * self.sold)
    
    def __str__(self):
        if self.contract == "salary":

            if self.comission == "none":
                return (f"{self.name} works on a monthly salary of {self.salary}. Their total pay is {self.get_pay()}.")
            
            elif self.comission == "bonus":
                return (f"{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}.")
            
            elif  self.comission == "contract":
                return (f"{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.sold} contract(s) at {self.bonus}/contract. Their total pay is {self.get_pay()}.")

            
        elif self.contract == "hourly":

            if self.comission == "none":
                return (f"{self.name} works on a contract of {self.hours} hours at {self.salary}/hour. Their total pay is {self.get_pay()}.")

            elif self.comission == "bonus":
                return (f"{self.name} works on a contract of {self.hours} hours at {self.salary}/hour and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}.")
            
            elif self.comission == "contract":
                return (f"{self.name} works on a contract of {self.hours} hours at {self.salary}/hour and receives a commission for {self.sold} contract(s) at {self.bonus}/contract. Their total pay is {self.get_pay()}.")


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', "salary", 4000, "none")

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', "hourly", 25, "none", 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', "salary", 3000, "contract", sold = 4, bonus = 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', "hourly", 25, "contract", 150, 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', "salary", 2000, "bonus", bonus = 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', "hourly", 30, "bonus", 120, 600)

