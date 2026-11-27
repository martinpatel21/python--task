# 1. Prime number function
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(int(input("Number: "))))

# 2. Reverse string
def reverse_string(text):
    return text[::-1]
print(reverse_string(input("Text: ")))

# 3. Factorial
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
print(factorial(int(input("Number: "))))

# 4. Simple interest
def simple_interest(principal, rate, time):
    return principal * rate * time / 100
print(simple_interest(10000, 5, 2))

# 5. Palindrome word
def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]
print(is_palindrome(input("Word: ")))

# 6. Count vowels
def count_vowels(text):
    return sum(1 for char in text.lower() if char in "aeiou")
print(count_vowels(input("Text: ")))

# 7. Merge two lists
def merge_lists(first, second):
    return first + second
print(merge_lists([1, 2], [3, 4]))

# 8. GCD
def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)
print(gcd(48, 18))

# 9. Area of rectangle
def rectangle_area(length, width):
    return length * width
print(rectangle_area(5, 4))

# 10. Armstrong number
def is_armstrong(number):
    digits = str(abs(number))
    power = len(digits)
    return number >= 0 and sum(int(digit) ** power for digit in digits) == number
print(is_armstrong(int(input("Number: "))))
