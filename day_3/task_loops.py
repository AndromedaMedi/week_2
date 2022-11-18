
ages = [5, 15, 64, 27, 84, 26]

odd_ages = [age for age in ages if age % 2 != 0]
print(odd_ages)


chicken_names = ["Hen Solo", "Cluck Norris", "Hennifer Lopez", "ChewPekka", "Feather Locklear"]

long_chicken_names = [name for name in chicken_names if len(name) > 10]
print(long_chicken_names)

h_chicken_names = [name for name in chicken_names if name[0] == 'H' ]
print(h_chicken_names)


words = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
lower_first_letters = [letter[0].lower() for letter in words]
                # make the 1st letter lower for all letters in words
print(lower_first_letters)