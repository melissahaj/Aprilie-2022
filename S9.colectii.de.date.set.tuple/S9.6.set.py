magic_numbers = {1, 44, 3, 23, 2, 33}
wrong_numbers = {88, 22, 34, 44}

print(magic_numbers)

# magic_numbers.update([1, 2, 3, 99]) #adaungam un element nou la set prin update

intersection = magic_numbers.intersection(wrong_numbers) #intersection.update altereaza lista initiala si arata doar elemnetul comun
difference = magic_numbers.difference(wrong_numbers) #difference.update altereaza lista initiala si arata doar elementele necomune

print(magic_numbers)
print(intersection)
print(difference)

