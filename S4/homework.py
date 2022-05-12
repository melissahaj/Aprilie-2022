# 1. Scrieti un program care afiseaza numerele prime din intervalul [0 100]

# min = 0
# max = 100
# print("Numerele prime cuprinse intre", min, "si", max, "sunt:")

# for num in range(min , max + 1):
#     if num > 1:
#         for i in range(2, num):
#             if(num % i) == 0:
#                 break
#         else:
#             print(num)  
# 
# 

# exempul lui Mihai
#  for n in range(0, 100):
#     prim = True
#     for i in range(2, n):
#         if n % i == 0:
#             prim = False
#             break
#     if prim:
#         print(n)  



#  4. Scrieti un program care citeste de la tastatura un nr natural "n", 
# si afiseaza n! (factorial). 6! = 1 * 2 * 3 * 4 * 5 * 6

# n = int(input("n = "))
# factorial = 1

# for i in range(1, n + 1):
#     factorial = factorial * i
# print("Numarul factorial al", n, "este:", factorial)    


# 5. Scrieti un program care afiseaza toate litere (capitale) ale 
# alfabetului englez, pe aceiasi linie despartite prin spatiu. 
# **A se vedea tablelul ASCII. chr(65) -> A


# for i in range(65, 91):
#     chr(i)
#     print(chr(i), end = " ")

# 6. Intr-o cutie se află 300 de bile, numerotate cu numere începând de la unu, 
# din trei în trei. Toate bilele cărora le corespund numere pare sunt verzi. 
# Să se afle câte bile verzi sunt.

# even_count = 0
# for i in range(1, 900, 3):
#     if i % 2 == 0:
#         print(i, end = " ")
#         even_count = even_count + 1
# print("Total bile verzi = ", even_count)


# o alta varianta
# i = 0
# nr_pe_bile = 1
# bile_verzi = 0

# while i <= 300 :
#     if nr_pe_bile % 2 == 0 :
#         bile_verzi += 1
#     i += 1
#     nr_pe_bile += 3 
# print ("Bile verzi= ",bile_verzi)



# 7. Scrieti un program care citeste doua nr de la tastatura si calculeaza produsul
# lor. A nu se utiliza operatorul de inmultire.



# 8. Scrieti un program de tip joc "ghiceste numarul".
#     Cerinte: 
#     1. Programul genereaza un numar aleator in intervalul [1, 99].
#     2. Intr-o bucla conditionata de gasirea numarului cautat:
#         - se citeste de la tastatura un numar
#         - se compara cu numarul cautat
#         - daca numarul introdus este mai mic decat numarul cautat se afiseaza +
#         - daca este mai mic se afiseaza -
#     3. Dupa ce numarul este ghicit se afiseaza un mesaj de felicitare si numarul cautat.


# import random

# print("Incepe jocul!")
# random_number = random.randint(1, 99)

# n = int(input("Introduceti un numar intre 1 si 99: "))
# #for n in random_number:
# while(n == random_number):
#     print("felicitari")
# while(n > random_number):
#     print("-")
#     n = random_number
# while(n < random_number):
#     print("+")

# Varianta buna:
# print("Incepe jocul")
# print("Introduceti un numar intre 1 ai 99")

# import random

# n = -1
# x = random.randit(1, 100)

# while x != n:
#     n = int(input(" "))

#   if x > n:
#         print(" + ")
        

#     else:
#         print(" - ")
       

# print("Felicitari!")
# print("Ai ghicit numarul: ", n)










    

