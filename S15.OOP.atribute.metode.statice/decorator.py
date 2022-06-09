# decoratorul adauga functionalitate unei functii deja scrise

# debug decorator
from datetime import datetime
import time

# decoratorul trebuie sa fie o functie care returneaza o alta functie
def debuger(f):
    def inner(*args): # inglobeaza un nr nelimitat de argumente
         print("S-a apelat functia xxx la ora", datetime.now() , "pentru argumentele =", args)
        start = time.time()
        print("Rezultatul apelului", f(*args))
        stop = time.time()
        print("Apelul a durat x secunde", stop - start)

    return inner

@debuger
def cube_volume(edge):
    """Calculate cube volume in liters"""
    return edge ** 3 * 1000

@debuger
def reverse(n):
    rev = 0
    while n != 0:
        c = n % 10  #rest
        n = n // 10 #catul
        rev = rev * 10 + c

cube_volume(10) # debuger(cube_volume0)(10)
reverse(234)
# inner(10)
# l = 29

# print("S-a apelat functia cube_volume la ora", datetime.now() , "pentru edge =", l)
# start = time.time()
# cube_volume(l)
# stop = time.time()
# print("Apelul a durat x secunde", stop - start)


# print("S-a apelat functia reverse la ora", datetime.now() , "pentru n =", l)
# start = time.time()
# reverse(l)
# stop = time.time()
# print("Apelul a durat x secunde", stop - start)

# def deco(f, n):
#     print("S-a apelat functia reverse la ora", datetime.now() , "pentru n =", n)
#     start = time.time()
#     f(n)
#     stop = time.time()
#     print("Apelul a durat x secunde", stop - start)

# deco(reverse, 29)
# deco(cube_volume, 29)












