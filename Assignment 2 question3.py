#SCT211-0040/2022 KEN MUTUKU BMI QUESTION
Height = int(input("Enter your heigth in cm "))
Mass = int(input("Mass "))
BMI= ((Mass/Height)*100)**2
if 18.5<BMI<=24.9:
    print("Normal BMI")
elif BMI<18.5:
    print("Abnormal BMI, you are underweight")
else:
    print("Abnormal BMI, you are overweight")
