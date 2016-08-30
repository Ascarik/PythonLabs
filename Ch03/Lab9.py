name = input("Enter employee's name: ")
hours = int(input("Enter number of hours worked in a week: "))
pay_rate = float(input("Enter hourly pay rate: "))
federal_tax = float(input("Enter federal tax withholding rate: "))
state_tax = float(input("Enter state tax withholding rate: "))

print("\n\nEmployee Name:", name)
print("Hours Worked:", hours)
print("Pay Rate: $",pay_rate, sep='')

gross_pay = pay_rate * hours
print("Gross Pay: $",gross_pay, sep='')

print("Deductions:")

result_federal_tax = gross_pay * federal_tax
print("\tFederal Withholding ({:.1%}): ${}".format(federal_tax, result_federal_tax))

result_state_tax = gross_pay * state_tax
print("\tState Withholding ({:.1%}): ${:.2f}".format(state_tax, result_state_tax))

result_total_tax = result_federal_tax + result_state_tax
print("\tTotal Deduction: ${:.2f}".format(result_total_tax))

print("Net Pay: {:.2f}".format(gross_pay - result_total_tax))