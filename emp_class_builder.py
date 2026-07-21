class employee:
     def display(self,emp_id,emp_name,emp_deprt):
          self.emp_id=emp_id
          self.emp_name=emp_name
          self.emp_deprt=emp_deprt

          print(f"Emp_Id = {self.emp_id} ")
          print(f"Name = {self.emp_name} ")
          print(f"Department = {self.emp_deprt} ")
          print("-"*20)

e1=employee()
e2=employee()
e1.display("U15OP","Ram","HR")
e2.display("U16LK","Rahul","Testing")