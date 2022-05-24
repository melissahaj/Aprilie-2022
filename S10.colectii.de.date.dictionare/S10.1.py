# lista asociativa = dictionar = maps = maping = mapari
# putem folosi la key si numere si str
# dictionarele nu sunt ordonate in nici un fel

empty_dict = {}
empty_dict1 = dict()

print(empty_dict)
print(type(empty_dict))
print(type(empty_dict1))

user_info = {
    "name": "Alex",
    "age": 28,
    "email": "alex.radu@email.com",
    "gender": "M"
}

user_info1 = ["Alex", 28, "alex.radu@email.com", "M"] #lista
print("Nume:", user_info1[0])  # asa  obtinem din lista informatii
print("Varsta:", user_info1[1]) 


print("Nume:", user_info["name"])  # asa obtinem din dictionar informatii
print("Varsta:", user_info["age"]) 

print(user_info.get("name", "Negasit"))  # a doua metoda cum obtinem din dictionar, asta o recomanda sa o folosim prima e cheia,
                                                # a doua da negasit daca nu exista in dictionar


# modificare dict
print("------------------")
user_info['name'] = "George"

print("Nume:", user_info["name"]) 
print("Varsta:", user_info["age"])

# adugare 
print(empty_dict)

empty_dict["ro"] = "Buna ziua!" #ro este cheia

print(empty_dict)

empty_dict["en"] = "Good afternoon!"
print(empty_dict)

print(empty_dict["en"]) # am printat doar en, fara ro

# stergere
print("--------------")
del user_info['email']
print(user_info)


# CRUD - create read update delete
empty_dict2 = {
    2010: "Dragon",
    2011: "Cocos",
    2012: "Iepure",
}

empty_dict2[2013] = "Catel"

print(empty_dict2[2013])


fool = {
    2: "Two",
    2.0: "Also two",
    2.1: "Almost two",

}

print(fool[2])

# sa iau din fisierul lui Mihai resul
# de cautat lambda