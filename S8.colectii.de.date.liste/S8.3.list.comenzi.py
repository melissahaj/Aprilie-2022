user_id = [33, 455,3, 32, 34, 12, 90, 32, 234]
leader_board = ['Alex', 'George', 'Ionut']

print(user_id)

# Lungimea listei
print("Lungimea listei este:", len(user_id))

# Maximul listei
print("Maximul listei este:", max(user_id))
print(max(leader_board)) #la stringuri foloseste ultima litera mai mare adica I - Ionut este  mai mare decat G sau A

# Minimul listei
print("Minimul listei este:", min(user_id))
print(min(leader_board))

print("-" * 30)

# Adaugare element nou - append
user_id.append(100)
print(user_id)
print("Lungimea listei este:", len(user_id))

# Eliminare element
user_id.remove(3)
print("Dupa remove")
print(user_id)

# Verificare daca valoarea face parte din lista
# value_to_remove = int(input("Remove value:")) #elimini din tastatura 
# if value_to_remove in user_id: #daca valoare face parte din user id
#     user_id.remove(value_to_remove)
# else: 
#     print("Valoarea nu exista in lista.")

# Numarul de aparitii al unui element
print("Elementul 33 apare de", user_id.count(33), "ori")
print(user_id.count(33))

# Insert la index - adaugam un element nu doar la final cum face append, ci oriunde vrem in lista
user_id.insert(1, 0) #in pozitia 1 se adauga 0, adica dupa primul nr
user_id.insert(-1, 0) #cu -1 se adaunga penultimul acel o

print("Dupa insert 0")
print(user_id)

# Gaseste indexul unei valori  - adica prima aparitie a lui 32
# print(user_id.index(32)) - asa gasim ce index are o valoare
index_magic = user_id.index(32)
user_id.insert(index_magic + 1, "x")

print("Dupa index magic")
print(user_id)



print("END")
