# 1. Voting eligibility
age = int(input("Enter age: "))
print("Eligible to vote" if age >= 18 else "Not eligible to vote")

# 2. Grade calculator
marks = float(input("Enter marks: "))
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
else:
    grade = "C"
print("Grade:", grade)

# 3. Traffic light
light = input("Enter traffic light color: ").lower()
if light == "red":
    print("Stop")
elif light == "yellow":
    print("Wait")
elif light == "green":
    print("Go")
else:
    print("Invalid color")

# 4. ATM withdrawal
balance = float(input("Balance: "))
amount = float(input("Withdrawal amount: "))
if amount > 0 and amount <= balance:
    print("Withdrawal successful. Remaining:", balance - amount)
else:
    print("Insufficient balance or invalid amount")

# 5. Positive, negative, or zero
n = float(input("Enter number: "))
print("Positive" if n > 0 else "Negative" if n < 0 else "Zero")

# 6. Check number in range
n = float(input("Number: "))
low = float(input("Range start: "))
high = float(input("Range end: "))
print("In range" if low <= n <= high else "Out of range")

# 7. Username and password verification
username = input("Username: ")
password = input("Password: ")
if username == "admin" and password == "admin123":
    print("Login successful")
else:
    print("Invalid username or password")

# 8. Electricity bill calculator (sample slab rates)
units = float(input("Units consumed: "))
if units < 0:
    print("Invalid units")
else:
    if units <= 100:
        bill = units * 1.5
    elif units <= 200:
        bill = 100 * 1.5 + (units - 100) * 2.5
    else:
        bill = 100 * 1.5 + 100 * 2.5 + (units - 200) * 4
    print("Bill: Rs.", bill)

# 9. Simple calculator
a = float(input("First number: "))
b = float(input("Second number: "))
op = input("Operator (+, -, *, /): ")
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/" and b != 0:
    print(a / b)
else:
    print("Invalid operator or division by zero")

# 10. Type of triangle
a, b, c = map(float, input("Enter three sides: ").split())
if min(a, b, c) <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print("Invalid triangle")
elif a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")
