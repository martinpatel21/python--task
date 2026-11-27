# 1. Length of string
text = input("Enter text: ")
print(len(text))

# 2. Convert sentence to lowercase
sentence = input("Enter sentence: ")
print(sentence.lower())

# 3. Replace spaces with underscores
text = input("Enter text: ")
print(text.replace(" ", "_"))

# 4. First and last character
text = input("Enter text: ")
if text:
    print("First:", text[0], "Last:", text[-1])

# 5. Reverse string using slicing
text = input("Enter text: ")
print(text[::-1])

# 6. Count occurrences of a letter
text = input("Enter text: ")
letter = input("Enter letter: ")
print(text.count(letter))

# 7. Check word in sentence
sentence = input("Sentence: ")
word = input("Word: ")
print(word in sentence)

# 8. Name and age using f-string
name = input("Name: ")
age = int(input("Age: "))
print(f"My name is {name} and I am {age} years old.")

# 9. Remove spaces from start and end
text = input("Enter text: ")
print(text.strip())

# 10. Join words with hyphen
words = ["Python", "is", "easy"]
print("-".join(words))

# 11. List of five favorite movies
movies = ["3 Idiots", "Dangal", "PK", "Chhichhore", "Lupin"]
print(movies)

# 12. Add a movie
movies.append(input("Enter a movie to add: "))
print(movies)

# 13. Remove first movie
if movies:
    movies.pop(0)
print(movies)

# 14. Sort numbers ascending
numbers = [8, 2, 5, 1, 9]
numbers.sort()
print(numbers)

# 15. Reverse a list
numbers.reverse()
print(numbers)

# 16. Largest number in a list
print(max(numbers))

# 17. Merge two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)

# 18. Last element without index number
items = ["red", "green", "blue"]
print(items[-1])

# 19. Nested list and access inner element
nested = [[1, 2], [3, 4], [5, 6]]
print(nested[1][0])

# 20. Count element occurrences
items = [1, 2, 2, 3, 2, 4]
print(items.count(2))
