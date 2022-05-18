user_id = [33, 455,3, 32, 34, 12, 90, 32, 234]

# Reversul listei !! opereaza pe lista
# print("Lista in stare initiala")
# print(user_id)

# user_id.reverse()

# print("Dupa reverse")
# print(user_id)

# List Sliceing - ex:primele 3 element din lista - ":" stanga inseamna start dreapta stop
top_three_users = user_id[:3] #nu include indexul 3 pentru ca lista porneste de la 0 si este 0, 1,2 adica 3 elemente
print("user_id", user_id)
print("top_three_users", top_three_users)

# List sliceing - ultimul element
last_element = user_id[-1:]
print(last_element)

# List sliceing interval
print(user_id[1:4])