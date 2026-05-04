# Name: Kris Kleiner
# Date: May 3, 2026
# Assignment: Module 8 - JSON Student List
# Purpose: Load, print, update, and save a student list from a JSON file.
# Source: Based on Bellevue University CSD-325 Module 8 assignment requirements and Python json module documentation.

import json


def print_students(student_list):
    """Loop through the student list and print each student's information."""

    for student in student_list:
        print(f"{student['L_Name']}, {student['F_Name']} : "
              f"ID = {student['Student_ID']} , Email = {student['Email']}")


# Load the original student data from the JSON file.
with open("student.json", "r") as file:
    students = json.load(file)


# Display the original student list.
print("This is the original Student list.")
print_students(students)


# Add a new student record to the list.
students.append({
    "F_Name": "Kris",
    "L_Name": "Kleiner",
    "Student_ID": 99999,
    "Email": "kkleiner@gmail.com"
})


# Display the updated student list.
print()
print("This is the updated Student list.")
print_students(students)


# Save the updated student list back to the JSON file.
with open("student.json", "w") as file:
    json.dump(students, file, indent=4)


# Notify the user that the JSON file was updated.
print()
print("The student.json file was updated.")
