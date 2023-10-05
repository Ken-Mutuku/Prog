#SCT211-0050/2022 KEN MUTUKU
username = input("Enter name")
#fees = int(input("Enter your the fee that you pay per semester"))
#courseduration = int(input(" Enter the duration that your course is to take"))
#Totalfees = (fees*courseduration*2)
#Statement = username+", the total amount of fees that you will require for this course is {} in {} years."
#print (Statement.format(Totalfees, courseduration))
from datetime import date
import datetime
year= int(input("Enter your year of birth"))
month= int(input("Enter the month of birth"))
day= int(input("Enter the day you were born"))
date_of_birth= datetime.date(year, month, day)
z= date.today()
age_years= z.year- date_of_birth.year
Statementyear= username+ ", is {} today."
print(Statementyear.format(age_years))
age_month= z.month- date_of_birth.month
Statementmonth= username+ ", is {} today."
print(Statementmonth.format(age_month))
age_day= z.day-date_of_birth.day
Statementday= username+ ", is {} days old today. "
print(Statementday.format(age_day))
