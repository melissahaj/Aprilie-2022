def say_welcome_message(name, lucky_number): #cati parametrii avem in functie, atatia sa avem si in apel
    """Prints welcome message""" # asa se comenteaza o functie
    
    print("Welcome back", name, "!")
    print("Lucky number is", lucky_number)

# apel
say_welcome_message("Mihai", 19)
say_welcome_message("Alex", 33)

# ordinea parametrilor dintr`o functie, trebuie respectata identic si in apel`
# DRY = Do not Repeat Yourself
# Welcome back, Melissa!
# Lucky number is 20.

# Welcome back, Alexandra!
# Lucky number is 20.