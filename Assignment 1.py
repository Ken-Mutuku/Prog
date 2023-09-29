#SCT211-0050/2022 KEN MUTUKU
username = input("Enter name")
fees = int(input("Enter your the fee that you pay per semester"))
courseduration = int(input(" Enter the duration that your course is to take"))
tution= 15000
Totalfees = (fees*courseduration*2)+ (tution*4)
Statement = username+", the total amount of fees that you will require for this course is {} in {} years,inclusive of tution."
print (Statement.format(Totalfees, courseduration))
