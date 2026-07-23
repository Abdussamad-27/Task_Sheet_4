class department:
    def __init__(self,dept,list):
        self.dept=dept
        self.list=list

    def list_emp(self):
        print("name : ",self.list,"Department : ",self.dept)
list=[]
dept=department("BCA",list)
e1=department("",list)
e2=department("BCA",list)
e3=department("BCA",list)
e1.list.append("Rahul")
e1.list.append("Raju")
e1.list.append("Ram")
dept.list_emp()

