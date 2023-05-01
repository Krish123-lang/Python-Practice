
height = float(input("Enter  Your Height in centimetres: "))/100
weight = float(input("Enter Your Weight in KGs: "))

metres = (height)**2

BMI = weight/metres

if BMI < 18.5:
    print(f"Your BMI is {BMI}. You are 'UNDERWEIGHTED'.")

elif 18.5 < BMI < 24.9:
    print(f"Your BMI is {BMI}. You are 'NORMAL'.")

elif 25 < BMI < 29.9:
    print(f"Your BMI is {BMI}. You are 'OVER WEIGHTED'.")

elif BMI > 30:
    print(f"Your BMI is {BMI}. You are 'OBESED'.")

else:
    print("Please input valid numbers !!!")
