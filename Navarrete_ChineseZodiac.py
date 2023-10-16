def find_chinese_zodiac_sign(year):
    start_year = 1900  # The Chinese zodiac cycle starts from 1900.

    if year < start_year:
        print("Year is out of range. The Chinese zodiac cycle starts from 1900.")
    else:
        year_difference = year - start_year
        zodiac_index = year_difference % 12

        if zodiac_index == 0:
            print(f"The Chinese zodiac sign for the year {year} is Monkey!")
        elif zodiac_index == 1:
            print(f"The Chinese zodiac sign for the year {year} is Rooster!")
        elif zodiac_index == 2:
            print(f"The Chinese zodiac sign for the year {year} is Dog!")
        elif zodiac_index == 3:
            print(f"The Chinese zodiac sign for the year {year} is Pig!")
        elif zodiac_index == 4:
            print(f"The Chinese zodiac sign for the year {year} is Rat!")
        elif zodiac_index == 5:
            print(f"The Chinese zodiac sign for the year {year} is Ox!")
        elif zodiac_index == 6:
            print(f"The Chinese zodiac sign for the year {year} is Tiger!")
        elif zodiac_index == 7:
            print(f"The Chinese zodiac sign for the year {year} is Rabbit!")
        elif zodiac_index == 8:
            print(f"The Chinese zodiac sign for the year {year} is Dragon!")
        elif zodiac_index == 9:
            print(f"The Chinese zodiac sign for the year {year} is Snake!")
        elif zodiac_index == 10:
            print(f"The Chinese zodiac sign for the year {year} is Horse!")
        else:
            print(f"The Chinese zodiac sign for the year {year} is Sheep!")


# Input year from the user
year = int(input("Enter your birth year: "))

# Find and display the Chinese zodiac sign for the given year
find_chinese_zodiac_sign(year)

