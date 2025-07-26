# Introduction  -|
# ---------------|
# Python Assingnment for the week 1 while being a part of the Data Science internship team at Zeno Talent under the guidance of Aishwarya. The assignment
# involves building a student grading system that reads marks from a file, calculates overall scores, assigns grades, sorts students, and logs results.


import numpy as np
# importing numpy library for array operations

def file(filename):
    # function to read a file
    try:
        f = open(filename, 'r')
        # opens the file in read mode
        lines = f.readlines()[1:]
        # reads from line 2 leaving the header
        f.close()
        # closes the file after reading
        data = [line.strip().split(",") for line in lines]
        # it splits each line by comma and strips whitespace, stores as a list
        return data
    except FileNotFoundError:
        # in case file does not exist, prints a message and returns empty list
        print("Input file not found!")
        return []

def grades_cal(data):
    # function that calcuates grades and returns a list
    results = []
    # empty list
    for reg, exam, course in data:
        # for loop to check through each record in the data
        try:
            exam = float(exam)
            course = float(course)
            # converts exam and coursework scores to float

            overall = round((0.6 * exam) + (0.4 * course), 2)
            # calculates overall score using 60% of exam and 40% of coursework upto 2 decimal places

            if overall >= 85:
                grade = 'A'
            elif overall >= 70:
                grade = 'B'
            elif overall >= 50:
                grade = 'C'
            else:
                grade = 'F'
            # assigning grades based on overall score

            results.append((reg, exam, course, overall, grade))
            # adding the result to the empty list
        except ValueError:
            # for handling invalid marks(non-numeric values)
            print(f"Invalid data for {reg} skipping.")
    return results

def res(results, filename):
    # function to write a file
    f = open(filename, 'w')
    # opens output file in write mode
    for row in results:
        f.write(",".join(map(str, row)) + "\n")
        # converts each item in the row to string, joins them with commas while writing

def statistics(results):
    # function to calculate grade statistics
    grades = [r[4] for r in results]
    # extracts grades from results
    print("Grade Statistics:")
    for g in ['A', 'B', 'C', 'F']:
        print(f"{g}: {grades.count(g)} students")
        # counts and displays the number of students for every grade

input = 'marks_input.csv'
output = 'marks_output.csv'
raw_data = file(input)
# function call

if raw_data:
    # if data is not empty
    processed = grades_cal(raw_data)
    # calling to calculate the grades

    dtype = [('reg_no', 'U10'), ('exam', 'f4'), ('coursework', 'f4'), ('overall', 'f4'), ('grade', 'U2')]
    np_array = np.array(processed, dtype=dtype)
    # converts results into array with named columns and defined data types:
    # U10 for Unicode string of length 10
    # f4 for 32-bit float

    np_array = np.sort(np_array, order='overall')[::-1]
    # sorting in descending order using slicing
    
    res(np_array, output)
    statistics(np_array)


# Conclusion  -|
# -------------|
# In this Week 1 assignment, I worked on gaining hands-on experience with file handling, NumPy structured arrays, sorting techniques, and implementing
# grading logic from real-world education systems.
