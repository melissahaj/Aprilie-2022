user_info = {
    "name": "Alex",
    "age": 28,
    "email": "alex.radu@email.com",
    "gender": "M"
}

# lista cheilor
u_i_keys1 = list(user_info.keys()) #trebuie modificat dic in lista ca sa ne dea cheile vechi dar si cele adaugate recent

for key in u_i_keys1():
    print(key)

user_info['address'] = "Bucharest"



