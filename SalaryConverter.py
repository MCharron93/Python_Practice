
def promptUser():
   annualSalary = int(input("What is your annual salary?")
   #return annualSalary

def convertSalary():
   weeksWored = annualSalary / 50
   hoursWeek = weeksWorked / 40
   return hoursWeek

salary = promptUser()

userHourlyRate = convertSalary(salary)

print("Your hourly rate is " + str(userHourlyRate))
