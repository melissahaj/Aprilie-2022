# cum extragem lista valorilor; values => obiect de tip view

user_info = {
    "name": "Alex",
    "age": 28,
    "email": "alex.radu@email.com",
    "gender": "M"
}

for v in user_info.values():
    print(v)

u_i_values1 = user_info.values()
print(type(u_i_values1))

for v in u_i_values1:
    print(v)

