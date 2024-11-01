"""
Title: Module 2 Case Study.py
Author: Neal Vander Does
Date: 10/31/2024
Class: SDEV220-50P-IO-202420-I-82X
Description: 
    Program to take in a students first name & last name & GPA then decide whether they made the Dean's List or Honor Roll based on their GPA.

Input:
    last_name: students last name or ZZZ to quit
    first_name: students first name
    gpa: students gpa (as a float)

Process:
    if & elif to check the gpa's and assign them to Dean's List or Honor Roll

Output:
    Student's last name & first name followed by whether they made the Dean's List or Honor Roll
"""

while True:
    last_name = input("Enter students last name or 'ZZZ' to quit: ")
    if last_name == "ZZZ":
        break
    first_name = input("Enter students first name: ")
    gpa = float(input("Enter students GPA as a float: "))
    if gpa >= 3.5:
        print(f"{last_name}, {first_name} has made the Dean's List with a GPA of {gpa}")
    elif gpa >= 3.25:
        print(f"{last_name}, {first_name} has made the Honor Roll with a GPA of {gpa}")