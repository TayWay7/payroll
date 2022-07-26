print("Begin Payroll")
    
def get_emp_info():
    emp_name = input("Enter employee name: ")
    return emp_name


def total_hours_worked():
    total_hours_worked = float(input("Enter total hours worked: "))
    return (f'{round(total_hours_worked,1)}')
 
def pay_rate():
    pay_rate = float(input("Enter employee hourly rate: "))
    return pay_rate
    
def income_tax_rate():
    income_tax_rate = float(input('Enter income tax rate: '))
    return income_tax_rate
    
def get_pay_info(total_hours_worked, hourly_rate, income_tax_rate):
    gross_pay = total_hours_worked * hourly_rate
    income_tax = gross_pay * income_tax_rate #total income tax is just tax rate times gross pay
    net_pay = gross_pay - income_tax # net pay is just gross_pay minus income_tax
    return income_tax, net_pay
    
def sum_info(emp_name, total_hours_worked, hourly_rate, income_tax_rate, income_tax, net_pay):
	print('Employee name: ', emp_name, 'Total hours: ', total_hours_worked, 'Hourly rate: ', hourly_rate, 'Income tax rate: ', income_tax_rate, 'Income tax amount: ', income_tax, 'Net pay: ', net_pay)
    # might want to format this cleaner


def final_num(total_num_employees, final_hours, final_tax, final_pay):
   print(total_num_employees, final_hours, final_tax, final_pay)

 


# create variables here to store total number of employees, total hours, total tax, total net pay
total_num_employees = 0
final_hours = 0
final_tax = 0
final_pay = 0
  
while True:	
   emp_name = get_emp_info()
   if emp_name == "end":
      final_num(total_num_employees, final_hours, final_tax, final_pay)
      break   
   
   total_num_employees += 1 #  calling this since the previous line got a new employee.
   total_hours_worked = total_hours_worked()
   final_hours += total_hours_worked #lling this since the previous line got more h
   pay_rate = pay_rate()
   income_tax_rate = income_tax_rate()
   income_tax, net_pay = get_pay_info(total_hours_worked, pay_rate, income_tax_rate)
   final_tax += income_tax
   final_pay += net_pay #incrememnt total tax and net pay
   sum_info(emp_name, total_hours_worked, pay_rate, income_tax_rate, income_tax, net_pay)


     


       

 





