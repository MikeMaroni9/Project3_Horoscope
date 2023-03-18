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

sign_description = {
    "Aries": "The first sign of the zodiac, Aries loves to be number one. Naturally, this dynamic fire sign is no stranger to competition. Bold and ambitious, Aries dives headfirst into even the most challenging situations—and they'll make sure they always come out on top!",
    "Taurus": "What sign is more likely to take a six-hour bath, followed by a luxurious Swedish massage and decadent dessert spread? Why Taurus, of course! Taurus is an earth sign represented by the bull. Like their celestial spirit animal, Taureans enjoy relaxing in serene, bucolic environments surrounded by soft sounds, soothing aromas, and succulent flavors. ",
    "Gemini": "Have you ever been so busy that you wished you could clone yourself just to get everything done? That's the Gemini experience in a nutshell. Spontaneous, playful, and adorably erratic, Gemini is driven by its insatiable curiosity. Appropriately symbolized by the celestial twins, this air sign was interested in so many pursuits that it had to double itself. You know, NBD!",
    "Cancer": "Represented by the crab, Cancer seamlessly weaves between the sea and shore representing Cancer’s ability to exist in both emotional and material realms. Cancers are highly intuitive and their psychic abilities manifest in tangible spaces. But—just like the hard-shelled crustaceans—this water sign is willing to do whatever it takes to protect itself emotionally. In order to get to know this sign, you're going to need to establish trust!",
    "Leo": "Roll out the red carpet because Leo has arrived. Passionate, loyal, and infamously dramatic, Leo is represented by the lion and these spirited fire signs are the kings and queens of the celestial jungle. They're delighted to embrace their royal status: Vivacious, theatrical, and fiery, Leos love to bask in the spotlight and celebrate… well, themselves.",
    "Virgo": "You know the expression, 'if you want something done, give it to a busy person?' Well, that definitely is the Virgo anthem. Virgos are logical, practical, and systematic in their approach to life. Virgo is an earth sign historically represented by the goddess of wheat and agriculture, an association that speaks to Virgo's deep-rooted presence in the material world. This earth sign is a perfectionist at heart and isn’t afraid to improve skills through diligent and consistent practice.",
    "Libra": "Balance, harmony, and justice define Libra energy. As a cardinal air sign, Libra is represented by the scales (interestingly, the only inanimate object of the zodiac), an association that reflects Libra's fixation on establishing equilibrium. Libra is obsessed with symmetry and strives to create equilibrium in all areas of life — especially when it comes to matters of the heart.",
    "Scorpio": "Elusive and mysterious, Scorpio is one of the most misunderstood signs of the zodiac. Scorpio is a water sign that uses emotional energy as fuel, cultivating powerful wisdom through both the physical and unseen realms. In fact, Scorpio derives its extraordinary courage from its psychic abilities, which is what makes this sign one of the most complicated, dynamic signs of the zodiac.",
    "Sagittarius": "Oh, the places Sagittarius goes! But… actually. This fire sign knows no bounds. Represented by the archer, Sagittarians are always on a quest for knowledge. The last fire sign of the zodiac, Sagittarius launches its many pursuits like blazing arrows, chasing after geographical, intellectual, and spiritual adventures. ",
    "Capricorn": "What is the most valuable resource? For Capricorn, the answer is clear: Time. Capricorn is climbing the mountain straight to the top and knows that patience, perseverance, and dedication is the only way to scale. The last earth sign of the zodiac, Capricorn, is represented by the sea-goat, a mythological creature with the body of a goat and the tail of a fish. Accordingly, Capricorns are skilled at navigating both the material and emotional realms.",
    "Aquarius": "Despite the 'aqua' in its name, Aquarius is actually the last air sign of the zodiac. Innovative, progressive, and shamelessly revolutionary, Aquarius is represented by the water bearer, the mystical healer who bestows water, or life, upon the land. Accordingly, Aquarius is the most humanitarian astrological sign. At the end of the day, Aquarius is dedicated to making the world a better place.",
    "Pisces": "If you looked up the word 'psychic' in the dictionary, there would definitely be a picture of Pisces next to it. Pisces is the most intuitive, sensitive, and empathetic sign of the entire zodiac — and that’s because it’s the last of the last. As the final sign, Pisces has absorbed every lesson — the joys and the pain, the hopes and the fears — learned by all of the other signs. It's symbolized by two fish swimming in opposite directions, representing the constant division of Pisces' attention between fantasy and reality.",
}

def horo_description():
	if horo_sign == "Aries":
		print(sign_description["Aries"])
	elif horo_sign == "Taurus":
		print(sign_description["Taurus"])
	elif horo_sign == "Gemini":
		print(sign_description["Gemini"])
	elif horo_sign == "Cancer":
		print(sign_description["Cancer"])
	elif horo_sign == "Leo":
		print(sign_description["Leo"])
	elif horo_sign == "Virgo":
		print(sign_description["Virgo"])
	elif horo_sign == "Libra":
		print(sign_description["Libra"])
	elif horo_sign == "Scorpio":
		print(sign_description["Scorpio"])
	elif horo_sign == "Sagittarius":
		print(sign_description["Sagittarius"])
	elif horo_sign == "Capricorn":
		print(sign_description["Capricorn"])
	elif horo_sign == "Aquarius":
		print(sign_description["Aquarius"])
	elif horo_sign == "Pisces":
		print(sign_description["Pisces"])
	else:
		print("ERR: Something went wrong... please try again")

horoscope()

print("Your Name is:", name.capitalize())
print(name_list)
print("You were born in:", str(day) + " " + str(month.capitalize()) + " " + str(year))
print("Todays date is : ")
print(the_date)
print("That means you have been alive for about " + str(days) + " days")
print("Your astrological sing is:", horo_sign)
horo_description()
