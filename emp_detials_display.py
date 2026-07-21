class employee:
     def display(self,emp_id,emp_name,emp_deprt):
          self.emp_id=emp_id
          self.emp_name=emp_name
          self.emp_deprt=emp_deprt

          print(f"[{self.emp_id}] {self.emp_name} - {self.emp_deprt}")
         
e1=employee()
e2=employee()
e1.display("U15OP","Ram","MEDICAL")
e2.display("U16LK","Rahul","ENGINEERING")