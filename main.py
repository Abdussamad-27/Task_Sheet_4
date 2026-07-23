import salary_utils as s

basic_salary=40000
hra=s.calculate_hra(basic_salary)

net_salary=s.calculate_net(basic_salary,hra)


print(f"basic_salary {basic_salary:,.2f}")
print(f"hra amount {hra:,.2f}")
print(f"Net Salary is : {net_salary:,.2f}")