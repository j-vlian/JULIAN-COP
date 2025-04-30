# This program determines an employee's bonus and prints the employee's name and bonus.

#initialize variables
employeeName= ""
shiftsWorked= 0
numTrans=0
transValue=0
avgTransvalue=0
productivityScore=0
bonus=0

#input
employeeName=input("Enter employee's name: ")
shiftsWorked=int(input("Enter number of shifts worked: "))
numTrans=int(input("Enter number of transactions: "))
transValue=float(input("Enter total of all transactions dollar value: $"))

#calculate productivity score
if shiftsWorked >0 and numTrans >0:
 avgTransvalue=transValue/numTrans
 productivityScore= avgTransvalue/shiftsWorked

#determine bonus
if productivityScore <= 30:
        bonus=50
elif productivityScore <=69:
    bonus=75
elif productivityScore <=199:
    bonus=100
else:
    bonus=200

#output
print(f"n\Employee Name: {employeeName}")
print(f"n\Employee Bonus: ${bonus}")