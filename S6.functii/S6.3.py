# Scrie o functie care verifica daca un nr natural este palindrom. 111 121 292 2992 = are aceeasi valoare daca il citim de la dreapta la stanga sau invers
# functie care returneza True daca este un nr palidrom
# citim de la tastatura un nr
# apelam functia



# n sa comparam cu un nr format pe baza nr initial citit de la dreapta catre stanga
#  178 != 871 False
# 121== 121 True

# algoritm pt inversare citire. trebuie extras pe rand ultima cifra din nr citit
# ex: 178 extragem
# 8 ramane
# 17 extragem
# 7
# ramane 1
# scoatem 1 nu mai ramane nimic

# 178 % 10 = 8
# 178 // 10 = 17 - impartire cu rest

# ca sa formam un nr luam 8 * 10 + 7 = 87
# 87 * 10 + 1 = 871 (obtinem reversul)

# Functie care arata in oglinda un nr 178 

def reverse(n):
    rev = 0
    while n != 0:
        c = n % 10  #rest
        n = n // 10 #catul
        rev = rev * 10 + c #rev = 0 initial === 0*10+1 = 1 apoi 1*10+7=17 apoi 17 * 10 + 8 = 178 ===rev isi schimba valoarea

def reverse(n):

    return rev

def palindrom(n):
    """Check if palindrom"""
    if n == reverse(n):
        return True
    else:
        return False

n = int(input("Introduceti un numar: "))

if palindrom(n):
    print("Numarul este palindrom")
else:
    print("Numarul nu este palindrom")

    


