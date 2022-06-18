from pprint import pprint

from pkg_resources import compatible_platforms
text = "meliSSa haJ aBdo"

calatori = [
    "Otavă Bogdan",
    "Greta Mihaela Geabelea",
    "Iustin Gabriel Manciu",
    "Corina Lungu",
    "Melissa Madalina Haj Abdo",
    "Gabriel Guțui",
    "George Valeanu",
    "Andreea-Simona Telegeanu",
    "Ionuț Alin Preda",
    "Arthur Timbalariu",
    "Cristian Laurentiu Șandor",
    "Alex Raul Bonat-Mihalca",
    "Artsanyo Dennis Kachi",
    "Sergiu Mihai Predel",
    "Marian-Gabriel Tohaneanu-Iatan",
    "Irina Florentina Barbu",
    "Cordos Simona",
]

py_text = """Python is an interpreted, interactive, object-oriented programming language. It incorporates modules, exceptions, dynamic typing, very high level dynamic data types, and classes. It supports multiple programming paradigms beyond object-oriented programming, such as procedural and functional programming. Python combines remarkable power with very clear syntax. It has interfaces to many system calls and libraries, as well as to various window systems, and is extensible in C or C++. It is also usable as an extension language for applications that need a programmable interface. Finally, Python is portable: it runs on many Unix variants including Linux and macOS, and on Windows.
To find out more, start with The Python Tutorial. The Beginner's Guide to Python links to other introductory tutorials and resources for learning Python."""

idx_virgula = py_text.find(",") # gaseste indexul sub-sringului cautat
# print(py_text[idx_virgula]) # ia textul pana la virgula
"""
idx_virgula = -1
done = False

while not done:
    idx_virgula = py_text.find(",", idx_virgula + 1)
    if idx_virgula != -1:
        print(idx_virgula)
    else:
        done = True
"""

# inlocuire
# print(py_text.replace(" ", ""))  # asa am scos spatiul dintr-un text (inlocuire)


#count
print(py_text.count("and")) # de cate ori apare "and" - daca numaram punctele aflam cate propozitii sunt

# split, rupe in bucati dupa delimitator
print(py_text)
propozitii = (py_text.split(". "))
print(len(propozitii)) # cate propozitii are textul

# am separat cuvintele
words = py_text.split()


# de cate ori apare fiecare cuvant
# eliminam virgulele, punctele, apostroafele, le facem pe toate cu litere mici si dupa le compatible_platforms

clean_words = []

for word in words:
    clean_words.append(word.lower().strip(",.'[]():;-+=")) #lower litera mica toate

pprint(clean_words)

max_len = 0

# asa aflam lungimea max a unui cuvant dintr-o lista de cuvinte
for word in clean_words:
    if len(word) > max_len:
        max_len = len(word)

passed_words = []
for word in clean_words:
    if word not in passed_words:
        print(word.ljust(max_len + 10, "."), clean_words.count(word))
        passed_words.append(word)





name = "Alin"
surname = "Preda"
print(name.rjust(10)) # rjust adauga atatea caractere in FATA cate sunt necesare pentru a avea lungimea de cat ii dam noi
print(surname.ljust(10, "-")) # ljust adauga atatea caractere in SPATE cate sunt necesare pentru a avea lungimea de cat ii dam noi

print(name.zfill(10)) # pune 0 inainte 












