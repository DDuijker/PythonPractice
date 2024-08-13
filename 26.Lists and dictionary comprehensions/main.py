NAMES = ["Alex", "Beth", "Caroline", "Eleanor", "Freddie", "Dave"]

# List comprehension --------------------------
# 'Syntax': [ value for value in list if condition]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_numbers = [n + 1 for n in numbers]

# Splitting name using list comprehension
name = "Djoeke"
seperated_name = [letter for letter in name]

# Create a new list from a range, were the list items are double the values in the range
new_list = [n * 2 for n in range(1, 5)]

# Create a new list that contains the names longer than 5 characters in ALL CAPS
capitalized_names = [name.upper() for name in NAMES if len(name) > 5]

# Dictionary Comprehension --------------------------
# 'Syntax': {new_key:new_value for (key, value) in dict.items() if condition}

import random

student_score = {student: random.randint(1, 100) for student in NAMES}
passed_students = {student:score for (student, score) in student_score.items() if score > 60}

# Iterating over Pandas Data Frame --------------------------

import pandas

student_dict = {
    "Angela": 67,
    "Jack": 55,
    "Lily": 65
}

student_df = pandas.DataFrame(student_score)
print(student_df)

# Loop through a data frame (cols)
# for (key,value) in student_df.items():
#     print(value)

# Loop through rows of data frame
# for (index, row) in student_df.iterrows():
#     print(row.student)

