user_name = set()

user_name.add("Mihai")
user_name.add("Alex")

print(user_name)

user_name.remove("Mihai")
print(user_name)

if "Mihai" in user_name:
    user_name.remove("Mihai") 
    # asa verificam daca un element face parte dintr-un set, in loc de in se poate si not, adica reversul

print(user_name)

user_name.clear()
print(user_name)