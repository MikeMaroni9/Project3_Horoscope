import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import time

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Horoscope')



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

"""
General Input Scheme and Variables
"""
name = input("Please enter Your name : \n")
month = input("Input month of birth (e.g. january, may etc): \n").lower()
year = int(input("Please Enter the year you were born (e.g.: 1984): \n"))
day = int(input("Please enter the day you were born in (e.g. 17:)\n"))
horo_sign = None
chn_horo = None
days = (2023 - year) * 365
the_date = datetime.now().date()
name_list = [i for i in name]


"""
def horoscope():
    global horo_sign
    if month in ('january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'):
        if month == 'december':
            horo_sign = 'Sagittarius' if (day < 22) else 'Capricorn'
        elif month == 'january':
            horo_sign = 'Capricorn' if (day < 20) else 'Aquarius'
        elif month == 'february':
            horo_sign = 'Aquarius' if (day < 19) else 'Pisces'
        elif month == 'march':
            horo_sign = 'Pisces' if (day < 21) else 'Aries'
        elif month == 'april':
            horo_sign = 'Aries' if (day < 20) else 'Taurus'
        elif month == 'may':
            horo_sign = 'Taurus' if (day < 21) else 'Gemini'
        elif month == 'june':
            horo_sign = 'Gemini' if (day < 21) else 'Cancer'
        elif month == 'july':
            horo_sign = 'Cancer' if (day < 23) else 'Leo'
        elif month == 'august':
            horo_sign = 'Leo' if (day < 23) else 'Virgo'
        elif month == 'september':
            horo_sign = 'Virgo' if (day < 23) else 'Libra'
        elif month == 'october':
            horo_sign = 'Libra' if (day < 23) else 'Scorpio'
        elif month == 'november':
            horo_sign = 'Scorpio' if (day < 22) else 'Sagittarius'
        else:
            print("There has been an error, please try again !")
    else:
        print("Error, that's not a valid entry, please check your spelling.")


"""
"""
Function to print out matching descriptions for each Zodiac Sign
"""
"""


def horo_description():
    if horo_sign == "Aries":
        print(signDescriptionAries)
    elif horo_sign == "Taurus":
        print(signDescriptionTaurus)
    elif horo_sign == "Gemini":
        print(signDescriptionGemini)
    elif horo_sign == "Cancer":
        print(signDescriptionCancer)
    elif horo_sign == "Leo":
        print(signDescriptionLeo)
    elif horo_sign == "Virgo":
        print(signDescriptionVirgo)
    elif horo_sign == "Libra":
        print(signDescriptionLibra)
    elif horo_sign == "Scorpio":
        print(signDescriptionScorpio)
    elif horo_sign == "Sagittarius":
        print(signDescriptionSagittarius)
    elif horo_sign == "Capricorn":
        print(signDescriptionCapricorn)
    elif horo_sign == "Aquarius":
        print(signDescriptionAquarius)
    elif horo_sign == "Pisces":
        print(signDescriptionPisces)
    else:
        print("ERR: Something went wrong... please try again")


"""
"""
Google Sheet Data implementation for Sign Description
"""
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


"""
"""
Chinese Horoscope Sign Function
"""
"""


def chinese_horo():
    global chn_horo
    if year in (1948, 1960, 1972, 1984, 1996, 2008, 2020):
        chn_horo = "Rat"
    elif year in (1949, 1961, 1973, 1985, 1997, 2009, 2021):
        chn_horo = "Ox"
    elif year in (1950, 1962, 1974, 1986, 1998, 2010, 2022):
        chn_horo = "Tiger"
    elif year in (1951, 1963, 1975, 1987, 1999, 2011, 2023):
        chn_horo = "Rabbit"
    elif year in (1952, 1964, 1976, 1988, 2000, 2012, 2024):
        chn_horo = "Dragon"
    elif year in (1953, 1965, 1977, 1989, 2001, 2013, 2025):
        chn_horo = "Snake"
    elif year in (1954, 1966, 1978, 1990, 2002, 2014, 2026):
        chn_horo = "Horse"
    elif year in (1955, 1967, 1979, 1991, 2003, 2015, 2027):
        chn_horo = "Goat"
    elif year in (1956, 1968, 1980, 1992, 2004, 2016, 2028):
        chn_horo = "Monkey"
    elif year in (1957, 1969, 1981, 1993, 2005, 2017, 2029):
        chn_horo = "Rooster"
    elif year in (1958, 1970, 1982, 1994, 2006, 2018, 2030):
        chn_horo = "Dog"
    elif year in (1959, 1971, 1983, 1995, 2007, 2019, 2031):
        chn_horo = "Pig"
    else:
        print("This system works from year 1948 onwards, please try again.")

"""
"""
Google Sheets Data implementation for CHN Sign Descriptions
"""
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



"""
"""
Function to assign correct Chinese description to correct sign.
"""
"""

def chinese_horo_description():
    if chn_horo == "Rat":
        print(signDescriptionRat)
    elif chn_horo == "Ox":
        print(signDescriptionOx)
    elif chn_horo == "Tiger":
        print(signDescriptionTiger)
    elif chn_horo == "Rabbit":
        print(signDescriptionRabbit)
    elif chn_horo == "Dragon":
        print(signDescriptionRabbit)
    elif chn_horo == "Snake":
        print(signDescriptionSnake)
    elif chn_horo == "Horse":
        print(signDescriptionHorse)
    elif chn_horo == "Goat":
        print(signDescriptionGoat)
    elif chn_horo == "Monkey":
        print(signDescriptionMonkey)
    elif chn_horo == "Rooster":
        print(signDescriptionRooster)
    elif chn_horo == "Dog":
        print(signDescriptionDog)
    elif chn_horo == "Pig":
        print(signDescriptionPig)
    else:
        print("ERR: Something went wrong... please try again")


horoscope()
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
print("You were born in:", str(day) + " " + str(month.capitalize()) + " " + str(year))
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
horo_description()
time.sleep(1)
print("---------------------------------------------------------------------")
time.sleep(1)
print("Initializing contact with China.... Gathering Information:")
time.sleep(3)
print("---------------------------------------------------------------------")
time.sleep(1)
chinese_horo()
time.sleep(1)
print("Your Chinese astrological sing is:", chn_horo)
time.sleep(1)
chinese_horo_description()
time.sleep(1)
print("---------------------------------------------------------------------")
time.sleep(1)
print("- Thank you for trying out My Project 3 : Python application  -------")
time.sleep(1)
print("------------------- Communication Closed-----------------------------")
"""