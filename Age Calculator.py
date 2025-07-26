# Introduction  -|
# ---------------|
# Python Assingnment for the week 1 while being a part of the Data Science internship team at Zeno Talent under the guidance of Aishwarya. The assignment
# involves writing a Python program that asks for user’s name birth date, validates it, calculates their current age in years, and formats the date to a
# European style.

from datetime import datetime
# used to import the datetime class from the datetime module which is used for date operations like parsing

def get_date():
    # function to get user input for name and birth date and returns both birth date and name
    try:
        # handle exceptions(incorrect date formats) that might occur during parsing dates
        name = input("Enter your name: ")
        print(f"Hello, {name}!")
        # takes user name as input and prints it
        birth = input("Enter your birthdate in(mm/dd/yyyy): ")
        # takes birth date as input

        birth_date = datetime.strptime(birth, "%m/%d/%Y")
        # it parses the birth string into a datetime object using strptime() with the format "%m/%d/%Y"

        return birth_date, name
    except ValueError:
        # it catches any incorrect format errors(25-07-2000 instead of 07/25/2000)
        print("Invalid date format! Please like mm/dd/yyyy format.")
        return None

def age_cal(birth_date):
    # function to compute current age from the birth date and returns the age
    today = datetime.today()
    # gets today’s date and time using the today() method

    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    # calculates age in full years if the user hasn’t had their birthday yet this year, subtracts 1
    return age

birth_date, name = get_date()
# function call

if birth_date:
    # if a valid birthdate is returned else(None) skips this
    age = age_cal(birth_date)
    print(f"{name}, your age is: {age} years")
    # calling the function to calculate age and prints it

    european = birth_date.strftime("%d/%m/%Y")
    # converts the original birthdate to European date format using strftime()
    print(f"{name}, your birthdate in European format is: {european}")


# Conclusion  -|
# -------------|
# In this Week 1 assignment, I worked on date parsing, string formatting, input validation, and exception handling in Python.
