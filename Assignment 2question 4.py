#SCT211-0050/2022 KEN MUTUKU 
year= int(input("Enter the year: "))
if year%100==0 and year%400==0:
    print("This is a leap year.")
else:
    print("This year is not a leap year.")