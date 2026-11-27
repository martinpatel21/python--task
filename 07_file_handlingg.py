from pathlib import Path
import csv
import shutil

# Create a sample file for the exercises
Path("sample.txt").write_text("Python is easy.\nPython is powerful.\nFile handling in Python.\n", encoding="utf-8")

# 1. Read and display file contents
with open("sample.txt", "r", encoding="utf-8") as file:
    print(file.read())

# 2. Count lines
with open("sample.txt", "r", encoding="utf-8") as file:
    print("Lines:", sum(1 for _ in file))

# 3. Count each word
with open("sample.txt", "r", encoding="utf-8") as file:
    words = file.read().lower().split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)

# 4. Write five user-entered sentences
with open("sentences.txt", "w", encoding="utf-8") as file:
    for i in range(5):
        file.write(input(f"Sentence {i + 1}: ") + "\n")

# 5. Append a list of strings
lines_to_add = ["First added line", "Second added line"]
with open("sample.txt", "a", encoding="utf-8") as file:
    file.writelines(line + "\n" for line in lines_to_add)

# 6. Print lines containing a specific word
search_word = input("Search word: ").lower()
with open("sample.txt", "r", encoding="utf-8") as file:
    for line in file:
        if search_word in line.lower():
            print(line, end="")

# 7. Replace a word and save changes
path = Path("sample.txt")
content = path.read_text(encoding="utf-8")
content = content.replace("easy", "simple")
path.write_text(content, encoding="utf-8")

# 8. Merge two text files into a third file
Path("first.txt").write_text("Content of first file\n", encoding="utf-8")
Path("second.txt").write_text("Content of second file\n", encoding="utf-8")
with open("merged.txt", "w", encoding="utf-8") as output:
    for filename in ("first.txt", "second.txt"):
        with open(filename, "r", encoding="utf-8") as source:
            output.write(source.read())

# 9. Read CSV and display formatted content
with open("students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "marks"])
    writer.writeheader()
    writer.writerow({"name": "Amit", "marks": 85})
    writer.writerow({"name": "Neha", "marks": 92})
with open("students.csv", "r", newline="", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        print(f"Name: {row['name']:<10} Marks: {row['marks']}")

# 10. Back up a file
shutil.copy2("sample.txt", "sample_backup.txt")
print("Backup created")
