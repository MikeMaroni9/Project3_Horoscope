import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import time

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

"""
Global Variables
"""
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Horoscope')
the_date = datetime.now().date()


"""
ASCII Graphics to make the intro of the program more appealing
"""
print("---------------------------------------------------------------------")
print("********* Welcome to your personalised Horoscope Checker ************")
print("---------------------------------------------------------------------")
print("                                  _ _")
print("                                 | (_)")
print("                     _______   __| |_  __ _  ___")
print("                    |_  / _ \ / _` | |/ _` |/ __|")
print("                     / / (_) | (_| | | (_| | (__ ")
print("                    /___\___/ \__,_|_|\__,_|\___|_")
print("---------------------------------------------------------------------")
print("---------------------------------------------------------------------")
time.sleep(2)
print("---------------Greetings, let us begin, shall we ?-------------------")
print("---------------------------------------------------------------------")
time.sleep(1)
name = input("Please enter Your name or leave it empty: \n")
if not name:
    name = "You wished to remain anonymous"
name_list = [i for i in name]
print("---------------------------------------------------------------------")


def is_valid_year(year):
    """
    User input and error checking of the YEAR he was born in
    """
    return 1948 <= year <= 2031
    global enter_year


while True:
    try:
        enter_year = int(input("Please enter a YEAR you were born in: \n (YYYY format, ex: 1984): \n"))
        if is_valid_year(enter_year):
            break
        else:
            print("Year ranges currently available in software (1948 to 2031)")
    except ValueError:
        print("The data is invalid. Please enter a valid year.")

print("Please wait, while the system loads all components...")
days = (2023 - int(enter_year)) * 365


def main():
    """
    Main function of the code
    """
    global month
    global zodiac_sign
    valid_months = ['January', 'February', 'March', 'April', 'May', 'June',
                    'July', 'August', 'September', 'October', 'November', 'December']
    while True:
        enter_month = input("Now the MONTH you were born in (ex.May,June:) \n")
        month = enter_month.title()

        if month in valid_months:
            print("Thank You!")
            break
        else:
            print("Data format is not correct. Please try again.")
    selected_date = get_valid_date()
    horoscope(month, selected_date)
    zodiac_sign = chinese_horo(enter_year)


def get_valid_date():
    """
    User input and error checking of the day of the month he was born in
    """
    global date
    while True:
        try:
            date = int(input("And finally DAY of the month you were born in. 1 to 31: \n"))
            if 1 <= date <= 31:
                return date
            else:
                print("Error: Date must be between 1 and 31.")
        except ValueError:
            print("Error: Please enter a valid number.")


def horoscope(month, day):
    """
    Function to assing correct Horoscope sign to the user
    based on the data he has entered
    """
    global horo_sign
    if month == 'December':
        horo_sign = 'Sagittarius' if day < 22 else 'Capricorn'
    elif month == 'January':
        horo_sign = 'Capricorn' if day < 20 else 'Aquarius'
    elif month == 'February':
        horo_sign = 'Aquarius' if day < 19 else 'Pisces'
    elif month == 'March':
        horo_sign = 'Pisces' if day < 21 else 'Aries'
    elif month == 'April':
        horo_sign = 'Aries' if day < 20 else 'Taurus'
    elif month == 'May':
        horo_sign = 'Taurus' if day < 21 else 'Gemini'
    elif month == 'June':
        horo_sign = 'Gemini' if day < 21 else 'Cancer'
    elif month == 'July':
        horo_sign = 'Cancer' if day < 23 else 'Leo'
    elif month == 'August':
        horo_sign = 'Leo' if day < 23 else 'Virgo'
    elif month == 'September':
        horo_sign = 'Virgo' if day < 23 else 'Libra'
    elif month == 'October':
        horo_sign = 'Libra' if day < 23 else 'Scorpio'
    elif month == 'November':
        horo_sign = 'Scorpio' if day < 22 else 'Sagittarius'
    return horo_sign


"""
Google Sheet Data implementation for Sign Description
"""
signDescriptionAries = SHEET.worksheet('sign_description').col_values(1)
signDescriptionTaurus = SHEET.worksheet('sign_description').col_values(2)
signDescriptionGemini = SHEET.worksheet('sign_description').col_values(3)
signDescriptionCancer = SHEET.worksheet('sign_description').col_values(4)
signDescriptionLeo = SHEET.worksheet('sign_description').col_values(5)
signDescriptionVirgo = SHEET.worksheet('sign_description').col_values(6)
signDescriptionLibra = SHEET.worksheet('sign_description').col_values(7)
signDescriptionScorpio = SHEET.worksheet('sign_description').col_values(8)
signDescriptionSagittarius = SHEET.worksheet('sign_description').col_values(9)
signDescriptionCapricorn = SHEET.worksheet('sign_description').col_values(10)
signDescriptionAquarius = SHEET.worksheet('sign_description').col_values(11)
signDescriptionPisces = SHEET.worksheet('sign_description').col_values(12)


def horo_description(horo_sign):
    """
    Function calling for the correct description based on the Horoscope sign
    """
    sign_descriptions = {
        "Aries": signDescriptionAries,
        "Taurus": signDescriptionTaurus,
        "Gemini": signDescriptionGemini,
        "Cancer": signDescriptionCancer,
        "Leo": signDescriptionLeo,
        "Virgo": signDescriptionVirgo,
        "Libra": signDescriptionLibra,
        "Scorpio": signDescriptionScorpio,
        "Sagittarius": signDescriptionSagittarius,
        "Capricorn": signDescriptionCapricorn,
        "Aquarius": signDescriptionAquarius,
        "Pisces": signDescriptionPisces
    }

    if horo_sign in sign_descriptions:
        print(sign_descriptions[horo_sign])
    else:
        print("ERR: Something went wrong... please try again")


