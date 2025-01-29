month_number = int(input("Enter the month: "))
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

if 1 <= month_number <= 12:
    print(f"Month {month_number} is {months[month_number - 1]}")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")


age = int(input("Enter your age: "))
full_price = 6.0

if age < 16:
    ticket_price = full_price / 2
elif age >= 60:
    ticket_price = full_price / 3
else:
    ticket_price = full_price

print(f"Your ticket costs £{ticket_price:.2f}")



weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("You are in the 'Underweight' range.")
elif 18.5 <= bmi < 25:
    print("You are in the 'Normal' range.")
elif 25 <= bmi < 30:
    print("You are in the 'Overweight' range.")
else:
    print("You are in the 'Obese' range.")




num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

greatest = max(num1, num2, num3)
print(f"The greatest number is {greatest}")





number = int(input("Enter a number: "))
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print(f"The factorial of {number} is {factorial}")





number = int(input("Enter a number: "))
reversed_number = 0

while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10

print(f"The reversed number is {reversed_number}")






number = int(input("Enter a number: "))
limit = int(input("Enter the limit: "))

print(f"The multiples of {number} up to {limit} are:")
for i in range(1, limit + 1):
    if i % number == 0:
        print(i)






value = input("Enter a value: ")
if value.lower() == 'done':
    print("Done")
    break
else:
    print(value)










for i in range(1, 11):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)





for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()






