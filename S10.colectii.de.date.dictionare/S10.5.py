# sortarea dictionarului dupa key

user_info = {
    "name": "Alex",
    "age": 28,
    "email": "alex.radu@email.com",
    "gender": "M"
}

china_years = {
    2010: "Dragonului",
    2011: "Cocosului",
    2012: "Iepurelui",
}


sorted_user_info = sorted(user_info.items())

print("Sortat dupa chei")
for k, v in user_info.items():
    print(k,"\\", v)


print("Sortat dupa valori")
def comparator(t):
    return t[1]
for k, v in sorted(china_years.items(), key=comparator): #key=lambda adica lambda este functia de mai sus def
    print("Anul", k, "a fost anul", v) # sortat alfabetic dupa valori


