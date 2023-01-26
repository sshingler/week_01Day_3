

def return_10():
    return 10

def add(number_1, number_2):
    return number_1 + number_2

def subtract(number_1, number_2):
    return number_1 - number_2

def multiply(number_1, number_2):
    return number_1 * number_2

def divide(number_1, number_2):
    return number_1 // number_2   #double division floors the number


def length_of_string(test_string):
    return len(test_string)
 

def join_string(string_1, string_2):
    return string_1 + string_2


def add_string_as_number(number1, number2):
    return int(number1) + int(number2)


# def number_to_full_month_name(month):
#     month = ["", "January", "February", "March", 
#             "April", "May", "June", 
#             "July", "August", "September",
#             "October", "November", "December"]
#     return month[1]
    
def number_to_full_month_name(number):
    if number == 1:
        return "January"
    elif number == 2:
        return "February"
    elif number == 3:
        return "March"
    elif number == 4:
        return "April"
    elif number == 5:
        return "May"
    elif number == 6:
        return "June"
    elif number == 7:
        return "July"
    elif number == 8:
        return "August"
    elif number == 9:
        return "September"
    elif number == 10:
        return "October"
    elif number == 11:
        return "November"
    elif number == 12:
        return "December"
    else:
        return "Please enter a number between 1 and 12"
    
# def number_to_short_month_name(number):
#     if number == 1:
#         return "Jan"
#     elif number == 4:
#         return "Apr"
#     elif number == 10:
#         return "Oct"
#     else:
#         return "Please enter either 1, 4, or 10."
    
def number_to_short_month_name (num):
    return number_to_full_month_name(num)[0:3]

def volume_of_cube(cube):
    return cube **3


def reverse_string(string):
    return string[::1]

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
