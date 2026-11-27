# 1. Tuple with five numbers
numbers = (10, 20, 30, 40, 50)
print(numbers)

# 2. Third tuple element
print(numbers[2])

# 3. Unpack tuple
a, b, c, d, e = numbers
print(a, b, c, d, e)

# 4. Set of five fruits
fruits = {"apple", "banana", "mango", "orange", "grapes"}
print(fruits)

# 5. Add fruit
fruits.add("watermelon")
print(fruits)

# 6. Remove an element safely
fruits.discard("banana")
print(fruits)

# 7. Union of two sets
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(set_a | set_b)

# 8. Intersection
print(set_a & set_b)

# 9. Subset check
small = {1, 2}
large = {1, 2, 3, 4}
print(small.issubset(large))

# 10. Remove duplicates using set
values = [1, 2, 2, 3, 3, 4]
print(set(values))

# 11. Dictionary of student marks
marks = {"Amit": 85, "Neha": 92, "Raj": 78}
print(marks)

# 12. Add key-value pair
marks["Martin"] = 90
print(marks)

# 13. Delete key-value pair
marks.pop("Raj", None)
print(marks)

# 14. Merge dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
print(dict1 | dict2)

# 15. Check whether key exists
print("Amit" in marks)

# 16. Word frequency
text = input("Enter a sentence: ").lower()
frequency = {}
for word in text.split():
    frequency[word] = frequency.get(word, 0) + 1
print(frequency)

# 17. Key with maximum value
scores = {"A": 80, "B": 95, "C": 88}
print(max(scores, key=scores.get))

# 18. Reverse keys and values
original = {"one": 1, "two": 2, "three": 3}
reversed_dict = {value: key for key, value in original.items()}
print(reversed_dict)

# 19. Update a dictionary value
marks["Amit"] = 95
print(marks)

# 20. Convert list of tuples to dictionary
pairs = [("name", "Martin"), ("age", 20), ("city", "Valsad")]
print(dict(pairs))
