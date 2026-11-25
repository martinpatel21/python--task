# 1. Print name, age, and city in one line
name, age, city = "Martin", 19, "Valsad"
print(name, age, city)

# 2. Sum of two user-input numbers
a = float(input("First number: "))
b = float(input("Second number: "))
print("Sum:", a + b)

# 3. Celsius to Fahrenheit
celsius = float(input("Temperature in Celsius: "))
print("Fahrenheit:", (celsius * 9 / 5) + 32)

# 4. Store name and print uppercase
name = input("Enter your name: ")
print(name.upper())

# 5. Calculate age from birth year
from datetime import date
birth_year = int(input("Enter birth year: "))
print("Age:", date.today().year - birth_year)

# 6. Swap two variables
a = input("Enter a: ")
b = input("Enter b: ")
a, b = b, a
print("a =", a, "b =", b)

# 7. Area of rectangle
length = float(input("Length: "))
width = float(input("Width: "))
print("Area:", length * width)

# 8. Positive or negative
number = float(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# 9. Average of two numbers
a = float(input("First number: "))
b = float(input("Second number: "))
print("Average:", (a + b) / 2)
