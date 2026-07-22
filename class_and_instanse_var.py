# task 4 

class Employee:
    company_name="Digital Dreams" #class variable accessed by every object
    def __init__(self,emp_name):
           
        self.emp_name=emp_name  #instance variable only accessed by called object
        # self.age=age

        company_name="Digital Dreams"

c1=Employee("Rahul")
c1.emp_id=9   
c2=Employee(4,"Ram")
c2.emp_id=19 

print("employee detials")
# Accessing class and instance variable
print(f"1.Name = {c1.emp_name} Emp_ID {c1.emp_id} Company {c1.company_name}")
print(f"2.Name = {c2.emp_name} Emp_ID {c2.emp_id} Company {c2.company_name}")


    