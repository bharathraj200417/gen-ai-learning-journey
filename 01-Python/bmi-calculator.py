# ----------------------------------
# Body Mass Index (BMI) Calculator
# ----------------------------------

# Get user input
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

# Calculate BMI
bmi = weight / (height * height)

# Display BMI category
if bmi < 18.5:
    print("Underweight")
elif bmi < 24.9:
    print("Normal Weight")
elif bmi < 29.9:
    print("Overweight")
else:
    print("Obese")