def chinese_horo(year):
    """
    Function checking for the correct Chinese horoscope
    based on the year he was born in
    """
    if year in (1948, 1960, 1972, 1984, 1996, 2008, 2020):
        return "Rat"
    elif year in (1949, 1961, 1973, 1985, 1997, 2009, 2021):
        return "Ox"
    elif year in (1950, 1962, 1974, 1986, 1998, 2010, 2022):
        return "Tiger"
    elif year in (1951, 1963, 1975, 1987, 1999, 2011, 2023):
        return "Rabbit"
    elif year in (1952, 1964, 1976, 1988, 2000, 2012, 2024):
        return "Dragon"
    elif year in (1953, 1965, 1977, 1989, 2001, 2013, 2025):
        return "Snake"
    elif year in (1954, 1966, 1978, 1990, 2002, 2014, 2026):
        return "Horse"
    elif year in (1955, 1967, 1979, 1991, 2003, 2015, 2027):
        return "Goat"
    elif year in (1956, 1968, 1980, 1992, 2004, 2016, 2028):
        return "Monkey"
    elif year in (1957, 1969, 1981, 1993, 2005, 2017, 2029):
        return "Rooster"
    elif year in (1958, 1970, 1982, 1994, 2006, 2018, 2030):
        return "Dog"
    elif year in (1959, 1971, 1983, 1995, 2007, 2019, 2031):
        return "Pig"
    else:
        raise ValueError("This system works from year 1948 to 2031, please try again.")


"""
Google Sheets Data implementation for CHN Sign Descriptions
"""
signDescriptionRat = SHEET.worksheet('chn_sign_description').col_values(1)
signDescriptionOx = SHEET.worksheet('chn_sign_description').col_values(2)
signDescriptionTiger = SHEET.worksheet('chn_sign_description').col_values(3)
signDescriptionRabbit = SHEET.worksheet('chn_sign_description').col_values(4)
signDescriptionDragon = SHEET.worksheet('chn_sign_description').col_values(5)
signDescriptionSnake = SHEET.worksheet('chn_sign_description').col_values(6)
signDescriptionHorse = SHEET.worksheet('chn_sign_description').col_values(7)
signDescriptionGoat = SHEET.worksheet('chn_sign_description').col_values(8)
signDescriptionMonkey = SHEET.worksheet('chn_sign_description').col_values(9)
signDescriptionRooster = SHEET.worksheet('chn_sign_description').col_values(10)
signDescriptionDog = SHEET.worksheet('chn_sign_description').col_values(11)
signDescriptionPig = SHEET.worksheet('chn_sign_description').col_values(12)


def chinese_horo_description(zodiac_sign):
    """
    Function assigning correct description for the Chinese horoscope sign
    based on the year he was born in
    """
    if zodiac_sign == "Rat":
        description = signDescriptionRat
    elif zodiac_sign == "Ox":
        description = signDescriptionOx
    elif zodiac_sign == "Tiger":
        description = signDescriptionTiger
    elif zodiac_sign == "Rabbit":
        description = signDescriptionRabbit
    elif zodiac_sign == "Dragon":
        description = signDescriptionDragon
    elif zodiac_sign == "Snake":
        description = signDescriptionSnake
    elif zodiac_sign == "Horse":
        description = signDescriptionHorse
    elif zodiac_sign == "Goat":
        description = signDescriptionGoat
    elif zodiac_sign == "Monkey":
        description = signDescriptionMonkey
    elif zodiac_sign == "Rooster":
        description = signDescriptionRooster
    elif zodiac_sign == "Dog":
        description = signDescriptionDog
    elif zodiac_sign == "Pig":
        description = signDescriptionPig
    return description


main()
"""
Main logic of the console print out for the UI
"""
print("---------------------------------------------------------------------")
time.sleep(1)
print("---------------------------------------------------------------------")
time.sleep(1)
print("Your Name is:", name.upper())
time.sleep(1)
print(name_list)
time.sleep(1)
print("---------------------------------------------------------------------")
print("Please Wait, calculating data...")
time.sleep(3)
print("---------------------------------------------------------------------")
time.sleep(1)
print("You were born in:", str(date) + " " + str(month.capitalize()) + " " + str(enter_year))
time.sleep(1)
print("Today's date is : ")
time.sleep(1)
print(the_date)
time.sleep(1)
print("That means you have been alive for about " + str(days) + " days")
time.sleep(1)
print("---------------------------------------------------------------------")
time.sleep(1)
print("Please Wait, Processing Information...")
time.sleep(3)
print("---------------------------------------------------------------------")
time.sleep(1)

print("Your astrological sing is:", horo_sign)
time.sleep(1)
print(horo_sign + " " + "is best described as :")
time.sleep(1)
horo_description(horo_sign)
time.sleep(1)
print("---------------------------------------------------------------------")
time.sleep(1)
print("Initializing contact with China.... Gathering Information:")
time.sleep(3)
print("---------------------------------------------------------------------")
time.sleep(1)
print("Your Chinese astrological sing is:", zodiac_sign)
time.sleep(1)
print(chinese_horo_description(zodiac_sign))
time.sleep(1)
print("---------------------------------------------------------------------")
time.sleep(1)
print("- Thank you for trying out My Project 3 : Python application  -------")
time.sleep(1)
print("------------------- Communication Closed-----------------------------")
