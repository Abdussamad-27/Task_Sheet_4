# task 4 

class Employee:
    company_name="Digital Dreams" #class variable accessed by every object
    def __init__(self,emp_id,emp_name):
        self.emp_id=emp_id        #instance variable only accessed by called object
        self.emp_name=emp_name

        company_name="Digital Dreams"

c1=Employee(3,"Rahul")
c2=Employee(4,"Ram")

print("employee detials")
# Accessing class and instance variable
print(f"1.Name = {c1.emp_name} Emp_ID {c1.emp_id} Company {c1.company_name}")
print(f"2.Name = {c2.emp_name} Emp_ID {c2.emp_id} Company {c2.company_name}")


    