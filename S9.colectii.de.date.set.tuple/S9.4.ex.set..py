# Scrie o functie care verifica daca o lista este uniforma
# l1 = [2, 2, 2, 2, 2, 2]
# o varianta de rezolvare este  minim si maxim din exemplul de lista uniforma

def is_uniform(list_in):
    return len(set(list_in)) == 1

print(is_uniform([1, 1, 2]))