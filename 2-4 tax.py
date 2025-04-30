# 2-4 tax.py -This program calculates tax, deductions and take home pay

# input statements
salary = float(input("Enter salary $"))
numDependents = float(input("Enter number of dependents"))

# calculate taxes here
stateTax = float((.065)*salary)
federalTax = float((.28)*salary)
dependentDeduction= float((.025)*(numDependents))*salary
totalWitholding = (stateTax)+(federalTax)+(dependentDeduction)
takeHomePay = salary-totalWitholding

# output statements
print("State Tax: $"+str(stateTax))
print("Federal Tax: $"+str(federalTax))
print("Dependents: $"+str(dependentDeduction))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))