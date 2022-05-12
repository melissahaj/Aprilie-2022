# for i in range(10, 0):
#     print("Interatia: ", i + 1)
#     print("i =", i)



# range(3) -> 0 1 2
# 1. i = 0
# 2. i = 1
# 3. i = 2

# range(10) produce intervalul [0, 10) - nu il include pe 10

# range(10) -> [0,10) -> 0...9
# range(stop)

# range(3, 10) -> [3, 10) -> 3...9
# range(start, stop)

# range(3, 10, 2) -> 3, 5, 7, 9
# range(start, stop, pas) -> din 2 in 2

# range(11, 0) -> nu returneaza nimic
# range(10, -1, -1) -> 10, 9, 8...0

# for i in range(1001):
#     if i % 2 == 1:
#         print(i)

# Scrieti un program care citeste de la tastatura un nr natural "n", 
# si afiseaza suma primelor n numere multiple de 5 si 3.


n = input("n = ")
n = int(n)
suma = 0

for i in range(3, n, 3):
    if i % 5 == 0:
        suma = suma + i
print(suma)
        
    
