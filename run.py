from datetime import datetime

name = input("Please enter Your name : ")
year = int(input("Please Enter the year you were born (e.g.: 1984): "))
month = input("Input month of birth (e.g. january, may etc): ")
day = int(input("Please enter the day you were born in (e.g. 17:)"))
horo_sign = None
days = (2023 - year) * 365
the_date = datetime.now().date()
name_list = [i for i in name]


def horoscope():
	global horo_sign
	if month == 'december':
		horo_sign = 'Sagittarius' if (day < 22) else 'capricorn'
	elif month == 'january':
		horo_sign = 'Capricorn' if (day < 20) else 'aquarius'
	elif month == 'february':
		horo_sign = 'Aquarius' if (day < 19) else 'pisces'
	elif month == 'march':
		horo_sign = 'Pisces' if (day < 21) else 'aries'
	elif month == 'april':
		horo_sign = 'Aries' if (day < 20) else 'taurus'
	elif month == 'may':
		horo_sign = 'Taurus' if (day < 21) else 'gemini'
	elif month == 'june':
		horo_sign = 'Gemini' if (day < 21) else 'cancer'
	elif month == 'july':
		horo_sign = 'Cancer' if (day < 23) else 'leo'
	elif month == 'august':
		horo_sign = 'Leo' if (day < 23) else 'virgo'
	elif month == 'september':
		horo_sign = 'Virgo' if (day < 23) else 'libra'
	elif month == 'october':
		horo_sign = 'Libra' if (day < 23) else 'scorpio'
	elif month == 'november':
		horo_sign = 'scorpio' if (day < 22) else 'sagittarius'

horoscope()

print("Your Name is:", name.capitalize())
print(name_list)
print("You were born in:", str(day) + " " + str(month.capitalize()) + " " + str(year))
print("Todays date is : ")
print(the_date)
print("That means you have been alive for about " + str(days) + " days")
print("Your astrological sing is:", horo_sign)
