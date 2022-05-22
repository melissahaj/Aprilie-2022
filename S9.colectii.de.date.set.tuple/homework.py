# 1. Definiti o martrice 5 x 5 si afisati numerele de pe diagonala principala si 
# numerele de pe diagonala secundara.


matrix = [
    [1, 2, 5, 7, 10],
    [4, 25, 6, 9, 7],
    [99, 8, 9, 11, 23],
    [3, 7, 2, 9, 10],
    [23, 40, 9, 88, 51]
]

print("Numerele din diagonala principala sunt:", matrix[0][0],matrix[1][1],matrix[2][2],matrix[3][3],matrix[4][4])
print("Numerele din diagonala secundara sunt:", matrix[0][4],matrix[1][3],matrix[2][2],matrix[3][1],matrix[4][0])


