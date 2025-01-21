# BMI Calculator Program

def calculate_bmi(weight, height):
    # BMI formula: BMI = weight (kg) / (height (m) * height (m))
    bmi = weight / (height ** 2)
    return bmi


def main():
    # User input for weight and height
    weight = float(input("Enter your weight in kilograms (kg): "))
    height = float(input("Enter your height in meters (m): "))

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Print the result
    print(f"Your BMI is: {bmi:.2f}")

    # BMI categories
    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        print("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        print("You are overweight.")
    else:
        print("You are obese.")


if __name__ == "__main__":
    main()
