bill= int(input("Enter the cost of food and drinks consumed: "))
no = int(input("Enter the number of people who will be splitting the bill: "))
tip = (1/10)*bill
Total_bill= bill+ tip #the tip is included as the 10% added over
per_person= Total_bill/no
Statement= "The amount to be paid per person will be {}"
print(Statement.format(per_person))


