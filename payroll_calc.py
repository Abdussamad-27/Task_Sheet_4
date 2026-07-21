class payroll:
    def calculate_net_salary(self,basic_salary,HRA,DA,deductions):
        self.basic_salary=basic_salary
        self.HRA=HRA
        self.DA=DA
        self.deductions=deductions

        net_salary=self.basic_salary+self.HRA+self.DA-self.deductions
        return net_salary
    
c1=payroll()
basic_salary=float(input("Enter employee saalary : "))
HRA=basic_salary*0.4  #40% hra
da=basic_salary*0.1 #10% da
deductions=basic_salary*0.05  #5% deductions
net_salary=c1.calculate_net_salary(basic_salary,HRA,da,deductions)

print(f"Net salary = {net_salary}")
