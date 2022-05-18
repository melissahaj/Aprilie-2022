leader_board = ['Alex', 'George', 'Ionut']

# 0  1  2
# leader_board = []
# leader_board = list()

print(type(leader_board))
print(leader_board)

print("-" * 30)
print("Numar castigatori:", len(leader_board))

print("Locul 1:", leader_board[0])
print("Ultimul loc:" , leader_board[-1])

print("-" * 30)

print("Locul 2 initial:", leader_board[1])

leader_board[1] = "Andrei"

print("Dupa modificare")
print("Locul 2:", leader_board[1])

del leader_board[-1]
print("Dupa stergerea ultimului element, lungimea este:", len(leader_board))
print(leader_board)

print("-" * 30)
print("Castigatorii sunt:")
for name in leader_board: #in loc de name se poate pune orice i,x,e etc
    print(name)

print("STOP")