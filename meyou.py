# Meyou matching

while True:
    name_entry = input("What is your name? ")
    try:
        if not name_entry.isalpha():
            raise ValueError("Please enter your name using letters only.")
    except ValueError as e:
        print(e)
    else:
        break

print("Hello,", name_entry)

age_entry = input("How old are you? : ")
try:
    age_value = int(age_entry)
except ValueError:
    print("Invalid input. Please enter an integer.")
try:
    result = age_value
except NameError:
    print("Letter not needed for age entry")


minimum_age_requirement = 24
maximum_age_requirement = 27

if age_value < minimum_age_requirement:
    print("You do not qualify!")
    exit()
elif age_value > maximum_age_requirement :
        print("You do not qualify!")
        exit()
else:
    print("You qualify!")


can_cook = True
not_like_football = True
a_believer = True

Yes = True
No = False

qualifications = {input("Can you cook? (Yes or No) \n"), input("Do you like football? (Yes or No) \n"), input("Are you a Believer? (Yes or No) \n")}

if qualifications == "Yes":
    print("You entered Yes")
elif qualifications == "No":
    print("You entered No")
else:
    print("Your answer must be Yes or No")


if can_cook or not_like_football:
    print("You qualify")
else:
    print("you do not qualify")
    exit()



