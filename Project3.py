# Underweight:BMI less than 18.5
# Normal weight:BMI between 18.5 and 24.9
# Overweight:BMI between 25 and 29.9
# Obesity:
# Class I (Moderate obesity): BMI between 30 and 34.9
# Class II (Severe obesity): BMI between 35 and 39.9
# Class III (Very severe or morbid obesity): BMI of 40 and above
weight=float(input("Enter your weight "))
height=float(input("Enter your height"))
bmi=weight/(height*height)
print(bmi)
if bmi<18.5:
    print("You are under weight")
elif bmi>=18.5 and bmi<=24.9:
    print("You are normal weight")
elif bmi>=25 and bmi<=29.9:
    print ("You are obese")
elif bmi>=30:

    if bmi>=30 and bmi<=34.9:
        print("You have class 1(moderate obesity) obesity")
    elif bmi>=35 and bmi<=39.9:
        print("You have class 2(severe obesity) obesity")
    elif bmi>=40:
        print("You have class 3 (morbid obesity")
else:
    print("Enter proper weight and height")
